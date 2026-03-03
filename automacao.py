import pyautogui
import time

#Entra no sistema da empresa
#Abre o navegador
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" 

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

#Escreve o link da variável
pyautogui.write(link)
pyautogui.press("enter")
#Pausa o sistema para garantir que vai carregar o site
time.sleep(3)

#Faz Login
pyautogui.click(x=697, y=369)
pyautogui.write("testeemail@gmail.com")
pyautogui.press("tab")
pyautogui.write("teste1234")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)
    
#Abre a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

#Cadastra o produto
#Repete o processo
for linha in tabela.index: #Para cada linha dentro da tabela, repete este processo até o fim
    pyautogui.click(x=653, y=294)

    # pega a tabela com o valor do campo que quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preenche o campo e passa pro próximo
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    
    #scroll para o topo do site
    pyautogui.scroll(5000)
   
