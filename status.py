from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
        
    chrome_options.add_experimental_option('prefs', {
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

driver = iniciar_driver()
driver.get('https://pt-pt.facebook.com/')
driver.maximize_window()

cookies = driver.find_element(By.XPATH,'//button[@class="_42ft _4jy0 _9xo6 _4jy3 _4jy1 selected _51sy"]')
cookies.click()
sleep(1)

campo_email = driver.find_element(By.XPATH,'//input[@class="inputtext _55r1 _6luy"]')
campo_email.send_keys('nandovalverde@gmail.com')
sleep(5)

campo_senha = driver.find_element(By.ID,'pass')
campo_senha.send_keys('xxxxxxxxxxxxxxxx')
sleep(5)

botao_login = driver.find_element(By.NAME, 'login')
botao_login.click()
sleep(3)

campo_status = driver.find_element(By.XPATH,'//div[@class="m9osqain a5q79mjw gy2v8mqq jm1wdb64 k4urcfbm qv66sw1b"]')
campo_status.click()
sleep(2)

digitar_status = driver.find_element(By.XPATH,'//div[@class="_1mf _1mj"]')
sleep(2)
digitar_status.click()
digitar_status.send_keys('Hola Mundo!')
sleep(2)
botao_publicar = driver.find_element(By.XPATH, '//div[@class="l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv d1544ag0 tw6a2znq s1i5eluu ta1k9048"]//span[@class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5"]')
botao_publicar.click()




input('')
driver.close()