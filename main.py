from pathlib import Path
import time
import random
import sys
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from contacts.contact_list import Users_loader
from message.message import Msg_loader

# Caminho do driver compatível com PyInstaller (Path to the driver compatible with PyInstaller)
if getattr(sys, 'frozen', False):
    application_path = Path(sys._MEIPASS)
else:
    application_path = Path(__file__).parent    
chrome_driver = application_path / "drivers" / "chromedriver-win64" / "chromedriver.exe"

# Configurações do Selenium (Selenium settings)
options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--log-level=3") 
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service, options=options)

# Carregar lista de usuários (Load the list of users)
user_list = Users_loader()
limit_to_connect_QR = 30

# Login no WhatsApp Web (Login to WhatsApp Web)
driver.get("https://web.whatsapp.com/")
print("Conecte-se ao WhatsApp Web através do QR CODE (Connect to WhatsApp Web via QR CODE)")
time.sleep(limit_to_connect_QR)  

# Relatórios de envio (Sending reports)
sucess_sends = []
fail_sends = []

for i, user in enumerate(user_list, 1):
    encoded_msg = Msg_loader(user["name"])
    phone_number = user["phone"]
    URL_WPP = f"https://web.whatsapp.com/send?phone=55{phone_number}&text={encoded_msg}"
    driver.get(URL_WPP)

    try:
        btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Enviar"]'))
        )
        btn.click()
        sucess_sends.append(user)
        print(f'Mensagem enviada para {user["name"]} - {i} / {len(user_list) + 1} ')

    except Exception:
        print("Segunda tentativa de envio (Second attempt to send)")
        try: 
            driver.get(URL_WPP)
            btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Enviar"]'))
            )
            btn.click()
            sucess_sends.append(user)
            print("Enviado na segunda tentativa (Sent on the second attempt)")
        except Exception:             
            fail_sends.append(user)
            print(f"Falha ao enviar para {user['name']} número: {user['phone']} (Failed to send to {user['name']} number: {user['phone']})")
    
    min_interval = 5
    max_interval = 15
    # Intervalo aleatório entre 5 e 15 segundos (Random interval between 5 and 15 seconds)
    random_timestamp = random.randint(min_interval, max_interval)
    time.sleep(random_timestamp)

# Impressão final (Final print)
print(f"Envio concluído com sucesso. {len(sucess_sends)} enviados com sucesso. {len(fail_sends)} não enviados. (Sending completed successfully. {len(sucess_sends)} sent successfully. {len(fail_sends)} failed.)")
print("Lista de insucesso: \n (Failed list: )")
for i in fail_sends:
    print(f"Nome: {i['name']} \nTelefone: {i['phone']}")

# Criar pasta dos relatórios (Create reports folder)
folder = Path("reports")
folder.mkdir(parents=True, exist_ok=True)

# Nomeação de Arquivo (File naming)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_txt = folder / f"relatorio_envio_{timestamp}.txt"
report_csv = folder / f"relatorio_envio_{timestamp}.csv"

# Gravar relatório em TXT (Save report in TXT)
with open(report_txt, "w", encoding="utf-8") as report_file:
    report_file.write("Relatório de envio de mensagens (Message sending report)\n")
    report_file.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
    report_file.write(f"Total enviados com sucesso: {len(sucess_sends)} (Total sent successfully: {len(sucess_sends)})\n")
    report_file.write(f"Total falhas: {len(fail_sends)} (Total failures: {len(fail_sends)})\n\n")

    report_file.write("== Enviados com sucesso == (== Sent successfully ==)\n")
    for s in sucess_sends:
        report_file.write(f"Nome: {s['name']} | Telefone: {s['phone']}\n")

    report_file.write("\n== Falhas == (== Failures ==)\n")
    for f in fail_sends:
        report_file.write(f"Nome: {f['name']} | Telefone: {f['phone']}\n")

# Gravar relatório em CSV (Save report in CSV)
with open(report_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Nome", "Telefone", "Status"])
    for s in sucess_sends:
        writer.writerow([s['name'], s['phone'], "Enviado (Sent)"])
    for f in fail_sends:
        writer.writerow([f['name'], f['phone'], "Falha (Failed)"])

print(f"Relatórios salvos em:\nTXT -> {report_txt}\nCSV -> {report_csv} (Reports saved in TXT -> {report_txt} CSV -> {report_csv})")

driver.quit()
