from DadosAbertosBrasil import camara
from dash_core_components.Dropdown import Dropdown

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc



UFS = camara.referencias('ufs', index=True)

column1 = dbc.Col([
    dbc.Row([
        dbc.Col(
            html.Img(
                id = 'dep_foto',
                className = 'shadow'
            ),
            width = 'auto'
        ),
        dbc.Col([
            html.Div(id='dep_nome'),

            # Email
            html.Div([
                html.Div('Email', className='dep_atributo_title'),
                html.Div(id='dep_email')
            ],
                className = 'dep_atributo'
            ),

            # Telefone
            html.Div([
                html.Div('Telefone', className='dep_atributo_title'),
                html.Div(id='dep_telefone'),
            ],
                className = 'dep_atributo'
            ),

            # Nascimento
            html.Div([
                html.Div('Nascimento', className='dep_atributo_title'),
                html.Div(id='dep_nascimento')
            ],
                className = 'dep_atributo'
            )

        ],
            width = 'auto'
        )
    ]),

    # Estado
    dbc.Row([
        dbc.Col(
            html.Img(
                id='uf_bandeira',
                className='shadow',
                style = {
                    'height': 'auto',
                    'width': '100%'
                }
            ),
            width = 3
        ),
        dbc.Col(
            html.Span(id='dep_uf')
        )
    ],
        style = {'padding': 10}
    ),

    # Partido
    dbc.Row([
        dbc.Col(
            html.Img(
                id = 'partido_logo',
                style = {
                    'height': 'auto',
                    'width': '100%'
                }
            ),
            width = 3
        ),
        dbc.Col(
            html.Span(id='dep_partido')
        )
    ],
        style = {'padding': 10}
    )
],
    className = 'col_layout shadow',
    style = {'margin-left': 10},
    width = 5
)



column2 = dbc.Col(
    html.Div(
        'Coluna 2',
        className = 'col_layout shadow'
    )
)



layout = html.Div([
    dbc.Navbar([
        dbc.Input(
            type = 'number',
            min = 1,
            max = 56,
            step = 1,
            value = 56,
            style = {'width': 70},
            className = 'mr-2'
        ),
        dcc.Dropdown(
            id = 'uf_dropdown',
            placeholder = 'UF',
            style = {'width': 270},
            options = [{
                'label': UFS.loc[i, 'nome'],
                'value': i
            } for i in UFS.index]
        ),
        dcc.Dropdown(
            id = 'dep_dropdown',
            placeholder = 'Selecione um deputado...',
            style = {'width': 300},
            clearable = False,
            className = 'ml-2'
        )
    ]),
    dbc.Container([
        dbc.Row([
            column1,
            column2
        ])
    ],
        className = 'dashboard',
        fluid = True
    )
])