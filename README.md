# Google Forms Auto-Filler Bot

---

## Sobre o Projeto

O **Google Forms Auto-Filler Bot** é um script desenvolvido em **Python** utilizando a biblioteca **Selenium**, com o objetivo de automatizar o preenchimento e envio de formulários do Google Forms.
O bot simula o comportamento humano clicando em opções de múltipla escolha de maneira aleatória e enviando o formulário repetidamente, conforme configuração.

---

## Funcionalidades

- Preenchimento automático de formulários.
- Escolha aleatória das opções em perguntas de múltipla escolha.
- Simulação de cliques humanos (pausas aleatórias).
- Envio automático do formulário.
- Contador exibindo o número de formulários enviados no terminal.
- Configuração do número de repetições diretamente no código.

---

## Tecnologias Utilizadas

- Python 3.x
- Selenium
- Google Chrome
- ChromeDriver

---

## Instalação

### 1. Instalar o Python

- Acesse [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Baixe e instale a versão mais recente do Python.
- Durante a instalação, marque a opção **"Add Python to PATH"**.

### 2. Instalar a Biblioteca Selenium

Após instalar o Python, abra o terminal e execute:

```bash
pip install selenium
```

### 3. Instalar o Google Chrome

Se ainda não tiver o navegador Google Chrome, baixe em:  
[https://www.google.com/chrome/](https://www.google.com/chrome/)

### 4. Baixar o ChromeDriver

- Verifique a versão do seu navegador Google Chrome acessando `chrome://settings/help`.
- Baixe o ChromeDriver correspondente em: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
- Extraia o arquivo `chromedriver.exe`.
- Coloque o `chromedriver.exe` na mesma pasta onde estará o script `preenche_formulario.py`.

---

## Como Usar

### 1. Configurar o Script

Abra o arquivo `preenche_formulario.py` e atualize a variável `url` com o link do seu Google Formulário:

```python
url = 'https://docs.google.com/forms/d/e/SEU-LINK-AQUI/viewform'
```

Substitua `SEU-LINK-AQUI` pelo ID real do seu formulário.

### 2. Executar o Script

No terminal, navegue até a pasta onde o projeto está e execute:

```bash
python preenche_formulario.py
```

O terminal mostrará o progresso do envio dos formulários, como por exemplo:

```
Formulário enviado: 1/30
Formulário enviado: 2/30
Formulário enviado: 3/30
...
Formulário enviado: 30/30
Finalizado!
```

---

## Demonstração

<p align="center">
  <img src="https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPOSITORIO/main/assets/preenchendo.gif" alt="Demonstração do Bot preenchendo formulário" width="600">
</p>

---

## Melhorias Futuras

- Executar o bot em modo "headless" (sem abrir a janela do navegador).
- Implementar suporte a perguntas de texto, checkbox e listas suspensas.
- Exportar o histórico de respostas enviadas em um arquivo `.csv`.
- Configurar o número de repetições diretamente pelo terminal.

---

## Estrutura do Projeto

```
Google-Forms-AutoFiller-Bot/
├── assets/
│   └── preenchendo.gif
├── preenche_formulario.py
└── README.md
```

---

## Licença

Distribuído sob a licença MIT.
Consulte o arquivo LICENSE para mais informações.

---

## Autor

Feito com dedicação por [Gustavo, Costa](https://github.com/Gustavop123).
