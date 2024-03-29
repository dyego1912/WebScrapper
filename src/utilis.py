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

#Importação da biblioteca responsável pela captura do caminho do projeto
from pathlib import Path

def get_project_root() -> Path:
    """Retorna o caminho do projeto."""
    return Path(__file__).parent.parent