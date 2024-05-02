from django.db import models

class DOEXTSim(models.Model):
    origem = models.CharField(max_length=60, null=True)
    tipobito = models.CharField(max_length=60, null=True)
    dtobito = models.CharField(max_length=60, null=True)
    horaobito = models.CharField(max_length=60, null=True)
    natur = models.CharField(max_length=60, null=True)
    codmunnatu = models.CharField(max_length=60, null=True)
    dtnasc = models.CharField(max_length=60, null=True)
    idade = models.CharField(max_length=60, null=True)
    sexo = models.CharField(max_length=60, null=True)
    racacor = models.CharField(max_length=60, null=True)
    estciv = models.CharField(max_length=60, null=True)
    esc = models.CharField(max_length=60, null=True)
    esc2010 = models.CharField(max_length=60, null=True)
    seriescfal = models.CharField(max_length=60, null=True)
    ocup = models.CharField(max_length=60, null=True)
    codmunres = models.CharField(max_length=60, null=True)
    lococor = models.CharField(max_length=60, null=True)
    codestab = models.CharField(max_length=60, null=True)
    estabdescr = models.CharField(max_length=60, null=True)
    codmunocor = models.CharField(max_length=60, null=True)
    idademae = models.CharField(max_length=60, null=True)
    escmae = models.CharField(max_length=60, null=True)
    escmae2010 = models.CharField(max_length=60, null=True)
    seriescmae = models.CharField(max_length=60, null=True)
    ocupmae = models.CharField(max_length=60, null=True)
    qtdfilvivo = models.CharField(max_length=60, null=True)
    qtdfilmort = models.CharField(max_length=60, null=True)
    gravidez = models.CharField(max_length=60, null=True)
    semagestac = models.CharField(max_length=60, null=True)
    gestacao = models.CharField(max_length=60, null=True)
    parto = models.CharField(max_length=60, null=True)
    obitoparto = models.CharField(max_length=60, null=True)
    peso = models.CharField(max_length=60, null=True)
    tpmorteoco = models.CharField(max_length=60, null=True)
    obitograv = models.CharField(max_length=60, null=True)
    obitopuerp = models.CharField(max_length=60, null=True)
    assistmed = models.CharField(max_length=60, null=True)
    exame = models.CharField(max_length=60, null=True)
    cirurgia = models.CharField(max_length=60, null=True)
    necropsia = models.CharField(max_length=60, null=True)
    linhaa = models.CharField(max_length=60, null=True)
    linhab = models.CharField(max_length=60, null=True)
    linhac = models.CharField(max_length=60, null=True)
    linhad = models.CharField(max_length=60, null=True)
    linhaii = models.CharField(max_length=60, null=True)
    causabas = models.CharField(max_length=60, null=True)
    cb_pre = models.CharField(max_length=60, null=True)
    comunsvoim = models.CharField(max_length=60, null=True)
    dtatestado = models.CharField(max_length=60, null=True)
    circobito = models.CharField(max_length=60, null=True)
    acidtrab = models.CharField(max_length=60, null=True)
    fonte = models.CharField(max_length=60, null=True)
    numerolote = models.CharField(max_length=60, null=True)
    tppos = models.CharField(max_length=60, null=True)
    dtinvestig = models.CharField(max_length=60, null=True)
    causabas_o = models.CharField(max_length=60, null=True)
    dtcadastro = models.CharField(max_length=60, null=True)
    atestante = models.CharField(max_length=60, null=True)
    stcodifica = models.CharField(max_length=60, null=True)
    codificado = models.CharField(max_length=60, null=True)
    versaosist = models.CharField(max_length=60, null=True)
    versaoscb = models.CharField(max_length=60, null=True)
    fonteinv = models.CharField(max_length=60, null=True)
    dtrecebim = models.CharField(max_length=60, null=True)
    atestado = models.CharField(max_length=60, null=True)
    dtrecoriga = models.CharField(max_length=60, null=True)
    causamat = models.CharField(max_length=60, null=True)
    escmaeagr1 = models.CharField(max_length=60, null=True)
    escfalagr1 = models.CharField(max_length=60, null=True)
    stdoepidem = models.CharField(max_length=60, null=True)
    stdonova = models.CharField(max_length=60, null=True)
    difdata = models.CharField(max_length=60, null=True)
    nudiasobco = models.CharField(max_length=60, null=True)
    nudiasobin = models.CharField(max_length=60, null=True)
    dtcadinv = models.CharField(max_length=60, null=True)
    tpobitocor = models.CharField(max_length=60, null=True)
    dtconinv = models.CharField(max_length=60, null=True)
    fontes = models.CharField(max_length=60, null=True)
    tpresginfo = models.CharField(max_length=60, null=True)
    tpnivelinv = models.CharField(max_length=60, null=True)
    nudiasinf = models.CharField(max_length=60, null=True)
    dtcadinf = models.CharField(max_length=60, null=True)
    morteparto = models.CharField(max_length=60, null=True)
    dtconcaso = models.CharField(max_length=60, null=True)
    fontesinf = models.CharField(max_length=60, null=True)
    altcausa = models.CharField(max_length=60, null=True)
    contador = models.CharField(max_length=60, null=True)
    ano = models.CharField(max_length=4, db_index=True)

    class Meta:
        db_table = 'doext_sim'