rd_dict = {
    'UF_ZI': {'type': 'CHAR (6)', 'description':  'Município Gestor.'},
    'ANO_CMPT': {'type': 'CHAR (4)', 'description': 'Ano de processamento da AIH, no formato aaaa.'},
    'MÊS_CMPT': {'type': 'CHAR (2)', 'description': 'Mês de processamento da AIH, no formato mm.'},
    'ESPEC': {'type': 'CHAR (2)', 'description': 'Especialidade do Leito'},
    'CGC_HOSP': {'type': 'CHAR (14)', 'description': 'CNPJ do Estabelecimento.'},
    'N_AIH': {'type': 'CHAR (13)', 'description': 'Número da AIH.'},
    'IDENT': {'type': 'CHAR (1)', 'description': 'Identificação do tipo da AIH.'},
    'CEP': {'type': 'CHAR (8)', 'description': 'CEP do paciente.'},
    'MUNIC_RES': {'type': 'CHAR (6)', 'description': 'Município de Residência do Paciente'},
    'NASC': {'type': 'CHAR (8)', 'description': 'Data de nascimento do paciente (aaaammdd).'},
    'SEXO': {'type': 'CHAR (1)', 'description': 'Sexo do paciente.'},
    'UTI_MES_IN': {'type': 'NUMERIC (2)', 'description': 'Zerado'},
    'UTI_MES_AN': {'type': 'NUMERIC (2)', 'description': 'Zerado'},
    'UTI_MES_AL': {'type': 'NUMERIC (2)', 'description': 'Zerado'},
    'UTI_MES_TO': {'type': 'NUMERIC (3)', 'description': 'Quantidade de dias de UTI no mês.'},
    'MARCA_UTI': {'type': 'CHAR (2)', 'description': 'Indica qual o tipo de UTI utilizada pelo paciente.'},
    'UTI_INT_IN': {'type': 'NUMERIC (2)', 'description': 'Zerado'},
    'UTI_INT_AN': {'type': 'NUMERIC (2)', 'description': 'Zerado'},
    'UTI_INT_AL': {'type': 'NUMERIC (2)', 'description': 'Zerado'},
    'UTI_INT_TO': {'type': 'NUMERIC (3)', 'description': 'Quantidade de diárias em unidade intermediaria.'},
    'DIAR_ACOM': {'type': 'NUMERIC (3)', 'description': 'Quantidade de diárias de acompanhante.'},
    'QT_DIARIAS': {'type': 'NUMERIC (3)', 'description': 'Quantidade de diárias.'},
    'PROC_SOLIC': {'type': 'CHAR (10)', 'description':  'Procedimento solicitado.'},
    'PROC_REA': {'type': 'CHAR (10)', 'description':  'Procedimento realizado.'},
    'VAL_SH': {'type': 'NUMERIC (13,2)', 'description': 'Valor de serviços hospitalares.'},
    'VAL_SP': {'type': 'NUMERIC (13,2)', 'description': 'Valor de serviços profissionais.'},
    'VAL_SADT': {'type': 'NUMERIC (13,2)', 'description': 'Zerado'},
    'VAL_RN': {'type': 'NUMERIC (13,2)', 'description': 'Zerado'},
    'VAL_ACOMP': {'type': 'NUMERIC (13,2)', 'description': 'Zerado'},
    'VAL_ORTP': {'type': 'NUMERIC (13,2)', 'description': 'Zerado'},
    'VAL_SANGUE': {'type': 'NUMERIC (13,2)', 'description': 'Zerado'},
    'VAL_SADTSR': {'type': 'NUMERIC (11,2)', 'description': 'Zerado'},
    'VAL_TRANSP': {'type': 'NUMERIC (13,2)', 'description': 'Zerado'},
    'VAL_OBSANG': {'type': 'NUMERIC (11,2)', 'description': 'Zerado'},
    'VAL_PED1AC': {'type': 'NUMERIC (11,2)', 'description': 'Zerado'},
    'VAL_TOT': {'type': 'NUMERIC (14,2)', 'description': 'Valor total da AIH.'},
    'VAL_UTI': {'type': 'NUMERIC (8,2)', 'description': 'Valor de UTI.'},
    'US_TOT': {'type': 'NUMERIC (10,2)', 'description': 'Valor total, em dólar.'},
    'DI_INTER': {'type': 'CHAR (8)', 'description': 'Data de internação no formato aaammdd.'},
    'DT_SAIDA': {'type': 'CHAR (8)', 'description': 'Data de saída, no formato aaaammdd.'},
    'DIAG_PRINC': {'type': 'CHAR (4)', 'description': 'Código do diagnóstico principal (CID10).'},
    'DIAG_SECUN': {'type': 'CHAR (4)', 'description': 'Código do diagnostico secundário (CID10). Preenchido com zeros a partir de 201501.'},
    'COBRANCA': {'type': 'CHAR (2)', 'description': 'Motivo de Saída/Permanência'},
    'NATUREZA': {'type': 'CHAR (2)', 'description': 'Natureza jurídica do hospital (com conteúdo até maio/12). Era utilizada a classificação de Regime e Natureza.'},
    'NAT_JUR': {'type': 'CHAR (4)', 'description': 'Natureza jurídica do Estabelecimento, conforme a Comissão Nacional de Classificação - CONCLA'},
    'DESTAO': {'type': 'CHAR (1)', 'description': 'Indica o tipo de gestão do hospital.'},
    'RUBRICA': {'type': 'NUMERIC (5)', 'description': 'erado'},
    'IND_VDRL': {'type': 'CHAR (1)', 'description': 'Indica exame VDRL.'},
    'MUNIC_MOV': {'type': 'CHAR (6)', 'description': 'Município do Estabelecimento.'},
    'COD_IDADE': {'type': 'CHAR (1)', 'description': 'Unidade de medida da idade.'},
    'IDADE': {'type': 'NUMERIC (2)', 'description': 'Idade.'},
    'DIAS_PERM': {'type': 'NUMERIC (5)', 'description': 'Dias de Permanência.'},
    'MORTE': {'type': 'NUMERIC (1)', 'description': 'Indica Óbito'},
    'NACIONAL': {'type': 'CHAR (2)', 'description': 'Código da nacionalidade do paciente.'},
    'NUM_PROC': {'type': 'CHAR (4)', 'description': 'Zerado'},
    'CAR_INT': {'type': 'CHAR (2)', 'description': 'Caráter da internação'},
    'TOT_PT_SP': {'type': 'NUMERIC (6)', 'description': 'erado'},
    'CPF_AUT': {'type': 'CHAR (11)', 'description': 'Zerado'},
    'HOMONIMO': {'type': 'CHAR (1)', 'description': 'Indicador se o paciente da AIH é homônimo do paciente de outra AIH.'},
    'NUM_FILHOS': {'type': 'NUMERIC (2)', 'description': 'úmero de filhos do paciente.'},
    'INSTRU': {'type': 'CHAR (1)', 'description': 'Grau de instrução do paciente.'},
    'CID_NOTIF': {'type': 'CHAR (4)', 'description': 'CID de Notificação.'},
    'CONTRACEP1': {'type': 'CHAR (2)', 'description': 'Tipo de contraceptivo utilizado.'},
    'CONTRACEP2': {'type': 'CHAR (2)', 'description': 'Segundo tipo de contraceptivo utilizado.'},
    'GESTRISCO': {'type': 'CHAR (1)', 'description': 'Indicador se é gestante de risco.'},
    'INSC_PN': {'type': 'CHAR (12)', 'description': 'Número da gestante no pré-natal.'},
    'SEQ_AIH5': {'type': 'CHAR (3)', 'description': 'Sequencial de longa permanência (AIH tipo 5).'},
    'CBOR': {'type': 'CHAR (3)', 'description': 'Ocupação do paciente, segundo a Classificação Brasileira de Ocupações – CBO.'},
    'CNAER': {'type': 'CHAR (3)', 'description': 'Código de acidente de trabalho.'},
    'VINCPREV': {'type': 'CHAR (1)', 'description': 'Vínculo com a Previdência.'},
    'GESTOR_COD': {'type': 'CHAR (3)', 'description': 'Motivo de autorização da AIH pelo Gestor.'},
    'GESTOR_TP': {'type': 'CHAR (1)', 'description': 'Tipo de gestor.'},
    'GESTOR_CPF': {'type': 'CHAR (11)', 'description': 'Número do CPF do Gestor.'},
    'GESTOR_DT': {'type': 'CHAR (8)', 'description': 'Data da autorização dada pelo Gestor (aaaammdd).'},
    'CNES': {'type': 'CHAR (7)', 'description': 'Código CNES do hospital.'},
    'CNPJ_MANT': {'type': 'CHAR (14)', 'description': 'CNPJ da mantenedora.'},
    'INFEHOSP': {'type': 'CHAR (1)', 'description': 'Status de infecção hospitalar.'},
    'CID_ASSO': {'type': 'CHAR (4)', 'description': 'CID causa.'},
    'CID_MORTE': {'type': 'CHAR (4)', 'description': 'CID da morte.'},
    'COMPLEX': {'type': 'CHAR (2)', 'description': 'Complexidade.'},
    'FINANC': {'type': 'CHAR (2)', 'description': 'Tipo de financiamento.'},
    'FAEC_TP': {'type': 'CHAR (6)', 'description': 'Subtipo de financiamento FAEC.'},
    'REGCT': {'type': 'CHAR (4)', 'description': 'Regra contratual.'},
    'RACA_COR': {'type': 'CHAR (4)', 'description': 'Raça/Cor do paciente.'},
    'ETNIA': {'type': 'CHAR (4)', 'description': 'Etnia do paciente, se raça cor for indígena.'},
    'SEQUENCIA': {'type': 'NUMERIC (9)', 'description': 'Sequencial da AIH na remessa.'},
    'REMESSA': {'type': 'CHAR (21)', 'description': 'Número da remessa.'},
    'AUD_JUST': {'type': 'CHAR (50)', 'description': 'Justificativa do auditor para aceitação da AIH sem o número do Cartão Nacional de Saúde.'},
    'SIS_JUST': {'type': 'CHAR (50)', 'description': 'Justificativa do estabelecimento para aceitação da AIH sem o número do Cartão Nacional de Saúde.'},
    'VAL_SH_FED': {'type': 'NUMERIC (10,2)', 'description': 'Valor do complemento federal de serviços hospitalares. Está incluído no valor total da AIH.'},
    'VAL_SP_FED': {'type': 'NUMERIC (10,2)', 'description': 'Valor do complemento federal de serviços profissionais. Está incluído no valor total da AIH.'},
    'VAL_SH_GES': {'type': 'NUMERIC (10,2)', 'description': 'Valor do complemento do gestor (estadual ou municipal) de serviços hospitalares. Está incluído no valor total da AIH.'},
    'VAL_SP_GES': {'type': 'NUMERIC (10,2)', 'description': 'Valor do complemento do gestor (estadual ou municipal) de serviços profissionais. Está incluído no valor total da AIH.'},
    'VAL_UCI': {'type': 'NUMERIC (10,2)', 'description': 'Valor de UCI.'},
    'MARCA_UCI': {'type': 'CHAR (2)', 'description': 'Tipo de UCI utilizada pelo paciente.'},
    'DIAGSEC1': {'type': 'CHAR (4)', 'description': 'Diagnóstico secundário1.'},
    'DIAGSEC2': {'type': 'CHAR (4)', 'description': 'Diagnóstico secundário 2.'},
    'DIAGSEC3': {'type': 'CHAR (4)', 'description': 'Diagnóstico secundário 3.'},
    'DIAGSEC4': {'type': 'CHAR (4)', 'description': 'Diagnóstico secundário 4.'},
    'DIAGSEC5': {'type': 'CHAR (4)', 'description': 'Diagnóstico secundário 5.'},
    'DIAGSEC6': {'type': 'CHAR (4)', 'description': 'Diagnóstico secundário 6.'},
    'DIAGSEC7': {'type': 'CHAR (4)', 'description': 'Diagnóstico secundário 7.'},
    'DIAGSEC8': {'type': 'CHAR (4)', 'description': 'Diagnóstico secundário 8.'},
    'DIAGSEC9': {'type': 'CHAR (4)', 'description': 'Diagnóstico secundário 9.'},
    'TPDISEC1': {'type': 'CHAR (1)', 'description': 'Tipo de diagnóstico secundário 1.'},
    'TPDISEC2': {'type': 'CHAR (1)', 'description': 'Tipo de diagnóstico secundário 2.'},
    'TPDISEC3': {'type': 'CHAR (1)', 'description': 'Tipo de diagnóstico secundário 3.'},
    'TPDISEC4': {'type': 'CHAR (1)', 'description': 'Tipo de diagnóstico secundário 4.'},
    'TPDISEC5': {'type': 'CHAR (1)', 'description': 'Tipo de diagnóstico secundário 5.'},
    'TPDISEC6': {'type': 'CHAR (1)', 'description': 'Tipo de diagnóstico secundário 6.'},
    'TPDISEC7': {'type': 'CHAR (1)', 'description': 'Tipo de diagnóstico secundário 7.'},
    'TPDISEC8': {'type': 'CHAR (1)', 'description': 'Tipo de diagnóstico secundário 8.'},
    'TPDISEC9': {'type': 'CHAR (1)', 'description': 'Tipo de diagnóstico secundário 9.'}
}


