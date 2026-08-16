import banco as bd

margin_left = 16
margin_right = 16
margin_top = 16

servicos_carregados = {}

async def carregar_dados():
    conexao = await bd.servico_valor()

    for servico in conexao:
        setor = servico[0]
        produto = servico[1]
        valor = servico[2]

        if setor not in servicos_carregados:
            servicos_carregados[setor] = {}

        if 'todos' not in servicos_carregados:
            servicos_carregados['todos'] = {}

        servicos_carregados[setor][produto] = {'setor': setor, 'produto': produto, 'valor': valor}
        servicos_carregados['todos'][produto] = {'setor': setor, 'produto': produto, 'valor': valor}

pagina_main = None
pagina_home = None
pagina_idioma = None
pagina_configuracao_main = None
pagina_agenda = None
cor_btns_navegation_bar = None

ativar_teclado_virtual = None
desativar_teclado_virtual = None