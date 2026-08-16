import banco as bd

idioma_select = bd.status_idioma_page(option = 0)

palavras = {
    'BR': {
        'titulos': {
            'idioma': 'Idioma',
            'inicio': 'Início',
            'agenda': 'Agenda',
            'historico': 'Histórico',
            'outros': 'Outros',
            'configuracao': 'Configuração',
            'notificacao': 'Notificação',
        },

        'navegacao': {
            'inicio': 'Início',
            'agenda': 'Agenda',
            'historico': 'Histórico',
            'outros': 'Outros'
        },

        'home': {
            'retirada': 'Retirada',
            'fiados': 'Fiados',
            'agendar': 'Agendar',
            'clientes_agendados': 'Clientes agendados'
        },

        'atendimento': {
            'busca_rapida': 'Busca rápida',
            'todos': 'Todos',
            'sem_resultados': 'Sem resultados\npara essa busca'
        },

        'registros': {
            'sem_informacoes': 'Sem informações...'
        },

        'configuracao': {
            'empresa': 'Empresa',
            'info_empresa': 'Informações da empresa',
            'administracao': 'Administração',
            'controle_acessos': 'Controle de acessos e senhas',

            'tema_escuro': 'Tema escuro',
            'alternar_tema': 'Alternar tema escuro/claro',

            'idioma': 'Idioma',
            'alterar_idioma': 'Alterar idioma do aplicativo'
        },

        'dialog_atendimento': {
            'titulo_atendimento': 'Atendimento',
            'titulo_conclusao': 'Conclusão',
            'nome_cliente_hint': 'Nome do cliente..',
            'cliente_padrao': 'Cliente ##',
            'total': 'Total:',
            'troco': 'Troco:',
            'subtotal': 'Subtotal',
            'voltar': 'Voltar',
            'finalizar': 'Finalizar',
            'prosseguir': 'Prosseguir',
            'cartao_credito': 'Cartão de crédito',
            'recebido_em': 'Recebido em',
            'desconto': 'Desconto',
            'adicional': 'Adicional',
            'valor_porcentagem': 'Valor em porcentagem %',
            'unidade_abrev': 'Und',
            'pix': 'Pix',
            'cartao': 'Cartão',
            'dinheiro': 'Dinheiro'
        },

        'notificacoes': {
            'selecione_itens_titulo': 'Atenção!\n',
            'selecione_itens_msg': 'Selecione pelo menos um serviço para continuar.',
            'valor_invalido_titulo': 'Ops..!\n',
            'valor_invalido_msg': 'Valor inválido, digite apenas números.',
            'selecione_pagamento_titulo': 'Atenção!\n',
            'selecione_pagamento_msg': 'Escolha uma forma de pagamento para continuar.',
            'venda_sucesso_titulo': 'Sucesso!\n',
            'venda_sucesso_msg': 'Venda registrada e salva no histórico.',
            'saldo_insuficiente_titulo': 'Saldo insuficiente!\n',
            'saldo_insuficiente_msg': 'O valor recebido é menor que o total da venda.',
            'valor_inserido_invalido_titulo': 'Ops..!\n',
            'valor_inserido_invalido_msg': 'Não foi possível processar o valor informado.'
        },

        'idioma': {
            'nome_idioma': {
                'portugues': 'Português - BR',
                'ingles': 'Inglês - EUA',
                'espanhol': 'Espanhol - ES',
                'frances': 'Francês - FR'
            },

            'exemplo': 'Olá, tudo bom?\nEste é um exemplo de escrita no idioma escolhido.\n\n(Português - BR)'
        }
    },

    'EUA': {
        'titulos': {
            'idioma': 'Language',
            'inicio': 'Home',
            'agenda': 'Schedule',
            'historico': 'History',
            'outros': 'More',
            'configuracao': 'Settings',
            'notificacao': 'Notification',
        },

        'navegacao': {
            'inicio': 'Home',
            'agenda': 'Schedule',
            'historico': 'History',
            'outros': 'More'
        },

        'home': {
            'retirada': 'Withdrawal',
            'fiados': 'Credit',
            'agendar': 'Schedule',
            'clientes_agendados': 'Scheduled clients'
        },

        'atendimento': {
            'busca_rapida': 'Quick search',
            'todos': 'All',
            'sem_resultados': 'No results\nfor this search'
        },

        'registros': {
            'sem_informacoes': 'No information...'
        },

        'configuracao': {
            'empresa': 'Company',
            'info_empresa': 'Company information',
            'administracao': 'Administration',
            'controle_acessos': 'Access and passwords',

            'tema_escuro': 'Dark mode',
            'alternar_tema': 'Toggle dark/light mode',

            'idioma': 'Language',
            'alterar_idioma': 'Change app language'
        },

        'dialog_atendimento': {
            'titulo_atendimento': 'Service',
            'titulo_conclusao': 'Checkout',
            'nome_cliente_hint': 'Client name..',
            'cliente_padrao': 'Client ##',
            'total': 'Total:',
            'troco': 'Change:',
            'subtotal': 'Subtotal',
            'voltar': 'Back',
            'finalizar': 'Finish',
            'prosseguir': 'Continue',
            'cartao_credito': 'Credit card',
            'recebido_em': 'Received in',
            'desconto': 'Discount',
            'adicional': 'Extra',
            'valor_porcentagem': 'Percentage value %',
            'unidade_abrev': 'Unit',
            'pix': 'Pix',
            'cartao': 'Card',
            'dinheiro': 'Cash'
        },

        'notificacoes': {
            'selecione_itens_titulo': 'Attention!\n',
            'selecione_itens_msg': 'Select at least one service to continue.',
            'valor_invalido_titulo': 'Oops..!\n',
            'valor_invalido_msg': 'Invalid value, enter numbers only.',
            'selecione_pagamento_titulo': 'Attention!\n',
            'selecione_pagamento_msg': 'Choose a payment method to continue.',
            'venda_sucesso_titulo': 'Success!\n',
            'venda_sucesso_msg': 'Sale recorded and saved in the history.',
            'saldo_insuficiente_titulo': 'Insufficient balance!\n',
            'saldo_insuficiente_msg': 'The amount received is less than the total.',
            'valor_inserido_invalido_titulo': 'Oops..!\n',
            'valor_inserido_invalido_msg': 'Could not process the entered value.'
        },

        'idioma': {
            'nome_idioma': {
                'portugues': 'Portuguese - BR',
                'ingles': 'English - USA',
                'espanhol': 'Spanish - ES',
                'frances': 'French - FR'
            },

            'exemplo': 'Hello, how are you?\nThis is an example of text written in the selected language.\n\n(English - USA)'
        }
    },

    'ES': {
        'titulos': {
            'idioma': 'Idioma',
            'inicio': 'Inicio',
            'agenda': 'Agenda',
            'historico': 'Historial',
            'outros': 'Más',
            'configuracao': 'Configuración',
            'notificacao': 'Notificación',
        },

        'navegacao': {
            'inicio': 'Inicio',
            'agenda': 'Agenda',
            'historico': 'Historial',
            'outros': 'Más'
        },

        'home': {
            'retirada': 'Retirada',
            'fiados': 'Fiados',
            'agendar': 'Agendar',
            'clientes_agendados': 'Clientes agendados'
        },

        'atendimento': {
            'busca_rapida': 'Búsqueda rápida',
            'todos': 'Todos',
            'sem_resultados': 'Sin resultados\npara esta búsqueda'
        },

        'registros': {
            'sem_informacoes': 'Sin información...'
        },

        'configuracao': {
            'empresa': 'Empresa',
            'info_empresa': 'Información de la empresa',
            'administracao': 'Administración',
            'controle_acessos': 'Control de accesos y contraseñas',

            'tema_escuro': 'Modo oscuro',
            'alternar_tema': 'Alternar modo oscuro/claro',

            'idioma': 'Idioma',
            'alterar_idioma': 'Cambiar idioma de la aplicación'
        },

        'dialog_atendimento': {
            'titulo_atendimento': 'Atención',
            'titulo_conclusao': 'Conclusión',
            'nome_cliente_hint': 'Nombre del cliente..',
            'cliente_padrao': 'Cliente ##',
            'total': 'Total:',
            'troco': 'Cambio:',
            'subtotal': 'Subtotal',
            'voltar': 'Volver',
            'finalizar': 'Finalizar',
            'prosseguir': 'Continuar',
            'cartao_credito': 'Tarjeta de crédito',
            'recebido_em': 'Recibido en',
            'desconto': 'Descuento',
            'adicional': 'Adicional',
            'valor_porcentagem': 'Valor en porcentaje %',
            'unidade_abrev': 'Unid.',
            'pix': 'Pix',
            'cartao': 'Tarjeta',
            'dinheiro': 'Efectivo'
        },

        'notificacoes': {
            'selecione_itens_titulo': '¡Atención!\n',
            'selecione_itens_msg': 'Selecciona al menos un servicio para continuar.',
            'valor_invalido_titulo': '¡Ups..!\n',
            'valor_invalido_msg': 'Valor inválido, ingresa solo números.',
            'selecione_pagamento_titulo': '¡Atención!\n',
            'selecione_pagamento_msg': 'Elige una forma de pago para continuar.',
            'venda_sucesso_titulo': '¡Éxito!\n',
            'venda_sucesso_msg': 'Venta registrada y guardada en el historial.',
            'saldo_insuficiente_titulo': '¡Saldo insuficiente!\n',
            'saldo_insuficiente_msg': 'El valor recibido es menor que el total.',
            'valor_inserido_invalido_titulo': '¡Ups..!\n',
            'valor_inserido_invalido_msg': 'No se pudo procesar el valor ingresado.'
        },

        'idioma': {
            'nome_idioma': {
                'portugues': 'Portugués - BR',
                'ingles': 'Inglés - EUA',
                'espanhol': 'Español - ES',
                'frances': 'Francés - FR'
            },

            'exemplo': '¡Hola! ¿Cómo estás?\nEste es un ejemplo de texto escrito en el idioma seleccionado.\n\n(Español - ES)'
        }
    },

    'FR': {
        'titulos': {
            'idioma': 'Langue',
            'inicio': 'Accueil',
            'agenda': 'Agenda',
            'historico': 'Historique',
            'outros': 'Plus',
            'configuracao': 'Paramètres',
            'notificacao': 'Notification',
        },

        'navegacao': {
            'inicio': 'Accueil',
            'agenda': 'Agenda',
            'historico': 'Historique',
            'outros': 'Plus'
        },

        'home': {
            'retirada': 'Retrait',
            'fiados': 'Crédit',
            'agendar': 'Planifier',
            'clientes_agendados': 'Clients programmés'
        },

        'atendimento': {
            'busca_rapida': 'Recherche rapide',
            'todos': 'Tous',
            'sem_resultados': 'Aucun résultat\npour cette recherche'
        },

        'registros': {
            'sem_informacoes': 'Aucune information...'
        },

        'configuracao': {
            'empresa': 'Entreprise',
            'info_empresa': 'Informations sur l’entreprise',
            'administracao': 'Administration',
            'controle_acessos': 'Accès et mots de passe',

            'tema_escuro': 'Mode sombre',
            'alternar_tema': 'Basculer entre sombre et clair',

            'idioma': 'Langue',
            'alterar_idioma': 'Changer la langue de l’application'
        },

        'dialog_atendimento': {
            'titulo_atendimento': 'Service',
            'titulo_conclusao': 'Conclusion',
            'nome_cliente_hint': 'Nom du client..',
            'cliente_padrao': 'Client ##',
            'total': 'Total :',
            'troco': 'Monnaie :',
            'subtotal': 'Sous-total',
            'voltar': 'Retour',
            'finalizar': 'Terminer',
            'prosseguir': 'Continuer',
            'cartao_credito': 'Carte de crédit',
            'recebido_em': 'Reçu en',
            'desconto': 'Remise',
            'adicional': 'Supplément',
            'valor_porcentagem': 'Valeur en pourcentage %',
            'unidade_abrev': 'Unité',
            'pix': 'Pix',
            'cartao': 'Carte',
            'dinheiro': 'Espèces'
        },

        'notificacoes': {
            'selecione_itens_titulo': 'Attention !\n',
            'selecione_itens_msg': 'Sélectionnez au moins un service pour continuer.',
            'valor_invalido_titulo': 'Oups..!\n',
            'valor_invalido_msg': 'Valeur invalide, entrez uniquement des chiffres.',
            'selecione_pagamento_titulo': 'Attention !\n',
            'selecione_pagamento_msg': 'Choisissez un moyen de paiement pour continuer.',
            'venda_sucesso_titulo': 'Succès !\n',
            'venda_sucesso_msg': 'Vente enregistrée et sauvegardée dans l’historique.',
            'saldo_insuficiente_titulo': 'Solde insuffisant !\n',
            'saldo_insuficiente_msg': 'Le montant reçu est inférieur au total.',
            'valor_inserido_invalido_titulo': 'Oups..!\n',
            'valor_inserido_invalido_msg': 'Impossible de traiter la valeur saisie.'
        },

        'idioma': {
            'nome_idioma': {
                'portugues': 'Portugais - BR',
                'ingles': 'Anglais - USA',
                'espanhol': 'Espagnol - ES',
                'frances': 'Français - FR'
            },

            'exemplo': 'Bonjour, comment allez-vous ?\nCeci est un exemple de texte écrit dans la langue sélectionnée.\n\n(Français - FR)'
        }
    }
}