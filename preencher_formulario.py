
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Pergunta ao usuário o link do formulário e o número de repetições
url = input("Digite o link do Google Formulário: ")
num_repeticoes = int(input("Digite o número de vezes que deseja preencher o formulário: "))

# Inicia o navegador
driver = webdriver.Chrome()

for i in range(1, num_repeticoes + 1):
    driver.get(url)
    time.sleep(2)

    perguntas = driver.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"]')

    for pergunta in perguntas:
        opcoes = pergunta.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
        if opcoes:
            opcao = random.choice(opcoes)
            opcao.click()
            time.sleep(random.uniform(0.3, 0.8))

    botao_enviar = driver.find_element(By.XPATH, '//span[contains(text(), "Enviar")]')
    botao_enviar.click()

    time.sleep(2)

    print(f"Formulário enviado: {i}/{num_repeticoes}")

print("Finalizado!")
driver.quit()
