from DadosAbertosBrasil import camara
from dash_core_components.Dropdown import Dropdown

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

import utils



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
            html.Div(
                id = 'dep_nome',
                className = 'title'
            ),

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

    html.Hr(),

    # Estado
    dbc.Row([
        dbc.Col(
            html.Img(
                id = 'uf_bandeira',
                className = 'shadow',
                style = {'height': 50}
            ),
            width = 'auto'
        ),
        dbc.Col(
            html.Div([
                html.Div('Unidade Federativa', className='dep_atributo_title'),
                html.Div(id='dep_uf'),
            ],
                className = 'dep_atributo'
            )
        )
    ],
        style = {'padding': 10}
    ),

    # Partido
    dbc.Row([
        dbc.Col(
            html.Img(
                id = 'partido_logo',
                style = {'height': 50}
            ),
            width = 'auto'
        ),
        dbc.Col(
            html.Div([
                html.Div('Partido', className='dep_atributo_title'),
                html.Div(id='dep_partido'),
            ],
                className = 'dep_atributo'
            )
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
    html.Div([
        html.Div(
            'Despesas',
            className = 'title',
            style = {'text-align': 'center'}
        ),
        html.Div(
            dcc.Graph(id='plots')
        )
    ],
        className = 'col_layout shadow'
    )
)



navbar = dbc.Navbar([
    dbc.Input(
        type = 'number',
        min = 1,
        max = 56,
        step = 1,
        value = 56,
        style = {'width': 70},
        className = 'mr-2',
        id = 'leg_input'
    ),
    dcc.Dropdown(
        id = 'uf_dropdown',
        placeholder = 'Selecione uma UF...',
        style = {'width': 270},
        options = [{
            'label': utils.UFS[uf],
            'value': uf
        } for uf in utils.UFS]
    ),
    dcc.Dropdown(
        id = 'dep_dropdown',
        placeholder = 'Selecione um deputado...',
        style = {'width': 300},
        clearable = False,
        className = 'ml-2'
    )
])



layout = html.Div([
    navbar,
    dcc.Loading(
        dbc.Container([
            dbc.Row([
                column1,
                column2
            ])
        ],
            className = 'dashboard',
            fluid = True
        ),
        fullscreen = True
    )
])