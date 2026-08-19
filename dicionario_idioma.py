import banco as bd

idioma_select = bd.status_idioma_page(option=0)

palavras = {
    'BR': {
        'titulos': {
            'idioma': 'Idioma',
            'inicio': 'Início',
            'agenda': 'Agenda',
            'outros': 'Outros',
            'pagamento': 'Pagamento',
            'conclusao': 'Conclusão',
            'historico': 'Histórico',
            'valor_invalido': 'Ops..!\n',
            'notificacao': 'Notificação',
            'atendimento': 'Atendimento',
            'venda_sucesso': 'Sucesso!\n',
            'configuracao': 'Configuração',
            'selecione_itens': 'Atenção!\n',
            'selecione_pagamento': 'Atenção!\n',
            'valor_inserido_invalido': 'Ops..!\n',
            'saldo_insuficiente': 'Saldo insuficiente!\n',
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
            'sem_resultados': 'Sem resultados\npara essa busca',
            'nome_cliente': 'Nome do cliente..',
            'cliente_padrao': 'Cliente ##',
            'total': 'Total:',
            'troco': 'Troco:',
            'subtotal': 'Subtotal',
            'voltar': 'Voltar',
            'finalizar': 'Finalizar',
            'prosseguir': 'Prosseguir',
            'cartao_credito': 'Cartão de crédito',
            'recebido': 'Recebido em',
            'desconto': 'Desconto',
            'adicional': 'Adicional',
            'porcentagem': 'Valor em porcentagem %',
            'unidade': 'Unidade',
            'digital': 'Digital',
            'cartao': 'Cartão',
            'dinheiro': 'Dinheiro',
            'outros': 'Outros',
            'salvar': 'Salvar',
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

        'notificacoes': {
            'selecione_itens': 'Selecione pelo menos um serviço para continuar.',
            'valor_invalido': 'Valor inválido, digite apenas números.',
            'selecione_pagamento': 'Escolha uma forma de pagamento para continuar.',
            'venda_sucesso': 'Venda registrada e salva no histórico.',
            'saldo_insuficiente': 'O valor recebido é menor que o total da venda.',
            'valor_inserido_invalido': 'Não foi possível processar o valor informado.'
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
            'outros': 'More',
            'pagamento': 'Payment',
            'conclusao': 'Checkout',
            'historico': 'History',
            'valor_invalido': 'Oops..!\n',
            'notificacao': 'Notification',
            'atendimento': 'Service',
            'venda_sucesso': 'Success!\n',
            'configuracao': 'Settings',
            'selecione_itens': 'Attention!\n',
            'selecione_pagamento': 'Attention!\n',
            'valor_inserido_invalido': 'Oops..!\n',
            'saldo_insuficiente': 'Insufficient balance!\n'
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
            'sem_resultados': 'No results\nfor this search',
            'nome_cliente': 'Client name..',
            'cliente_padrao': 'Client ##',
            'total': 'Total:',
            'troco': 'Change:',
            'subtotal': 'Subtotal',
            'voltar': 'Back',
            'finalizar': 'Finish',
            'prosseguir': 'Continue',
            'cartao_credito': 'Credit card',
            'recebido': 'Received in',
            'desconto': 'Discount',
            'adicional': 'Extra',
            'porcentagem': 'Percentage value %',
            'unidade': 'Unit',
            'digital': 'Electronic',
            'cartao': 'Card',
            'dinheiro': 'Cash',
            'outros': 'Other',
            'salvar': 'Save'
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

        'notificacoes': {
            'selecione_itens': 'Select at least one service to continue.',
            'valor_invalido': 'Invalid value, enter numbers only.',
            'selecione_pagamento': 'Choose a payment method to continue.',
            'venda_sucesso': 'Sale recorded and saved in the history.',
            'saldo_insuficiente': 'The amount received is less than the total.',
            'valor_inserido_invalido': 'Could not process the entered value.'
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
            'outros': 'Más',
            'pagamento': 'Pago',
            'conclusao': 'Conclusión',
            'historico': 'Historial',
            'valor_invalido': '¡Ups..!\n',
            'notificacao': 'Notificación',
            'atendimento': 'Atención',
            'venda_sucesso': '¡Éxito!\n',
            'configuracao': 'Configuración',
            'selecione_itens': '¡Atención!\n',
            'selecione_pagamento': '¡Atención!\n',
            'valor_inserido_invalido': '¡Ups..!\n',
            'saldo_insuficiente': '¡Saldo insuficiente!\n'
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
            'sem_resultados': 'Sin resultados\npara esta búsqueda',
            'nome_cliente': 'Nombre del cliente..',
            'cliente_padrao': 'Cliente ##',
            'total': 'Total:',
            'troco': 'Cambio:',
            'subtotal': 'Subtotal',
            'voltar': 'Volver',
            'finalizar': 'Finalizar',
            'prosseguir': 'Continuar',
            'cartao_credito': 'Tarjeta de crédito',
            'recebido': 'Recibido en',
            'desconto': 'Descuento',
            'adicional': 'Adicional',
            'porcentagem': 'Valor en porcentaje',
            'unidade': 'Unidad',
            'digital': 'Digital',
            'cartao': 'Tarjeta',
            'dinheiro': 'Efectivo',
            'outros': 'Otros',
            'salvar': 'Guardar'
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

        'notificacoes': {
            'selecione_itens': 'Selecciona al menos un servicio para continuar.',
            'valor_invalido': 'Valor inválido, ingresa solo números.',
            'selecione_pagamento': 'Elige una forma de pago para continuar.',
            'venda_sucesso': 'Venta registrada y guardada en el historial.',
            'saldo_insuficiente': 'El valor recibido es menor que el total.',
            'valor_inserido_invalido': 'No se pudo procesar el valor ingresado.'
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
            'outros': 'Plus',
            'pagamento': 'Paiement',
            'conclusao': 'Conclusion',
            'historico': 'Historique',
            'valor_invalido': 'Oups..!\n',
            'notificacao': 'Notification',
            'atendimento': 'Service',
            'venda_sucesso': 'Succès !\n',
            'configuracao': 'Paramètres',
            'selecione_itens': 'Attention !\n',
            'selecione_pagamento': 'Attention !\n',
            'valor_inserido_invalido': 'Oups..!\n',
            'saldo_insuficiente': 'Solde insuffisant !\n'
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
            'sem_resultados': 'Aucun résultat\npour cette recherche',
            'nome_cliente': 'Nom du client..',
            'cliente_padrao': 'Client ##',
            'total': 'Total :',
            'troco': 'Monnaie :',
            'subtotal': 'Sous-total',
            'voltar': 'Retour',
            'finalizar': 'Terminer',
            'prosseguir': 'Continuer',
            'cartao_credito': 'Carte de crédit',
            'recebido': 'Reçu en',
            'desconto': 'Remise',
            'adicional': 'Supplément',
            'porcentagem': 'Valeur en pourcentage %',
            'unidade': 'Unité',
            'digital': 'Électronique',
            'cartao': 'Carte',
            'dinheiro': 'Espèces',
            'outros': 'Autres',
            'salvar': 'Enregistrer'
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

        'notificacoes': {
            'selecione_itens': 'Sélectionnez au moins un service pour continuer.',
            'valor_invalido': 'Valeur invalide, entrez uniquement des chiffres.',
            'selecione_pagamento': 'Choisissez un moyen de paiement pour continuer.',
            'venda_sucesso': 'Vente enregistrée et sauvegardée dans l’historique.',
            'saldo_insuficiente': 'Le montant reçu est inférieur au total.',
            'valor_inserido_invalido': 'Impossible de traiter la valeur saisie.'
        },

        'idioma': {
            'nome_idioma': {
                'portugues': 'Portugais - BR',
                'ingles': 'Anglais - EUA',
                'espanhol': 'Espagnol - ES',
                'frances': 'Français - FR'
            },
            'exemplo': 'Bonjour, comment allez-vous ?\nCeci est un exemple de texte écrit dans la langue sélectionnée.\n\n(Français - FR)'
        }
    }
}