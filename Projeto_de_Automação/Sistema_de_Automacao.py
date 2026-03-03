#Passo 1: Abrir o Navegador
#Passo 2: Acessar o Site
#Passo 3: Fazer Login

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

Link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"


#acessar o navegador
pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("enter")
#

#entrar no sistema da empresa
pyautogui.write(Link)
pyautogui.press("enter")
pyautogui.click(x=726, y=448)
pyautogui.write("Caioaa2500@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhaincribel")
pyautogui.press("tab")
pyautogui.press("enter")
#

#Preencher o formulario

# Importando a tabela, para a variavel "Tabela".
Tabela = pd.read_csv("Projeto_de_Automação/produtos.csv")

# categorizando a tabela com index, para que ele busque as informaçoes da tabela linha por linha.
# colocando essa informação na variavel "Linha".

for Linha in Tabela.index:

    time.sleep(3)

    pyautogui.click(x= 719, y=309)

    #com a variavel "Tabela" e "Linha" ja feitas, agora queremos localizar cada item separadamente.
    # criamos a variavel com o mesmo nome da coluna do produto "codigo".
    # informamos para ele .loc "localizar" a variavel "Linha" na coluna "codigo" da Tabela.
    codigo = Tabela.loc [Linha, "codigo"]

    #note que eu atribui um valor "str" dentro da variavel, pois quero que ele transforme os numeros de valor "inteiro" para "string".
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #Marca
    #faremos o mesmo procedimento anterior com a coluna "Marca" desta vez.
    marca = Tabela.loc [Linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #Tipo
    #faremos o mesmo procedimento anterior.
    tipo = Tabela.loc [Linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #Categoria
    #faremos o mesmo procedimento anterior
    categoria = Tabela.loc [Linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #Preco
    #faremos o mesmo procedimento
    preco = Tabela.loc [Linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    #Custo
    custo = Tabela.loc [Linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #Observacao

    
    obs = Tabela.loc [Linha, "obs"]
    if pd.notna(obs):
        pyautogui.write(str(obs))
    
    pyautogui.press("tab")

    #cadastrar
    pyautogui.press("enter")
    pyautogui.scroll(5000)
