import pyautogui
import time
import openpyxl
import subprocess # Importa o módulo para rodar outros programas


workbook = openpyxl.load_workbook('D:/PyProjetos/pjt006/automacao-cadastro/dados_ficticios_500.xlsx')
vendas_sheet = workbook['Sheet1']

SISTEMA_FAKE = 'D:/PyProjetos/pjt006/automacao-cadastro/sistema_cadastro_fake.py'

subprocess.Popen(['python', SISTEMA_FAKE])

print("Sistema Fake supostamente aberto. Aguardando 5 segundos para carregar...")
time.sleep(2) # Dê um tempo para o sistema fake abrir e carregar.

print("Processo de abertura finalizado.")


for i in vendas_sheet.iter_rows(min_row=2):
    #id
    pyautogui.click(347,169, duration=0.2)
    pyautogui.write(str(i[0].value))

    #Nome
    pyautogui.click(352, 197, duration=0.2)
    pyautogui.write(i[1].value)

    #Email
    pyautogui.click(352, 232, duration=0.2)
    pyautogui.write(i[2].value)

    #Telefone
    pyautogui.click(351, 261, duration=0.2)
    pyautogui.write(str(i[3].value))

    #Estado
    pyautogui.click(351, 288, duration=0.2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)  # Pequena pausa
    pyautogui.press('backspace')  # ou 'delete'
    pyautogui.write(i[4].value)

    #Produto
    pyautogui.click(351, 326, duration=0.2)
    pyautogui.write(i[5].value)

    #Valor
    pyautogui.click(349, 350, duration=0.2)
    pyautogui.write(str(i[6].value))

    #Data
    pyautogui.click(349, 388, duration=0.2)

    if i[7].value is not None and hasattr(i[7].value, 'strftime'):
        data_formatada = i[7].value.strftime('%d/%m/%Y')
        pyautogui.write(data_formatada)
    elif i[7].value is not None:
        valor_como_string = str(i[7].value)

        if " 00:00:00" in valor_como_string:
            pyautogui.write(valor_como_string.split(" ")[0])
        else:
            pyautogui.write(valor_como_string)
    else:
        pyautogui.write("")


    #Status
    pyautogui.click(353, 415, duration=0.2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)  # Pequena pausa
    pyautogui.press('backspace')
    pyautogui.write(i[8].value)

    #Salvar
    pyautogui.click(337, 652, duration=0.2)

    #Ok
    pyautogui.click(732, 444, duration=0.2)


