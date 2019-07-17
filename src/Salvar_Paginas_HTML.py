"""""
Script escrito por Dyego Silva de Oliveira
em maio de 2019 para o Trabalho de Conclusão do
curso de Bacharelado em Sistemas de Informação
pela Universidade Federal do Acre.

Este código pode ser utilizado, modificado e adaptado
de acordo com as necessidades que surgirem, desde que
seja para fins acadêmicos ou próprios, não podendo ser
comercializado.

"""

"""
Sobre o funcionamento: 

Este script é responsável pela extração do conteúdo HTML das páginas
de anúncios do site Empregos TI - Vagas em TI (https://empregos.profissionaisti.com.br?p=).

Existe um laço de repetição que vai da última página do site
até a primeira. (Usou-se essa técnica pois os anúncios mais antigos estão na
útilma página, assim como os mais recentes estão na primeira).

Notou-se que para avançar pelas páginas do site, basta concatenar o site principal
com o número da página desejada. Ex: Para acessar a página 66 do site, basta concatenar 
o site "https://empregos.profissionaisti.com.br?p=" com o número da página, logo, ficaria assim:
https://empregos.profissionaisti.com.br?p=66.

Depois de coletado o conteúdo HTML das páginas, os dados são exportados no caminho:
/.results/paginas_html do projeto

"""

#Importações
from src.utilis import get_project_root
from requests import get
from bs4 import BeautifulSoup

#lista para armazenar as páginas HTML

lista_paginas_html = []

#url inicial
url_main = "https://empregos.profissionaisti.com.br/?p="

#indices para as páginas do site -> Usar da última para a primeira página do site
pagina_inicial = 1
pagina_final = 228

#Laço de repetição responsável pelo controle dos acessos às páginas e pela extração dos conteúdos HTML
for indice in range(pagina_final,pagina_inicial,-1):

#Concatenação da url com o índice da página
    url_page = url_main+str(indice)

    print("\nPágina: ", indice, ": ", url_page, "\n")

#faz a requisição da url
    request_url = get(url_page)

#Captura o conteúdo html da url
    html_soup = BeautifulSoup(request_url.text, 'html.parser')

#Adiciona o conteúdo HTML da página à lista "lista_paginas_html"
    lista_paginas_html.append(html_soup)

print("Quantidade de páginas na lista: ",len(lista_paginas_html))

#indice da última pagina HTML
indice_pagina = pagina_final

#Caminho do projeto
root = get_project_root()

#Exporta o contéudo HTML das páginas
#São criados arquivos txt na pasta \.results\paginas_html do projeto
for o in lista_paginas_html:
    filename = (str(root)) +"\\.results\\paginas_html\\paginas_html_" + str(indice_pagina) + ".txt"
    with open(filename, 'a') as f:
        f.write(str(o))
    indice_pagina = indice_pagina - 1
f.close()