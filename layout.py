import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc



layout = html.Div([
    dbc.Navbar(
        dcc.Dropdown(
            id = 'dep_dropdown',
            style = {'width': 300}
        )
    ),
    dbc.Container([
        dbc.Row([
            dbc.Col([
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
                        html.Div(id='dep_partido'),
                        html.Div(id='dep_uf')
                    ],
                        style = {'margin': 20}
                    )
                ])
            ],
                className = 'col_layout shadow',
                width = 5
            ),
            dbc.Col(
                html.Div(
                    'Coluna 2',
                    className = 'col_layout shadow'
                )
            )
        ])
    ],
        style = {'margin-top': 40}
    )
])