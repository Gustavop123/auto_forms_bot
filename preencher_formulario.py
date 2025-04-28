from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Inicia o navegador Chrome
driver = webdriver.Chrome()

# Link do seu formulário
url = 'https://docs.google.com/forms/d/e/1FAIpQLSfEtgs-nGmSLivAH9nXlAsnjY7N_iUpGSsUxfwX1rQ0CmINYw/viewform'

# Número de vezes que queremos preencher
num_repeticoes = 30

for i in range(1, num_repeticoes + 1):  # Começa no 1
    driver.get(url)
    time.sleep(2)  # Espera o formulário carregar

    # Captura todas as perguntas de múltipla escolha
    perguntas = driver.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"]')

    for pergunta in perguntas:
        # Para cada pergunta, pega as opções possíveis
        opcoes = pergunta.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')

        if opcoes:
            # Escolhe UMA opção aleatoriamente entre as disponíveis
            opcao_escolhida = random.choice(opcoes)
            opcao_escolhida.click()
            time.sleep(random.uniform(0.3, 0.8))  # Varia o tempo de clique para parecer humano

    # Depois de preencher tudo, clica no botão Enviar
    botao_enviar = driver.find_element(By.XPATH, '//span[contains(text(), "Enviar")]')
    botao_enviar.click()

    time.sleep(2)  # Aguarda antes de repetir

    # Mostra no console quantos formulários já foram enviados
    print(f'Formulário enviado: {i}/{num_repeticoes}')

print("Finalizado!")
driver.quit()