# 🚀 Cadastro Automatizado

Este projeto demonstra uma automação de preenchimento de cadastros em uma aplicação desktop local. Utiliza **Python** para gerar dados fictícios, uma interface gráfica com **Tkinter** para simular o sistema de cadastro, e **PyAutoGUI** para realizar a automação da inserção desses dados.

---

## 📋 Funcionalidades

- ✅ **Geração de Dados:** Criação automática de uma planilha Excel com dados fictícios (ID, nome, e-mail, telefone, estado, produto, valor, data de cadastro, status) usando a biblioteca Faker.
- ✅ **Interface Gráfica Simulada:** Uma aplicação desktop desenvolvida com Tkinter que simula um sistema de cadastro, permitindo a visualização do processo de automação.
- ✅ **Automação de Preenchimento:** Preenchimento automático dos campos da interface gráfica com os dados lidos da planilha Excel.
- ✅ **Interação com GUI:** Simulação de cliques e digitação para interagir com os campos, botões e menus de seleção da aplicação.

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3.x** – Linguagem principal
- 🖼️ **Tkinter** – Para a interface gráfica do sistema de cadastro simulado
- 🧠 **Faker** – Para a geração de dados fictícios realistas
- 📊 **Pandas** – Para manipulação e criação da planilha Excel com os dados fictícios
- 엑셀 **Openpyxl** – Para leitura da planilha Excel pelo script de automação
- 🖱️ **PyAutoGUI** – Para automação de interações com a interface gráfica (cliques e teclado)


---

## 📂 Estrutura do Projeto (Sugerida)
/automacao-cadastro/ <br>
|-- gerador_dados.py                 <br>
|-- sistema_cadastro_fake.py         <br>
|-- automacao_cadastro_clientes.py   <br>
|-- dados_ficticios_500.xlsx         <br>
|-- dados_salvos_sistema_fake.csv    <br>
|-- README.md                       

---

## 💻 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/CarlosDevZera/automacao-cadastro](https://github.com/CarlosDevZera/automacao-cadastro)
    ```

2.  **Acesse a pasta do projeto:**
    ```bash
    cd automacao-cadastro
    ```

3.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    Certifique-se de que o `pip` está atualizado e instale as bibliotecas listadas no `requirements.txt` (se você criar um) ou manualmente:
    ```bash
    pip install pandas faker openpyxl pyautogui pyperclip
    ```
    *(Tkinter geralmente já vem com a instalação padrão do Python).*

5.  **Execute o Gerador de Dados:**
    Este script criará o arquivo `dados_ficticios_500.xlsx` no mesmo diretório.
    ```bash
    python gerador_dados.py
    ```

6.  **Execute o Script de Automação:**
    Este script tentará iniciar o `sistema_cadastro_fake.py` (a GUI Tkinter) e, em seguida, começará a preencher os dados.
    ```bash
    python automacao_cadastro_clientes.py
    ```

    * **Atenção:** A janela do "Sistema de Cadastro de Clientes (Fake)" deve estar visível e idealmente sem sobreposição de outras janelas para que o PyAutoGUI funcione corretamente com as coordenadas.
    * Não mova o mouse ou use o teclado durante a execução da automação para evitar interrupções ou o acionamento do *fail-safe* do PyAutoGUI.

---

## 📜 Explicação dos Scripts

* **`gerador_dados.py`:**
    * Utiliza `Faker` para criar dados realistas e `pandas` para organizar esses dados em um DataFrame.
    * Salva o DataFrame como uma planilha Excel (`dados_ficticios_500.xlsx`), que servirá de entrada para o robô.

* **`sistema_cadastro_fake.py`:**
    * Cria uma janela de cadastro simples usando `Tkinter`, com campos de texto e comboboxes.
    * Possui botões para "Salvar Dados" (que salva os dados dos campos em `dados_salvos_sistema_fake.csv`) e "Limpar Campos".
    * Serve como o "sistema alvo" para a automação.

* **`automacao_cadastro_clientes.py`:**
    * Inicia o `sistema_cadastro_fake.py` usando `subprocess`.
    * Lê os dados da planilha `dados_ficticios_500.xlsx` usando `openpyxl`.
    * Itera sobre cada linha da planilha e usa `pyautogui` para:
        * Clicar nas coordenadas específicas de cada campo da interface gráfica.
        * Digitar os dados correspondentes.
        * Lidar com a formatação de datas e limpeza de campos (usando `Ctrl+A` e `Backspace`).
        * Clicar nos botões de "Salvar" e "OK" (na mensagem de confirmação).

---




