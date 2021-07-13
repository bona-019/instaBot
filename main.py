from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import os

clear = lambda: os.system('cls')
# Lê o arquivo login.txt e transforma cada linha de texto
# em elementos de uma lista pw, onde o 1º elemento é o nome
# de usuário e o 2º elemento é a senha, adicionando às variáveis
# username e password, respectivamente.
f = open(r"C:\..\login.txt", 'r', encoding='utf8')
pw = f.readlines()
username = pw[0]
password = pw[1]

clear()
print("Abrindo o navegador ...")
driver = webdriver.Firefox(executable_path=r"C:\..\geckodriver-v0.29.0-win64\geckodriver.exe")
driver.maximize_window()
clear()
print("Fazendo login ...")
driver.get('https://instagram.com')
sleep(3)
# Localizando, clicando e inserindo a variável username
# na caixa de texto onde deve ser inserido o nome de usuário.
usuario = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
usuario.click()
usuario.send_keys(username)
# Localizando, clicando e inserindo a variável password
# na caixa de texto onde deve ser inserida a senha.
senha = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
senha.click()
senha.send_keys(password)
# Pressionando a tecla enter na caixa de texto da senha.
senha.send_keys(Keys.RETURN)
clear()
print("Login realizado!")
sleep(5)
f.close()
clear()
print("Abrindo publicação ...")
# Entrando na publicação do sorteio.
driver.get('https://www.instagram.com/p/link_do_sorteio)

# Criando um for loop que fará 1000 comentários na publicação.
for i in range(1,1000):
    clear()
    print("Postando um comentário ...")
    # Criando a lista words com todas as palavras no arquivo palavras.txt
    f = open(r"C:\..\palavras.txt", 'r', encoding="utf8")
    words = f.readlines()
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").click()
    sleep(5)
    cx = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
    cx.click()
    sleep(2)
    # Inserindo na caixa de texto uma seleção aleatória da lista words.
    cx.send_keys(random.choice(words))
    clear()
    print("Enviando comentário ...")
    sleep(2)
    cx.send_keys(Keys.RETURN)
    clear()
    print("Comentário enviado!")
    clear()
    # É setado um tempo de espera entre cada comentário de 1 minuto e 20 segundos.
    # No final de cada comentário mostra o total de comentários enviados.
    print("Esperando 1min20s ...")
    print("Total de comentários enviados: %d" % (i))
    sleep(20)
    sleep(20)
    sleep(20)
    sleep(20)