sp_dict = {
    'SP_GESTOR': {'type': 'CHAR (6)', 'description': 'Unidade de Federação + Código Município de Gestão ou UF0000 se o Estabelecimento Executante está sob Gestão Estadual.'},
    'SP_UF': {'type': 'CHAR (2)', 'description': 'Unidade da Federação.'},
    'SP_AA': {'type': 'CHAR (4)', 'description': 'Ano da internação.'},
    'SP_MM': {'type': 'CHAR (2)', 'description': 'Mês da internação.'},
    'SP_CNES': {'type': 'CHAR (7)', 'description': 'Código do CNES do Estabelecimento de Saúde executante da AIH.'},
    'SP_NAIH': {'type': 'CHAR (13)', 'description': 'Número da AIH.'},
    'SP_PROCREA': {'type': 'CHAR (10)', 'description': 'Procedimento principal realizado na AIH.'},
    'SP_DTINTER': {'type': 'CHAR (8)', 'description': 'Data da internação.'},
    'SP_DTSAIDA': {'type': 'CHAR (8)', 'description': 'Data de saída.'},
    'SP_NUM_PR': {'type': 'CHAR (8)', 'description': 'Zerado'},
    'SP_TIPO': {'type': 'CHAR (2)', 'description': 'Zerado'},
    'SP_CPFCGC': {'type': 'CHAR (14)', 'description': 'CNES, CPF ou CNPJ do prestador do serviço do ato profissional.'},
    'SP_ATOPROF': {'type': 'CHAR (10)', 'description': 'Procedimento referente ao ato profissional.'},
    'SP_TP_ATO': {'type': 'CHAR (2)', 'description': 'Zerado.'},
    'SP_QTD_ATO': {'type': 'NUMERIC (4)', 'description': 'Quantidade de atos profissionais.'},
    'SP_PTSP': {'type': 'CHAR (6)', 'description': 'Quantidade de pontos.'},
    'SP_NF': {'type': 'CHAR (8)', 'description': 'Nota fiscal do material empregado quando órtese/prótese, quando não, o campo representa a data do ato.'},
    'SP_VALATO': {'type': 'NUMERIC (14,2)', 'description': 'Valor do ato profissional.'},
    'SP_M_HOSP': {'type': 'CHAR (6)', 'description': 'Município de localização do Estabelecimento Executante da AIH.'},
    'SP_M_PAC': {'type': 'CHAR (6)', 'description': 'Município de residência do paciente.'},
    'SP_DES_HOS': {'type': 'CHAR (1)', 'description': 'Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento.'},
    'SP_DES_PAC': {'type': 'CHAR (1)', 'description': 'Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento.'},
    'SP_COMPLEX': {'type': 'CHAR (2)', 'description': 'Complexidade do ato profissional.'},
    'SP_FINANC': {'type': 'CHAR (2)', 'description': 'Tipo de financiamento do ato profissional.'},
    'SP_CO_FAEC': {'type': 'CHAR (6)', 'description': 'Tipo de financiamento (04-FAEC) + Subtipo de financiamento relacionado ao tipo de financiamento (04-FAEC) do ato profissional.'},
    'SP_PF_CBO': {'type': 'CHAR (6)', 'description': 'Código de Ocupação Brasileira do Profissional que realizou o ato ou “00000” caso não tenha sido.'},
    'SP_PF_DOC': {'type': 'CHAR (15)', 'description': 'Documento de pessoa jurídica.'},
    'SP_PJ_DOC': {'type': 'CHAR (14)', 'description': 'Documento de pessoa física.'},
    'IN_TP_VAL': {'type': 'CHAR (1)', 'description': 'Tipo de valor: 1 - SP /2 –SH.'},
    'SEQUENCIA': {'type': 'CHAR (9)', 'description': 'Código sequencial.'},
    'REMESSA': {'type': 'CHAR (21)', 'description': 'Nome da remessa.'},
    'SERV_CLA': {'type': 'CHAR (6)', 'description': 'Serviço/Classificação.'},
    'SP_CIDPRI': {'type': 'CHAR (4)', 'description': 'CID Principal.'},
    'SP_CIDSEC': {'type': 'CHAR (4)', 'description': 'CID Secundário.'},
    'SP_QT_PROC': {'type': 'NUMERIC (4)', 'description': 'Quantidade de procedimentos realizados.'},
    'SP_U_AIH': {'type': 'CHAR (1)', 'description': 'Indicador único da AIH. Contabiliza a AIH sem repetições.'}
}


