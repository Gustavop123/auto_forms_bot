# Google Forms Auto-Filler Bot

---

## Sobre o Projeto

O **Google Forms Auto-Filler Bot** é um script desenvolvido em **Python** utilizando **Selenium**, que agora permite:
- Inserir o link do formulário diretamente pelo console.
- Definir o número de repetições diretamente pelo console.
- Gerar um arquivo executável `.exe` para facilitar a execução com apenas dois cliques.

O bot simula o comportamento humano:
- Acessa o formulário.
- Escolhe respostas aleatórias.
- Simula pausas humanas.
- Envia o formulário automaticamente.

---

## Funcionalidades

- Preenchimento automático de formulários.
- Inserção de informações via console.
- Escolha aleatória das opções.
- Contador exibindo o número de formulários enviados.
- Geração de arquivo `.exe`.

---

## Tecnologias Utilizadas

- Python 3.x
- Selenium
- Google Chrome
- ChromeDriver
- PyInstaller

---

## Instalação

### 1. Instalar o Python

Acesse [https://www.python.org/downloads/](https://www.python.org/downloads/)  
Durante a instalação, marque "**Add Python to PATH**".

### 2. Instalar as bibliotecas necessárias

```bash
pip install selenium
pip install pyinstaller
```

### 3. Instalar o Google Chrome

Se ainda não possuir, baixe em: [https://www.google.com/chrome/](https://www.google.com/chrome/)

### 4. Baixar o ChromeDriver

- Verifique sua versão do Chrome em `chrome://settings/help`.
- Baixe o correspondente em: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
- Extraia e coloque o `chromedriver.exe` na pasta do projeto.

---

## Como Usar

### 1. Executar o script manualmente

No terminal, execute:

```bash
python preenche_formulario.py
```

O script pedirá:
- Link do formulário
- Número de repetições

### 2. Gerar um arquivo executável (.exe)

Execute o comando:

```bash
pyinstaller --onefile preenche_formulario.py
```

O `.exe` será criado dentro da pasta `dist/`.

### 3. Rodar o executável

Dê dois cliques no arquivo `.exe`, informe o link do formulário e o número de repetições no console.

---

## Melhorias Futuras

- Rodar o bot em modo headless (sem abrir janela do navegador).
- Suporte a perguntas de texto e múltiplas seleções (checkbox).
- Exportar histórico de envios em arquivo `.csv`.

---

## Estrutura do Projeto

```
auto_forms_bot/
├── preenche_formulario.py
├── README.md
└── dist/
    └── preenche_formulario.exe
```

---

## Licença

Distribuído sob a licença MIT.

---

## Autor

Feito com dedicação por [Gustavo, Costa](https://github.com/Gustavop123).
