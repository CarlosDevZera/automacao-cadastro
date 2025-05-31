import pyautogui
import time
import openpyxl
import subprocess
import os

# --- Configurações das imagens de referência ---
IMAGENS_PATH = 'D:/PyProjetos/pjt006/automacao-cadastro/imagens_referencia'

# Dicionário de imagens de referência para os rótulos
IMAGENS_LABELS = {
    'id_cliente': os.path.join(IMAGENS_PATH, '1.png'),
    'nome_completo': os.path.join(IMAGENS_PATH, '2.png'),
    'email': os.path.join(IMAGENS_PATH, '3.png'),
    'telefone': os.path.join(IMAGENS_PATH, '4.png'),
    'estado': os.path.join(IMAGENS_PATH, '5.png'),
    'produto': os.path.join(IMAGENS_PATH, '6.png'),
    'valor_compra': os.path.join(IMAGENS_PATH, '7.png'),
    'data_cadastro': os.path.join(IMAGENS_PATH, '8.png'),
    'status_cliente': os.path.join(IMAGENS_PATH, '9.png'),
}

# Imagens para botões e caixas de mensagem
IMAGEM_BOTAO_SALVAR = os.path.join(IMAGENS_PATH, '10.png')
IMAGEM_BOTAO_OK_POPUP = os.path.join(IMAGENS_PATH, '11.png')


# Offset padrão para clicar no campo de entrada ao lado do rótulo
# Estes são os valores CALCULADOS para cada campo
OFFSETS_CAMPOS = {
    'id_cliente': {'x': 161, 'y': 0},
    'nome_completo': {'x': 144, 'y': 0},
    'email': {'x': 172, 'y': 0},
    'telefone': {'x': 172, 'y': 0},
    'estado': {'x': 166, 'y': 0},
    'produto': {'x': 169, 'y': 0},
    'valor_compra': {'x': 135, 'y': 0},
    'data_cadastro': {'x': 115, 'y': 0},
    'status_cliente': {'x': 158, 'y': 0},
}

# --- Carregamento dos dados ---
workbook = openpyxl.load_workbook('D:/PyProjetos/pjt006/automacao-cadastro/dados_ficticios_500.xlsx')
vendas_sheet = workbook['Sheet1']

SISTEMA_FAKE_PATH = 'D:/PyProjetos/pjt006/automacao-cadastro/sistema_cadastro_fake.py'

# --- Função auxiliar para encontrar e clicar em um elemento ---
def encontrar_e_clicar(imagem_path, offset_x=0, offset_y=0, confidence=0.9, attempts=3, delay=0.5):
    for _ in range(attempts):
        try:
            location = pyautogui.locateCenterOnScreen(imagem_path, confidence=confidence)
            if location:
                click_point = (location.x + offset_x, location.y + offset_y)
                pyautogui.click(click_point, duration=0.2)
                return click_point
        except pyautogui.ImageNotFoundException:
            pass # Continua para a próxima tentativa
        time.sleep(delay)
    raise Exception(f"Elemento '{os.path.basename(imagem_path)}' não encontrado na tela após {attempts} tentativas.")

# --- Abrir o sistema fake ---
process = subprocess.Popen(['python', SISTEMA_FAKE_PATH])

print("Sistema Fake supostamente aberto. Aguardando 5 segundos para carregar...")
time.sleep(3)
pyautogui.hotkey('win', 'up')
time.sleep(1)

print("Processo de abertura finalizado. Iniciando automação...")

for i, row in enumerate(vendas_sheet.iter_rows(min_row=2)):
    print(f"\nPreenchendo registro {i+1}...")
    try:
        # ID
        encontrar_e_clicar(IMAGENS_LABELS['id_cliente'],
                           offset_x=OFFSETS_CAMPOS['id_cliente']['x'],
                           offset_y=OFFSETS_CAMPOS['id_cliente']['y'])
        pyautogui.write(str(row[0].value))

        # Nome
        encontrar_e_clicar(IMAGENS_LABELS['nome_completo'],
                           offset_x=OFFSETS_CAMPOS['nome_completo']['x'],
                           offset_y=OFFSETS_CAMPOS['nome_completo']['y'])
        pyautogui.write(row[1].value)

        # Email
        encontrar_e_clicar(IMAGENS_LABELS['email'],
                           offset_x=OFFSETS_CAMPOS['email']['x'],
                           offset_y=OFFSETS_CAMPOS['email']['y'])
        pyautogui.write(row[2].value)

        # Telefone
        encontrar_e_clicar(IMAGENS_LABELS['telefone'],
                           offset_x=OFFSETS_CAMPOS['telefone']['x'],
                           offset_y=OFFSETS_CAMPOS['telefone']['y'])
        pyautogui.write(str(row[3].value))

        # Estado (Combobox)
        estado_click_point = encontrar_e_clicar(IMAGENS_LABELS['estado'],
                                                 offset_x=OFFSETS_CAMPOS['estado']['x'],
                                                 offset_y=OFFSETS_CAMPOS['estado']['y'])
        if estado_click_point:
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.1)
            pyautogui.press('backspace')
            pyautogui.write(row[4].value)



        # Produto
        encontrar_e_clicar(IMAGENS_LABELS['produto'],
                           offset_x=OFFSETS_CAMPOS['produto']['x'],
                           offset_y=OFFSETS_CAMPOS['produto']['y'])
        pyautogui.write(row[5].value)

        # Valor
        encontrar_e_clicar(IMAGENS_LABELS['valor_compra'],
                           offset_x=OFFSETS_CAMPOS['valor_compra']['x'],
                           offset_y=OFFSETS_CAMPOS['valor_compra']['y'])
        pyautogui.write(str(row[6].value))

        # Data
        encontrar_e_clicar(IMAGENS_LABELS['data_cadastro'],
                           offset_x=OFFSETS_CAMPOS['data_cadastro']['x'],
                           offset_y=OFFSETS_CAMPOS['data_cadastro']['y'])
        if row[7].value is not None and hasattr(row[7].value, 'strftime'):
            data_formatada = row[7].value.strftime('%d/%m/%Y')
            pyautogui.write(data_formatada)
        elif row[7].value is not None:
            valor_como_string = str(row[7].value)
            if " 00:00:00" in valor_como_string:
                pyautogui.write(valor_como_string.split(" ")[0])
            else:
                pyautogui.write(valor_como_string)
        else:
            pyautogui.write("")

        # Status (Combobox)
        status_click_point = encontrar_e_clicar(IMAGENS_LABELS['status_cliente'],
                                                 offset_x=OFFSETS_CAMPOS['status_cliente']['x'],
                                                 offset_y=OFFSETS_CAMPOS['status_cliente']['y'])
        if status_click_point:
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.1)
            pyautogui.press('backspace')
            pyautogui.write(row[8].value)

        # Clicar no botão Salvar
        encontrar_e_clicar(IMAGEM_BOTAO_SALVAR, confidence=0.8)
        time.sleep(1)

        # Clicar no botão OK da caixa de mensagem
        encontrar_e_clicar(IMAGEM_BOTAO_OK_POPUP, confidence=0.8)
        time.sleep(0.5)

    except Exception as e:
        print(f"Erro ao processar registro {i+1}: {e}")
        break

print("\nAutomação concluída!")
process.terminate()