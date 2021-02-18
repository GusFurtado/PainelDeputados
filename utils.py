def bandeira(uf:str, tamanho:int=100) -> str:
    '''
    Gera a URL da WikiMedia para a bandeira de um estado de um tamanho
    escolhido.

    Parâmetros
    ----------
    uf: str
        Sigla da Unidade Federativa.
    tamanho: int (default=100)
        Tamanho em pixels da bandeira.

    Retorna
    -------
    str
        URL da bandeira do estado no formato PNG.

    --------------------------------------------------------------------------
    '''
    
    URL = r'https://upload.wikimedia.org/wikipedia/commons/thumb/'
    
    bandeira = {
        'AC': f'4/4c/Bandeira_do_Acre.svg/{tamanho}px-Bandeira_do_Acre.svg.png',
        'AM': f'6/6b/Bandeira_do_Amazonas.svg/{tamanho}px-Bandeira_do_Amazonas.svg.png',
        'AL': f'8/88/Bandeira_de_Alagoas.svg/{tamanho}px-Bandeira_de_Alagoas.svg.png',
        'AP': f'0/0c/Bandeira_do_Amap%C3%A1.svg/{tamanho}px-Bandeira_do_Amap%C3%A1.svg.png',
        'BA': f'2/28/Bandeira_da_Bahia.svg/{tamanho}px-Bandeira_da_Bahia.svg.png',
        'CE': f'2/2e/Bandeira_do_Cear%C3%A1.svg/{tamanho}px-Bandeira_do_Cear%C3%A1.svg.png',
        'DF': f'3/3c/Bandeira_do_Distrito_Federal_%28Brasil%29.svg/{tamanho}px-Bandeira_do_Distrito_Federal_%28Brasil%29.svg.png',
        'ES': f'4/43/Bandeira_do_Esp%C3%ADrito_Santo.svg/{tamanho}px-Bandeira_do_Esp%C3%ADrito_Santo.svg.png',
        'GO': f'b/be/Flag_of_Goi%C3%A1s.svg/{tamanho}px-Flag_of_Goi%C3%A1s.svg.png',
        'MA': f'4/45/Bandeira_do_Maranh%C3%A3o.svg/{tamanho}px-Bandeira_do_Maranh%C3%A3o.svg.png',
        'MG': f'f/f4/Bandeira_de_Minas_Gerais.svg/{tamanho}px-Bandeira_de_Minas_Gerais.svg.png',
        'MT': f'0/0b/Bandeira_de_Mato_Grosso.svg/{tamanho}px-Bandeira_de_Mato_Grosso.svg.png',
        'MS': f'6/64/Bandeira_de_Mato_Grosso_do_Sul.svg/{tamanho}px-Bandeira_de_Mato_Grosso_do_Sul.svg.png',
        'PA': f'0/02/Bandeira_do_Par%C3%A1.svg/{tamanho}px-Bandeira_do_Par%C3%A1.svg.png',
        'PB': f'b/bb/Bandeira_da_Para%C3%ADba.svg/{tamanho}px-Bandeira_da_Para%C3%ADba.svg.png',
        'PE': f'5/59/Bandeira_de_Pernambuco.svg/{tamanho}px-Bandeira_de_Pernambuco.svg.png',
        'PI': f'3/33/Bandeira_do_Piau%C3%AD.svg/{tamanho}px-Bandeira_do_Piau%C3%AD.svg.png',
        'PR': f'9/93/Bandeira_do_Paran%C3%A1.svg/{tamanho}px-Bandeira_do_Paran%C3%A1.svg.png',
        'RJ': f'7/73/Bandeira_do_estado_do_Rio_de_Janeiro.svg/{tamanho}px-Bandeira_do_estado_do_Rio_de_Janeiro.svg.png',
        'RO': f'f/fa/Bandeira_de_Rond%C3%B4nia.svg/{tamanho}px-Bandeira_de_Rond%C3%B4nia.svg.png',
        'RN': f'3/30/Bandeira_do_Rio_Grande_do_Norte.svg/{tamanho}px-Bandeira_do_Rio_Grande_do_Norte.svg.png',        
        'RR': f'9/98/Bandeira_de_Roraima.svg/{tamanho}px-Bandeira_de_Roraima.svg.png',
        'RS': f'6/63/Bandeira_do_Rio_Grande_do_Sul.svg/{tamanho}px-Bandeira_do_Rio_Grande_do_Sul.svg.png',
        'SC': f'1/1a/Bandeira_de_Santa_Catarina.svg/{tamanho}px-Bandeira_de_Santa_Catarina.svg.png',
        'SE': f'b/be/Bandeira_de_Sergipe.svg/{tamanho}px-Bandeira_de_Sergipe.svg.png',
        'SP': f'2/2b/Bandeira_do_estado_de_S%C3%A3o_Paulo.svg/{tamanho}px-Bandeira_do_estado_de_S%C3%A3o_Paulo.svg.png',
        'TO': f'f/ff/Bandeira_do_Tocantins.svg/{tamanho}px-Bandeira_do_Tocantins.svg.png',        
    }
    
    return URL + bandeira[uf]


UFS = {
    'AC': 'Acre',
    'AM': 'Amazonas',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espirito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MG': 'Minas Gerais',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'PR': 'Paraná',
    'RJ': 'Rio de Janeiro',
    'RO': 'Rondônia',
    'RN': 'Rio Grande do Norte',        
    'RR': 'Roraima',
    'RS': 'Rio Grande do Sul',
    'SC': 'Santa Catarina',
    'SE': 'Sergipe',
    'SP': 'São Paulo',
    'TO': 'Tocantins'
}