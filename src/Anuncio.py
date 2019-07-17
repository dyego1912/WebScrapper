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

#classe utilizada para abstrair as informações dos anúncios
class Anuncio():

    num_anuncio = ""
    pag_anuncio = ""
    codigo = ""
    titulo = ""
    link = ""
    responsavel = ""
    modalidade = ""
    dedicacao = ""
    empresa = ""
    localizacao = ""
    area_atuacao = ""
    data_publicacao = ""
    descricao = ""

#Método utilizado para definir os atributos da classe
    def insere_anuncio(self, num_anuncio, pag_anuncio, codigo, titulo, link, responsavel, modalidade, dedicacao, empresa, localizacao, area_atuacao, data_publicacao, descricao):
        self.num_anuncio = num_anuncio
        self.pag_anuncio = pag_anuncio
        self.codigo = codigo
        self.titulo = titulo
        self.link = link
        self.responsavel = responsavel
        self.modalidade = modalidade
        self.dedicacao = dedicacao
        self.empresa = empresa
        self.localizacao = localizacao
        self.area_atuacao = area_atuacao
        self.data_publicacao = data_publicacao
        self.descricao = descricao