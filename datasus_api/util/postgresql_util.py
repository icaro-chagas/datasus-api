import psycopg2
import logging
import enum
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger()

STORAGE_PATH = './datasus_api/util/tmp/'
#STORAGE_PATH = '/app/datasus_api/util/' # Docler path

class OperationType(enum.Enum):
    CREATE_TABLE = 1
    DROP_TABLE = 2
    DELETE_ALL_ROWS = 3
    INSERT_ROWS = 4
    SELECT_FILE_METADATA = 5
    SELECT_COLUMN_NAMES = 6

class PostgresDbOperations():
    
    def __init__(self, table_name):
        self.__table_name = table_name
        self.__logger = logging.getLogger(__name__)
        self.__connection = None
        
        
    
    def __connect_db(self):
        try:
            self.__connection = psycopg2.connect(
                host = os.environ.get('DB_HOST'),
                #host = 'postgres_container',
                #host = 'db',
                database = os.environ.get('DB_NAME'),
                user = os.environ.get('DB_USER'),
                password = os.environ.get('DB_PASSWORD'),
                port = os.environ.get('DB_PORT')
            )

        except psycopg2.Error as e:
            self.__logger.error("Unable to connect to the database.")
            self.__logger.error(e)
            raise  # Re-raise the exception for the calling code to handle

    
    def __disconnect_db(self):
        if self.__connection is not None:
            self.__connection.close()
    
    
    
    def __execute_command(self, command, operation_type, row_values=None, query_metadata=None):
        try:
            if self.__connection is None or self.__connection.closed:
                self.__connect_db()

            cursor = self.__connection.cursor()
            
            if operation_type in [OperationType.CREATE_TABLE, OperationType.DROP_TABLE,
                                  OperationType.SELECT_FILE_METADATA, OperationType.SELECT_COLUMN_NAMES]:
                cursor.execute(command)

                if operation_type in [OperationType.SELECT_FILE_METADATA, OperationType.SELECT_COLUMN_NAMES]:
                    return cursor.fetchall()
                
            elif operation_type == OperationType.DELETE_ALL_ROWS:
                for comm in command:
                    cursor.execute(comm)
                
            elif operation_type == OperationType.INSERT_ROWS:
                cursor.executemany(command, row_values)
                cursor.execute(query_metadata)
                
            self.__connection.commit()

        except psycopg2.Error as error:
            if operation_type in [OperationType.INSERT_ROWS, OperationType.DELETE_ALL_ROWS]:
                self.__connection.rollback()  # Rollback the transaction if there's an error

            self.__logger.error("Error executing command.")
            self.__logger.error(error)
            raise  # Re-raise the exception for the calling code to handle

        finally:
            self.__disconnect_db()  # Ensure connection is closed even if an error occurs
    
    
    def create_table(self, df):
        command = self.__get_create_command(df)
        self.__execute_command(command, OperationType.CREATE_TABLE)
        
                
    def drop_table(self):
        command = f"DROP TABLE {self.__table_name}"
        self.__execute_command(command, OperationType.DROP_TABLE)
        
                
    def delete_all_rows(self):
        table_name = self.__table_name
        table_type = table_name.split('_')[1]
        
        command1 = f"DELETE FROM {self.__table_name}"
        command2 = f"ALTER SEQUENCE {self.__table_name}_{table_type}_id_seq RESTART WITH 1;"
        commands = [command1, command2]
        
        self.__execute_command(commands, OperationType.DELETE_ALL_ROWS)


    def insert_rows(self, file_metadata, rows, columns):
        column_names = str(columns).replace('[',"").replace(']',"").replace("'", "")
        placeholders = '%s, '*len(columns)

        filename, prefix, uf, year, month = file_metadata

        query_metadata = f"INSERT INTO file_metadata (filename, prefix, uf, month, year, insertion_timestamp) VALUES ('{filename}', '{prefix}', '{uf}', '{month}', '{year}', CURRENT_TIMESTAMP);"
        
        command = f"INSERT INTO {self.__table_name}({column_names}) VALUES({placeholders[:-2]});"
        
        self.__execute_command(command, OperationType.INSERT_ROWS, rows, query_metadata)


    def insert_file(self, filename, prefix, uf, year, month):
        print('\nLendo o arquivo...')
        df = pd.read_csv(f'{STORAGE_PATH}{filename}.csv.gz', compression='gzip', low_memory=False)
        df['UF'] = uf
        df['ANO'] = year
        df['MES'] = month

        db_column_names = [col.upper() for col in self.get_column_names()]
        db_column_names.remove('ID')
        for db_column in db_column_names:
            if db_column not in df.columns:
                df[db_column] = None
        
        df = df[db_column_names]

        print('\nTransformando o arquivo em lista de tuplas...')
        rows = list(df.itertuples(index=False, name=None))

        file_metadata = (filename, prefix, uf, year, month)

        print('\nInserindo arquivo no banco de dados...')
        self.insert_rows(file_metadata, rows, df.columns.tolist())

        os.remove(f'{STORAGE_PATH}{filename}.csv.gz')

        del rows, df
        print('\nProcessamento finalizado!')


    # Tracking logic
    def get_inserted_files(self):
        select_query = "SELECT filename FROM file_metadata;"

        list_inserted_files = [filename_tuple[0] for filename_tuple in 
                               self.__execute_command(select_query, OperationType.SELECT_FILE_METADATA)]

        return list_inserted_files
    

    def get_column_names(self):
        select_query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{self.__table_name}' ORDER BY ORDINAL_POSITION;"

        return [column_tuple[0] for column_tuple in 
                self.__execute_command(select_query, OperationType.SELECT_FILE_METADATA)]
    

if __name__ == '__main__':
    db = PostgresDbOperations('lt_cnes')
    print(db.get_column_names())
    
