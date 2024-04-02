import ftplib
import logging
import os
import multiprocessing
import urllib.error
import urllib.request as request

from pysus.utilities.readdbc import dbc2dbf, dbf_to_csvgz
from time import sleep

logger=logging.getLogger()

STORAGE_PATH = './datasus_api/util/tmp/'
#STORAGE_PATH = '/app/datasus_api/util/' # Docler path

def run_function_with_timeout(target_function, args=(), timeout_seconds=60):

    process = multiprocessing.Process(target=target_function, args=args)

    process.start()

    process.join(timeout_seconds)

    if process.is_alive():
        process.terminate()
        process.join()

        raise TimeoutError(f"Function {target_function.__name__} timed out after {timeout_seconds} seconds")


def connect_ftp(path):
    url = "ftp.datasus.gov.br"
    
    ftp = ftplib.FTP(url)
    ftp.login()
    ftp.cwd(path)
    return ftp


def get_ftp_connection(base_name, filename_prefix):
    base_name = base_name.upper()

    ftp_connection = None
    ftp_path = ''
    if base_name == 'CIH':
        ftp_path = 'dissemin/publicos/CIH/200801_201012/Dados'

    elif base_name == 'CNES':
        ftp_path = f'dissemin/publicos/{base_name}/200508_/Dados/{filename_prefix}'

    elif base_name == 'PCE':
        ftp_path = 'dissemin/publicos/PCE/DADOS'

    elif base_name == 'SIASUS' or base_name == 'SIHSUS':
        ftp_path = f'dissemin/publicos/{base_name}/200801_/Dados'

    elif base_name == 'PO':
        ftp_path = 'dissemin/publicos/PAINEL_ONCOLOGIA/DADOS'
    
    elif base_name == 'CIHA':
        ftp_path = f'dissemin/publicos/{base_name}/201101_/Dados'

    elif base_name == 'SIM1':
        ftp_path = 'dissemin/publicos/SIM/CID10/DORES/'

    elif base_name == 'SIM2':
        ftp_path = 'dissemin/publicos/SIM/PRELIM/DORES/'
    
    elif base_name == 'SINAN1':
        ftp_path = 'dissemin/publicos/SINAN/DADOS/FINAIS/'

    elif base_name == 'SINAN2':
        ftp_path = 'dissemin/publicos/SINAN/DADOS/PRELIM/'
    
    elif base_name == 'SINASC1':
        ftp_path = 'dissemin/publicos/SINASC/1996_/Dados/DNRES/'
    
    elif base_name == 'SINASC2':
        ftp_path = 'dissemin/publicos/SINASC/PRELIM/DNRES/'
    
    ftp_connection = connect_ftp(ftp_path)

    return (ftp_connection, ftp_path)


def get_init_index_year(filename):
    init_index_year = 0
    for char in filename:

        if not char.isdigit():
            init_index_year += 1
        
        else:
            break

    return init_index_year


def get_filenames(ftp_connection, filename_prefix):

    list_file_names = ftp_connection.nlst()
    

    filename_we = ''
    for filename in list_file_names:
        if filename.startswith(filename_prefix) and filename.endswith('.dbc'):
            filename_we = filename.split('.')[0]
            break

    init_year_index = get_init_index_year(filename_we)

    filtered_list = []
    for filename in list_file_names:

        if filename.startswith(filename_prefix) and filename[init_year_index:init_year_index+2].isdigit() and filename.endswith('.dbc'):
            filtered_list.append(filename)


    return filtered_list


def aux_get_file(filename_dbc, storage_path, ftp_path):

    url = f'ftp://ftp.datasus.gov.br/{ftp_path}/{filename_dbc}'

    filename_dbf = filename_dbc.replace('.dbc', '.dbf')

    file_path_dbc = storage_path + filename_dbc
    file_path_dbf = storage_path + filename_dbf
    
    print(f'Baixando arquivo: {filename_dbc}\n')
    request.urlretrieve(url, file_path_dbc)
    
    print(f'Convertendo o arquivo {filename_dbc} para csv...\n')
    dbc2dbf(file_path_dbc, file_path_dbf)
    os.remove(file_path_dbc)
    
    dbf_to_csvgz(file_path_dbf)
    os.remove(file_path_dbf)


def get_file(filename_dbc, storage_path, ftp_path):

    try:
        timeout_seconds = 2400 #40 minutos

        run_function_with_timeout(aux_get_file, (filename_dbc, storage_path, ftp_path), timeout_seconds)

    except TimeoutError as te:
        logger.exception(te)
        sleep(3)
        
    except urllib.error.URLError as e:
        logger.error(f'The {filename_dbc} file is not available!\n')
        sleep(3)
        
    except Exception as e:
        logger.error(f"Error downloading file: \n\n\t--> {e}")
        sleep(3)


def download_file(base_name, filename, filename_prefix):
    filename = filename + '.dbc'
    
    try:
        ftp_connection, ftp_path = get_ftp_connection(base_name, filename_prefix)

    except Exception as e:
        logger.error(f"Error connecting to FTP server: \n\n\t--> {e}")
        raise

    filenames = get_filenames(ftp_connection, filename_prefix)
    if not f'{filename}' in filenames:
        raise DownloadDataException(f'The file {filename} is not available!')

    if ftp_connection:
        ftp_connection.quit()

    get_file(filename, STORAGE_PATH, ftp_path)


class DownloadDataException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    
if __name__ == '__main__':
    download_file('CNES', 'LTPB2101', 'LT')

    
