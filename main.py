from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import os

clear = lambda: os.system('cls')
f = open(r"F:\Programação\Python\Bot Instagram\insta_login.txt", 'r', encoding='utf8')
pw = f.readlines()
username = pw[0]
password = pw[1]

clear()
print("Abrindo o navegador ...")
driver = webdriver.Firefox(executable_path=r"F:\Programação\Python\Bot Instagram\geckodriver-v0.29.0-win64\geckodriver.exe")
driver.maximize_window()
clear()
print("Fazendo login ...")
driver.get('https://instagram.com')
sleep(3)
usuario = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
usuario.click()
usuario.send_keys(username)
senha = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
senha.click()
senha.send_keys(password)
senha.send_keys(Keys.RETURN)
clear()
print("Login realizado!")
sleep(5)
f.close()
clear()
print("Abrindo publicação ...")
driver.get('https://www.instagram.com/p/CN3KOCWhXIW/')

for i in range(1,1000):
    clear()
    print("Postando um comentário ...")
    f = open(r"F:\Programação\Python\Bot Instagram\palavras.txt", 'r', encoding="utf8")
    words = f.readlines()
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").click()
    sleep(5)
    cx = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
    cx.click()
    sleep(2)
    cx.send_keys(random.choice(words))
    clear()
    print("Enviando comentário ...")
    sleep(2)
    cx.send_keys(Keys.RETURN)
    clear()
    print("Comentário enviado!")
    clear()
    print("Esperando 1min20s ...")
    print("Total de comentários enviados: %d" % (i))
    sleep(20)
    sleep(20)
    sleep(20)
    sleep(20)