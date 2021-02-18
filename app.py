from DadosAbertosBrasil import camara

import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import layout, utils



app = dash.Dash(
    name = __name__,
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)

app.layout = layout.layout
app.title = 'Painel de Deputados'



def get_logo(cod:int) -> str:
    p = camara.Partido(cod)
    return p.logo

PARTIDOS = camara.lista_partidos(legislatura=56, itens=50)
PARTIDOS['logo'] = PARTIDOS.id.apply(get_logo)
DEPUTADOS = camara.lista_deputados()



# Carregar opções do dropdown
@app.callback(
    Output('dep_dropdown', 'options'),
    [Input('dep_dropdown', 'style')])
def update_dropdown_options(x):
    return [{'label': row.nome, 'value': row.id} \
        for i, row in DEPUTADOS.iterrows()]



# Carregar informações de um deputado
@app.callback(
    [Output('dep_foto', 'src'),
    Output('dep_nome', 'children'),
    Output('dep_uf', 'children'),
    Output('uf_bandeira', 'src'),
    Output('dep_partido', 'children'),
    Output('partido_logo', 'src')],
    [Input('dep_dropdown', 'value')],
    prevent_initial_call = True)
def update_deputado(cod):
    dep = camara.Deputado(cod)
    partido = PARTIDOS.index[PARTIDOS.sigla==dep.partido][0]
    
    return (
        dep.foto,
        dep.nome_eleitoral,
        utils.UFS[dep.uf],
        utils.bandeira(dep.uf),
        PARTIDOS.loc[partido, 'nome'],
        PARTIDOS.loc[partido, 'logo']
    )



if __name__ == '__main__':
    app.run_server(
        host = '0.0.0.0',
        port = 1000
    )