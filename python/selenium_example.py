# ESTE PROGRAMA FOI CRIADO COM O INTUITO DE CAPTURAR, TODOS OS MESES, O PRÓXIMO BOLETO A VENCER DA PLANO&PLANO! 
# CRIE COM INTUITO DE ENCAMINHAR AO E-MAIL DE MINHA MÃE, QUE POR SINAL NÃO SE DA MUITO BEM COM A TECNOLOGIA RSRS. 
# LOGO APROVEITEI A OPORTUNIDADE E RESOLVI CRIAR ESTE PROGRAMINHA UTILIZANDO O SELENIUM 
# (POR MAIS QUE TENHA ALGUM MECANISMO QUE JÁ FAÇA ISTO, ENFIM, FOI LEGAL PRO CONHECIMENTO). 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time as time

login = ""
senha = ""
email = ""

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get("https://relacionamento.planoeplano.com.br/acesso")
driver.maximize_window()

time.sleep(10)

form = driver.find_element(By.TAG_NAME, "form")
tag_inputs = form.find_elements(By.TAG_NAME, "input")

for i in range(len(tag_inputs)):    
    if i == 0:     
        tag_inputs[i].send_keys(login)
    elif i == 1:
        tag_inputs[i].send_keys(senha)

btn_acessar = form.find_element(By.TAG_NAME, "button")  

if btn_acessar.get_attribute("type") == "submit":
    btn_acessar.click()
else:
    print("====== * OCORREU UM ERRO * ======")

time.sleep(10)

btn_pagar = driver.find_element(By.CLASS_NAME, "payment-slip__pay-btn")
btn_pagar.click()
input_email = driver.find_element(By.TAG_NAME, "input")
input_email.clear()
input_email.send_keys(email)
btn_submit = driver.find_element(By.CLASS_NAME, "v-btn__content")
btn_submit.click()

driver.quit()
