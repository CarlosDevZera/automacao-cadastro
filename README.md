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
- 📋 **Pyperclip** (Recomendado) – Para copiar/colar texto, especialmente útil para caracteres especiais.

---

## 📂 Estrutura do Projeto (Sugerida)
/automacao-cadastro/
|-- gerador_dados.py                # Script para gerar dados_ficticios_500.xlsx
|-- sistema_cadastro_fake.py        # Script da aplicação Tkinter GUI (sistema alvo)
|-- automacao_cadastro_clientes.py  # Script principal de automação com PyAutoGUI
|-- dados_ficticios_500.xlsx        # Gerado por gerador_dados.py (após execução)
|-- dados_salvos_sistema_fake.csv   # Gerado por sistema_cadastro_fake.py (após interações)
|-- README.md                       # Este arquivo




