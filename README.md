# instaBot
Projeto desenvolvido sozinho em aproximadamente 3 meses,
entre o início de março de 2021 e final de maio de 2021.
Atualmente funciona bem como um projeto pessoal,
sem possibilidade de escalonamento.

# O que o projeto faz?
Bot de comentários automáticos em publicações no Instagram
utilizando a biblioteca Selenium na linguagem Python.
Usado principalmente em publicações de sorteios, comentando 
uma média de 500 comentários por dia em cada conta utilizada
pelo bot.

# Como o projeto funciona?
Com o navegador Firefox o projeto faz uso do Geckodriver,
utilizado para abrir sites em testes automatizados do Selenium.
Com o Geckodriver é possível abrir qualquer página web e simular
comandos reais como clique, inserção de teclas e rolar a página,
tudo isso referenciando elementos contidos na página (XPATH, CSS selectors,
class name, ID, link text).

# Arquivos do projeto
Além do main.py o projeto conta com o arquivo palavras.txt, que contém uma lista de palavras
do dicionário da língua portuguesa, ou seja, o bot comenta palavras aleatórias
do dicionário. Também possui o arquivo login.txt, que contém informações
de login de contas do Instagram. 
