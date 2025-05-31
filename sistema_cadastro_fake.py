import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import os

# Nome do arquivo CSV onde os dados serão salvos
NOME_ARQUIVO_CSV = 'dados_salvos_sistema_fake.csv'

def criar_tela_cadastro():
    janela = tk.Tk()
    janela.title("Sistema de Cadastro de Clientes (Fake)")
    janela.geometry("600x550+100+100")
    janela.resizable(True, True)

    global entry_fields
    entry_fields = {}

    form_frame = ttk.Frame(janela, padding="20")
    form_frame.pack(fill="both", expand=True)

    # --- Campos do Formulário ---
    ttk.Label(form_frame, text="ID Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_fields['id_cliente'] = ttk.Entry(form_frame, width=50)
    entry_fields['id_cliente'].grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(form_frame, text="Nome Completo:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_fields['nome_completo'] = ttk.Entry(form_frame, width=50)
    entry_fields['nome_completo'].grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(form_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_fields['email'] = ttk.Entry(form_frame, width=50)
    entry_fields['email'].grid(row=2, column=1, padx=5, pady=5)

    ttk.Label(form_frame, text="Telefone:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    entry_fields['telefone'] = ttk.Entry(form_frame, width=50)
    entry_fields['telefone'].grid(row=3, column=1, padx=5, pady=5)

    ttk.Label(form_frame, text="Estado (UF):").grid(row=4, column=0, padx=5, pady=5, sticky="w")
    estados_brasileiros = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    entry_fields['estado'] = ttk.Combobox(form_frame, values=estados_brasileiros, width=47)
    entry_fields['estado'].grid(row=4, column=1, padx=5, pady=5)
    entry_fields['estado'].set("SP")

    ttk.Label(form_frame, text="Produto:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
    entry_fields['produto'] = ttk.Entry(form_frame, width=50)
    entry_fields['produto'].grid(row=5, column=1, padx=5, pady=5)

    ttk.Label(form_frame, text="Valor Última Compra:").grid(row=6, column=0, padx=5, pady=5, sticky="w")
    entry_fields['valor_ultima_compra'] = ttk.Entry(form_frame, width=50)
    entry_fields['valor_ultima_compra'].grid(row=6, column=1, padx=5, pady=5)

    ttk.Label(form_frame, text="Data Cadastro (AAAA-MM-DD):").grid(row=7, column=0, padx=5, pady=5, sticky="w")
    entry_fields['data_cadastro'] = ttk.Entry(form_frame, width=50)
    entry_fields['data_cadastro'].grid(row=7, column=1, padx=5, pady=5)

    ttk.Label(form_frame, text="Status Cliente:").grid(row=8, column=0, padx=5, pady=5, sticky="w")
    status_opcoes = ['Ativo', 'Inativo', 'Pendente']
    entry_fields['status_cliente'] = ttk.Combobox(form_frame, values=status_opcoes, width=47)
    entry_fields['status_cliente'].grid(row=8, column=1, padx=5, pady=5)
    entry_fields['status_cliente'].set("Ativo")

    # --- Funções para os Botões ---
    def salvar_dados_fake():
        dados_coletados = {
            'ID_Cliente': [entry_fields['id_cliente'].get()], # Coloque como lista para criar um DataFrame de uma linha
            'Nome_Completo': [entry_fields['nome_completo'].get()],
            'Email': [entry_fields['email'].get()],
            'Telefone': [entry_fields['telefone'].get()],
            'Estado': [entry_fields['estado'].get()],
            'Produto': [entry_fields['produto'].get()],
            'Valor_Ultima_Compra': [entry_fields['valor_ultima_compra'].get()],
            'Data_Cadastro': [entry_fields['data_cadastro'].get()],
            'Status_Cliente': [entry_fields['status_cliente'].get()]
        }

        # Cria um DataFrame do pandas com os dados da linha atual
        df_novo_registro = pd.DataFrame(dados_coletados)

        # Verifica se o arquivo CSV já existe
        if not os.path.exists(NOME_ARQUIVO_CSV):
            # Se não existe, cria o arquivo com cabeçalho
            df_novo_registro.to_csv(NOME_ARQUIVO_CSV, index=False, mode='w', encoding='utf-8',
                                    sep=';')  # Adicione sep=';'
            print(f"Arquivo '{NOME_ARQUIVO_CSV}' criado com o primeiro registro.")
        else:
            # Se existe, anexa o novo registro sem cabeçalho
            df_novo_registro.to_csv(NOME_ARQUIVO_CSV, index=False, mode='a', header=False, encoding='utf-8',
                                    sep=';')  # Adicione sep=';'
            print(f"Novo registro anexado a '{NOME_ARQUIVO_CSV}'.")


        messagebox.showinfo("Sucesso", "Dados salvos no CSV!")
        limpar_campos()

    def limpar_campos():
        for field_name in entry_fields:
            if isinstance(entry_fields[field_name], ttk.Entry):
                entry_fields[field_name].delete(0, tk.END)
            elif isinstance(entry_fields[field_name], ttk.Combobox):
                entry_fields[field_name].set("")
        entry_fields['estado'].set("SP")
        entry_fields['status_cliente'].set("Ativo")
        entry_fields['nome_completo'].focus_set()

    # --- Botões ---
    button_frame = ttk.Frame(janela, padding="10")
    button_frame.pack(pady=10)

    btn_salvar = ttk.Button(button_frame, text="Salvar Dados", command=salvar_dados_fake)
    btn_salvar.pack(side="left", padx=10)

    btn_limpar = ttk.Button(button_frame, text="Limpar Campos", command=limpar_campos)
    btn_limpar.pack(side="left", padx=10)

    janela.mainloop()

if __name__ == "__main__":
    criar_tela_cadastro()