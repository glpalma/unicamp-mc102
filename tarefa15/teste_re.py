import re
from modulo import *

def main():
	#site_html = """<a href="https://ic.unicamp.br/graduacao/engenharia-da-computacao/">
	#Engenharia da Computação
	#</a>
	#href="https://www.youtube.com/channel/UC81VD6eeuLLSfyY_D-N8sVw" """
	#regex = r'\bhref="(.+)"'
	#html = obter_html("https://ic.unicamp.br/~lehilton/mc102qr/index.html") #acha a pasta em que o site está
	#lista_urls = re.findall(regex, html)
	#for link in lista_urls:
	#	print(link)
	
	url_valida = eh_url_valida('https://ic.unicamp.br/~lehilton/mc102qr/tarefas/14-recursao.html', "https://ic.unicamp.br/~lehilton/mc102qr/unidades/11-recursao.html")
	print(url_valida)

main()