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

#Importações
from src.Anuncio import *
import codecs
import json
from bs4 import BeautifulSoup
from requests import get
from src.utilis import get_project_root

#Método utilizado para gerar e exportar o arquivo JSON contendo os anúncios coletados
def escrever_json(dic,ini,fim):
    file_name = str(root)+"\\results\\anuncios_json\\anuncios_"+(str(ini))+"_"+str(fim+1)+".json"
    dic = json.dumps(dic, indent=4, sort_keys=False, ensure_ascii=False)
    with codecs.open(file_name, 'a', encoding='utf-8') as f:
        f.write(dic)
        f.close()

#listas necessárias
lista_content_html = []
lista_informacoes_extraidas = []

#Define o id do anúncio
#Mudar conforme necessidade
id_anuncio = 1

#Valores que servem para definir os limites inicial e final do laço de repetição
#Uma vez que o processo de scrapping não pode ser realizado de uma única vez, devido à sobrecarga
#da conexão à internet, a coleta foi realizada de forma segmentada.
num_pagina_inicial = 28 #228, 190, 152, 114, 95, 74, 60, 50, 44, 35, 32, 25, 19, 10
num_pagina_final = 27 #190, 152, 114, 095, 74, 60, 50, 44, 35, 32, 25, 19, 10, 0

#Informa a página do site onde o anúncio se encontra
pagina_anuncio = num_pagina_inicial

#Retorna o caminho do projeto Python
root = get_project_root()

#Laço de repetição responsável pela conversão (parsing) dos arquivos html em objetos do tipo árvore,
#que possam ser analisados afim de encontrar as informações desejadas
for t in range (num_pagina_inicial, num_pagina_final, -1):
    filename = str(root)+"\\results\\paginas_html\\paginas_html_"+str(t)+".txt"
    with open(filename,'r') as f:
        arquivo_txt_html = f.read()

    #O método BeautifulSoup recebe dois parâmetros: Um arquivo txt contendo a estrutura HTML
    #(Coletado por meio do script "Salvar_Paginas_HTML") e um objeto do tipo 'html.parser' responsável por informar
    #ao método que o primeiro parâmetro contém um conteúdo HTML
    html_soup_txt = BeautifulSoup(arquivo_txt_html, 'html.parser')

    #A lista "lista_content_html" recebe o objeto contendo a árvore formada a partir da estrutura HTML.
    lista_content_html.append(html_soup_txt)
    f.close()

#Laço para procurar e extrair as informações dos objetos produzidos no laço anterior
for pagina_html in lista_content_html:

    # div para a lista dos anúncios de empregos na página requisitada
    # Procura todos os elementos da tag 'div' correspondentes à classe 'job-list-content'
    list_jobs = pagina_html.find_all('div', class_='job-list-content')

    #Conta a ordem do anúncio na página (varia de acordo com a qunatidade de anúncios na página)
    cont_anuncio_pagina = 1

    # captura cada anúncio de emprego contido em list_jobs
    for anuncios in list_jobs:

        #pega as informações do elemento 'p' e os adiciona ao vetor 'informacoes'
        informacoes = anuncios.p.text.split()

        #Código do anúncio localiza-se na posição 4 do vetor
        codigo = informacoes[4]

        #responsável pelo anúncio localiza-se na posição 7 do vetor
        responsavel = informacoes[7]

        #pega o link do anúncio contido no elemento 'h4' -> 'a'
        link = anuncios.h4.a['href']

        #titulo do anuncio
        titulo = anuncios.h4.a.text

        #modalidade de emprego e dedicação
        modalidade_dedicacao = anuncios.find_all('span', class_='label')

#informações obtidas nos links dos anúncios (Necessita acessar cada anúncio da página):

        # envia uma requisição ao link do anúncio
        url_job = get(link)

        # Captura a página html da url
        html_soup_job = BeautifulSoup(url_job.text, 'html.parser')

        # div para as informações complementares do anúncio
        # Procura o primeiro elemnto da tag 'div' correspondente à classe 'job-icons clearfix'
        job_info = html_soup_job.find('div', class_='job-icons clearfix')

        # popula uma lista com as informacoes complementares
        list_informations = job_info.find_all('a')

        #nome da empresa
        empresa = "None"

        #nome da localização
        localizacao = "None"

        #area de atuação
        area_atuacao = "None"

        #data de publicação
        data_publicacao = "None"

        #Se o vetor list_informations possuir 4 objetos
        if(len(list_informations)==4):
            empresa = list_informations[0].text
            localizacao = list_informations[1].text
            area_atuacao = list_informations[2].text
            data_publicacao = list_informations[3].text

        # Se o vetor list_informations possuir 3 objetos (No caso do anúncio não possuir o nome da empresa)
        if(len(list_informations)==3):
            empresa = "None"
            localizacao = list_informations[0].text
            area_atuacao = list_informations[1].text
            data_publicacao = list_informations[2].text

        print("\nAnúncio: ", id_anuncio)
        print("\nAnúncio (página/ordem): ", pagina_anuncio, cont_anuncio_pagina)
        print("Código: ", codigo)

        #div para a descrição do anúncio de emprego da página
        #Procura o elemento da tag 'div' correspondente à classe 'job-content' (Esse é um elemento único)
        job_description = html_soup_job.find('div', class_='job-content')

        descricao = job_description.find_all('p')

        desc = ""
        for d in descricao:
            desc = desc + str(d.text)+" "

        #Instância da classe Anuncio
        jobs = Anuncio()

        #Insere as informações no objeto 'jobs'
        jobs.insere_anuncio(id_anuncio, pagina_anuncio, codigo, titulo, link, responsavel, modalidade_dedicacao[0].text, modalidade_dedicacao[1].text, empresa, localizacao, area_atuacao, data_publicacao, desc)

        #Adiciona o objeto jobs contendo as informações extraídas à lista "lista_informacoes_extraidas"
        lista_informacoes_extraidas.append(jobs)
        print("Anúncio inserido")

        id_anuncio = id_anuncio + 1
        cont_anuncio_pagina = cont_anuncio_pagina + 1

        #FIM DO FOR Anúncios

        url_job.close()
        #Informações sobre o status da conexão
        print(url_job.history)
        print(url_job.reason)
        print(url_job.request)
        print("Status conexão: ",url_job.status_code)
    pagina_anuncio = pagina_anuncio - 1

#vetor lista_dicionario contendo todas as informações extraídas
lista_dicionario = [
    dict(
        _id=anuncio.num_anuncio,
        pagina_anuncio=anuncio.pag_anuncio,
        codigo=anuncio.codigo,
        titulo=anuncio.titulo,
        link=anuncio.link,
        responsavel=anuncio.responsavel,
        modalidade=anuncio.modalidade,
        dedicacao=anuncio.dedicacao,
        empresa=anuncio.empresa,
        localizacao=anuncio.estado,
        area=anuncio.area_atuacao,
        data_publicacao=anuncio.data_publicacao,
        descricao=anuncio.descricao
    )
    for anuncio in lista_informacoes_extraidas
]

#dicionário pronto para ser exportado em um arquivo JSON
dicionario_salvar = {"":lista_dicionario}

#Método para exportar o arquivo JSON
escrever_json(dicionario_salvar, num_pagina_inicial, num_pagina_final)
