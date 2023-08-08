from modulo import eh_url_valida, obter_html, resolver_url
import re

def coletar_urls(html):
    """Devolve uma lista de URLs presentes
    em uma string com formato HTML."""
    regex = r'href=[\'"]?([^\'" >]+)'

    lista_urls = re.findall(regex, html)

    return lista_urls

def mostrar_arvore(url_inicial, url_ramo, n_indentacoes, sites_mostrados):
    """Encontra e mostra as ramificações de uma URL fornecida."""
    tamanho_indentacao = 2 * ' '
    
    if url_ramo == '':
        url = url_inicial
    else:
        url = url_ramo

    html = obter_html(url)
    lista_urls = coletar_urls(html)
    print(n_indentacoes * tamanho_indentacao + url)
    sites_mostrados.add(url)

    for link in lista_urls:
        url_resolvida = resolver_url(link, url)
        if eh_url_valida(url_resolvida, url_inicial) and url_resolvida not in sites_mostrados:
            mostrar_arvore(url_inicial, url_resolvida, n_indentacoes + 1, sites_mostrados)

def main():
    url_inicial = input().strip()
    mostrar_arvore(url_inicial, '', 0, set())

main()