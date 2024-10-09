import requests 
import re
from bs4 import BeautifulSoup


def pegaDadosNome(nome):
    pagina = requests.get(f"https://www.dicionariodenomesproprios.com.br/{nome}/")
    content = BeautifulSoup(pagina.content, "lxml") # pega o HTML da página
    
    if content.h1.text == "Página Não Encontrada":
        return None
    
    else:
        rawSignificados = content.p.text # le o elemento <p> onde estão os significados do nome 
        significadosNome = re.findall(r'“([^“”]*)”', rawSignificados) + re.findall(r'"([^""]*)"', rawSignificados)  # le e coloca em lista todos os significados do nome

        rawOrigens = content.find("p", id="origem").children # le o elemento <p> de id "origem"
        origensNome = [e.text for e in rawOrigens if e.name == "a"] # le e coloca lista de origens do nome
        
        data = {
            "significados": significadosNome,
            "origens": origensNome
        }

        return data
