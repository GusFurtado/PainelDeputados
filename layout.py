import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc



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
        ],
            style = {'margin': 20}
        )
    ],
        no_gutters = True
    ),

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
    width = 5
)



column2 = dbc.Col(
    html.Div(
        'Coluna 2',
        className = 'col_layout shadow'
    )
)



layout = html.Div([
    dbc.Navbar(
        dcc.Dropdown(
            id = 'dep_dropdown',
            style = {'width': 300}
        )
    ),
    dbc.Container([
        dbc.Row([
            column1,
            column2
        ])
    ],
        style = {'margin-top': 40}
    )
])