from DadosAbertosBrasil import camara

from datetime import datetime

import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import layout, utils



MONTSERRAT = {
    'href': 'https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap',
    'rel': 'stylesheet'
}


app = dash.Dash(
    name = __name__,
    external_stylesheets = [dbc.themes.BOOTSTRAP, MONTSERRAT]
)

app.layout = layout.layout
app.title = 'Painel de Deputados'



def get_logo(cod:int) -> str:
    p = camara.Partido(cod)
    return p.logo

PARTIDOS = camara.lista_partidos(legislatura=56, itens=50)
PARTIDOS['logo'] = PARTIDOS.id.apply(get_logo)



# Carregar opções do dropdown
@app.callback(
    Output('dep_dropdown', 'options'),
    [Input('leg_input', 'value'),
    Input('uf_dropdown', 'value')])
def update_dropdown_options(leg, uf):
    DEPUTADOS = camara.lista_deputados(
        legislatura = leg,
        uf = uf
    )
    return [{'label': row.nome, 'value': row.id} \
        for _, row in DEPUTADOS.iterrows()]



# Carregar informações de um deputado
@app.callback(
    [Output('dep_foto', 'src'),
    Output('dep_nome', 'children'),
    Output('dep_email', 'children'),
    Output('dep_telefone', 'children'),
    Output('dep_nascimento', 'children'),
    Output('dep_uf', 'children'),
    Output('uf_bandeira', 'src'),
    Output('dep_partido', 'children'),
    Output('partido_logo', 'src'),
    Output('pizza', 'figure')],
    [Input('dep_dropdown', 'value')],
    prevent_initial_call = True)
def update_deputado(cod):
    dep = camara.Deputado(cod)
    partido = PARTIDOS.index[PARTIDOS.sigla==dep.partido][0]

    nascimento = datetime.strftime(
        datetime.strptime(dep.nascimento, '%Y-%m-%d'),
        format = '%d/%m/%Y'
    )

    return (
        dep.foto,
        dep.nome_eleitoral,
        dep.email,
        dep.gabinete['telefone'],
        nascimento,
        utils.UFS[dep.uf],
        utils.bandeira(dep.uf, tamanho=50),
        PARTIDOS.loc[partido, 'nome'],
        PARTIDOS.loc[partido, 'logo'],
        utils.pizza(dep, ano=2021)
    )



if __name__ == '__main__':
    app.run_server(
        host = '0.0.0.0',
        port = 1000
    )