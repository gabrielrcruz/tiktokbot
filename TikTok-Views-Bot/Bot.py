
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from time import sleep

def loop1():
    global i
    sleep(10)
    try:
        driver.find_element_by_xpath("//*[@id=\"main\"]/div/div[4]/div/button").click()
    except:
        print("Você ainda não resolveu o captcha. Precisa atualizar para evitar loop infinito.")
        driver.refresh()
        loop1()
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        sleep(10)
        driver.refresh()
        i += 1
        total = i * 1000
        print("Sucesso de visualizações entregues! Total", total,"Visualizações")
        sleep(360)
        loop1()
    except:
        print("Ocorreu um erro genérico. Agora vou tentar novamente")
        driver.refresh()
        sleep(20)
        loop1()

def loop2():
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
    except:
        print("Você ainda não resolveu o captcha. Precisa atualizar para evitar loop infinito.")
        driver.refresh()
        loop2()
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("//html/body/div[4]/div[3]/div/form/div/div/button").click()
        sleep(10)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div[1]/div/form/button").click()
        sleep(10)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text
        sleep(55)
        print(hearts," Sucesso entregue! Agradeça-me com uma doação de $ 1 no GitHub")
        sleep(100)
        driver.refresh()
        sleep(200)
        loop2()
    except:
        print("Ocorreu um erro genérico. Agora vou tentar novamente")
        driver.refresh()
        sleep(355)
        loop2()

def loop3():
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
    except:
        print("Você ainda não resolveu o captcha. Precisa atualizar para evitar loop infinito.")
        driver.refresh()
        loop2()
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/form/div/div/button").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/form/button").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/form/ul/li/div/button").click()
        sleep(47)
        driver.refresh()
        print("Ações enviadas! Agradeça-me com uma doação de $ 1 no GitHub")
        loop3()
    except:
        print("Ocorreu um erro genérico. Agora vou tentar novamente")
        driver.refresh()
        sleep(50)
        loop3()

def loop4():
    sleep(20)
    wait_time = 660 #11 minutes
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click() #Followers
    except:
        print("Ocorreu um erro genérico. Agora vou tentar novamente")
        driver.refresh()
        loop4()
    try:
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/form/div/input").send_keys(vidUrl) #Write
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/div/div/form/div/div/button").click() #Search
        sleep(20)
        driver.find_element_by_xpath("//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click() #AddFollowers
        sleep(wait_time/3)
        print("Ações enviadas! Agradeça-me com uma doação de $ 1 no GitHub")
        sleep(wait_time/3)
        driver.refresh()
        sleep(wait_time/3)
        loop4()
    except:
        print("Ocorreu um erro genérico. Agora vou tentar novamente")
        driver.refresh()
        sleep(wait_time)
        loop4()

def loop5():
    sleep(20)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
    except:
        print("Você ainda não resolveu o captcha. Precisa atualizar para evitar loop infinito.")
        driver.refresh()
        loop5()
    try:
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div/form/div/input").send_keys(vidUrl) # Write
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div/form/div/div/button").click() # Search
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div/div/div[1]/div/form/button").click() # AddShares
        sleep(60)
        print("Ações enviadas! Agradeça-me com uma doação de $ 1 no GitHub")
        sleep(1700)
    except:
        print("Ocorreu um erro genérico. Agora vou tentar novamente")
        driver.refresh()
        sleep(300)
        loop5()

def loop6():
    sleep(1000)
    driver.refresh()
    print("Reload")
    loop5()

print("Autor: https://github.com/NoNameoN-A  -  Tradutor: https://github.com/gabrielrcruz")

#Coloque o Link do Video Aqui:
vidUrl = "https://www.tiktok.com/@xbeatriznascimento/video/6986285972874857734" #Change it

bot = int(input("O que você quer fazer?\n1 - Visualizações automáticas(1000)\n2 - Like Automatico\n3 - Auto Like no (Primeiro) Comentário\n4 - Seguidores Automáticos\n5 - [Novo]Auto Seguidores\n6 - Recarga Simples\n"))
i = 0

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#Para funcioanr coloque o Endereço do Chromedriver dentro de ''
driver = webdriver.Chrome(executable_path=r'C:\Users\gabrielrcruz\Desktop\codigos python\TikTok-Views-Bot\chromedriver.exe',chrome_options=chrome_options) #Change it

driver.get("https://vipto.de/")

if bot == 1:
    loop1()
elif bot == 2:
    loop2()
elif bot == 3:
    loop3()
elif bot == 4:
    loop4()
elif bot == 5:
    loop5()
elif bot == 6:
    loop5()
else:
    print("Você pode inserir apenas 1, 2, 3, 4, 5 ou 6")
