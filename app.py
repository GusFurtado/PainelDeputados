from DadosAbertosBrasil import camara

import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import layout



app = dash.Dash(
    name = __name__,
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)

app.layout = layout.layout
app.title = 'Painel de Deputados'



# Carregar opções do dropdown
@app.callback(
    Output('dep_dropdown', 'options'),
    [Input('dep_dropdown', 'style')])
def update_dropdown_options(x):
    lista = camara.lista_deputados()
    return [{'label': row.nome, 'value': row.id} \
        for i, row in lista.iterrows()]



# Carregar informações de um deputado
@app.callback(
    [Output('dep_foto', 'src'),
    Output('dep_nome', 'children'),
    Output('dep_partido', 'children'),
    Output('dep_uf', 'children')],
    [Input('dep_dropdown', 'value')],
    prevent_initial_call = True)
def update_deputado(cod):
    dep = camara.Deputado(cod)
    return (
        dep.foto,
        dep.nome_eleitoral,
        dep.uf,
        dep.partido
    )



if __name__ == '__main__':
    app.run_server(
        host = '0.0.0.0',
        port = 1000
    )