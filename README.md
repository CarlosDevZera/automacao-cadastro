# Cadastro Automatizado com foco em reconhecimento visual

Este projeto demonstra uma automação de preenchimento de cadastros em uma aplicação desktop local. Utiliza **Python** para gerar dados fictícios, uma interface gráfica com **Tkinter** para simular o sistema de cadastro, e **PyAutoGUI** para realizar a automação da inserção desses dados.

---

## 📋 Funcionalidades

- ✅ **Geração de Dados:** Criação automática de uma planilha Excel com dados fictícios (ID, nome, e-mail, telefone, estado, produto, valor, data de cadastro, status) usando a biblioteca Faker.
- ✅ **Interface Gráfica Simulada:** Uma aplicação desktop desenvolvida com Tkinter que simula um sistema de cadastro, permitindo a visualização do processo de automação.
- ✅ **Automação de Preenchimento Inteligente:** Preenchimento automático dos campos da interface gráfica com os dados lidos da planilha Excel, utilizando reconhecimento visual de elementos (baseado em imagens) para maior robustez.
- ✅ **Interação Adaptável com GUI:** Simulação de cliques e digitação que se adapta à posição dos elementos na tela (rótulos, campos, botões), graças ao reconhecimento de imagem e offsets dinâmicos. Inclui a maximização automática da janela para garantir um layout consistente.

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3.x** – Linguagem principal
- 🖼️ **Tkinter** – Para a interface gráfica do sistema de cadastro simulado
- 🧠 **Faker** – Para a geração de dados fictícios realistas
- 📊 **Pandas** – Para manipulação e criação da planilha Excel com os dados fictícios
- 엑셀 **Openpyxl** – Para leitura da planilha Excel pelo script de automação
- 🖱️ **PyAutoGUI** – Para automação de interações com a interface gráfica (cliques e teclado)
- 👁️ **OpenCV (opencv-python)** – Essencial para o reconhecimento de imagem (`locateOnScreen`) e o uso do parâmetro `confidence` no PyAutoGUI.


---

## 📂 Estrutura do Projeto (Sugerida)
/automacao-cadastro/ <br>
|-- criador_planilha_fake.py                 <br>
|-- sistema_cadastro_fake.py         <br>
|-- automacao_cadastro_clientes.py   <br>
|-- dados_ficticios_500.xlsx         <br>
|-- dados_salvos_sistema_fake.csv    <br>
|-- README.md <br>
└── imagens_referencia/             
    ├── 1.png (label ID Cliente)
    ├── 2.png (label Nome Completo)
    ├── ... (e as demais imagens de labels)
    ├── 10.png (botão Salvar Dados)
    └── 11.png (botão OK da mensagem de sucesso)                      

---

## 💻 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/CarlosDevZera/automacao-cadastro
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
    Certifique-se de que o `pip` está atualizado e instale as bibliotecas necessárias.
    ```bash
    pip install pandas faker openpyxl pyautogui opencv-python # Adicionado 'opencv-python' e removido 'pyperclip' se não usado.
    ```
    *(Tkinter geralmente já vem com a instalação padrão do Python).*

5.  **Prepare as Imagens de Referência:**
    * **Crucial para a automação visual:** Verifique se a pasta `imagens_referencia/` (localizada no mesmo diretório dos scripts) contém todas as imagens `.png` necessárias para o reconhecimento dos elementos da interface.
    * Essas imagens (como `1.png` a `11.png`) são capturas específicas dos rótulos e botões da GUI do `sistema_cadastro_fake.py`.

6.  **Execute o criador_planilha_fake:**
    Este script criará o arquivo `dados_ficticios_500.xlsx` no mesmo diretório, que será a fonte de dados para a automação.
    ```bash
    python criador_planilha_fake.py
    ```

7.  **Execute o Script de Automação:**
    Este script **irá iniciar o `sistema_cadastro_fake.py` (a GUI Tkinter)** e, em seguida, começará a preencher os dados automaticamente.
    ```bash
    python automacao_cadastro_clientes.py
    ```

    **Atenção Importante:**
    * Durante a execução, o script **tentará maximizar automaticamente a janela do "Sistema de Cadastro de Clientes (Fake)"** para padronizar o layout e otimizar o reconhecimento dos elementos.
    * A janela do aplicativo deve estar **visível na tela e sem sobreposição** de outras janelas para que o PyAutoGUI possa localizar os elementos visuais com precisão.
    * **Não mova o mouse ou use o teclado** durante a execução da automação para evitar interrupções ou o acionamento do `fail-safe` do PyAutoGUI.
    * A precisão do reconhecimento de imagem é **sensível a mudanças na resolução da tela e, principalmente, nas configurações de escala (DPI)** do sistema operacional. Se a automação falhar em um ambiente diferente, pode ser necessário **recapturar as imagens de referência** (`.png` na pasta `imagens_referencia/`) para aquele ambiente específico e/ou ajustar os offsets no script `automacao_cadastro_clientes.py`.

---

## 📜 Explicação dos Scripts

* **`criador_planilha_fake.py`:**
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
        * **Localizar elementos da GUI (rótulos e botões) através de reconhecimento de imagem (`locateOnScreen`) na tela.**
        * **Clicar nos campos aplicando offsets (deslocamentos) calculados** a partir da localização das imagens dos rótulos, garantindo precisão mesmo com a janela reposicionada.
        * Digitar os dados correspondentes.
        * Lidar com a formatação de datas e limpeza de campos (usando `Ctrl+A` e `Backspace`).
        * Clicar nos botões de "Salvar" e "OK" (na mensagem de confirmação).
        * **Maximizar a janela do aplicativo (`Windows + Seta Para Cima`) automaticamente para padronizar o ambiente de automação.**

---



