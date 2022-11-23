from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time



def login_test(url,email,password): 
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(url)  

    driver.find_element(By.CLASS_NAME,"flag-country-block").click()

    username = driver.find_element(By.NAME,"username").send_keys(email)  
    password = driver.find_element(By.ID,"loginPassInput").send_keys(password)  
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[5]/div/button").click()

    old_title = "The Futurely: Login"
    print(driver.current_url)
    print(driver.title)
    if old_title != driver.title:
        print("Pass test case")
    else:
        print("Not Pass test case")

def forget_password_check(url,email,newpassword):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(url)  

    try:
        if len(driver.find_elements(By.CLASS_NAME,"flag-country-block"))>0:
            driver.find_element(By.CLASS_NAME,"flag-country-block").click()
        email = driver.find_element(By.ID,"id_email").send_keys(email) 
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[3]/div/button").click()
        print("Enter forget password link ")
        link_forget = input()
        time.sleep(5)
        driver.get(link_forget)
        password1 = driver.find_element(By.ID,"id_new_password1").send_keys(newpassword)
        password2 = driver.find_element(By.ID,"id_new_password2").send_keys(newpassword)
        title1 = driver.title
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[3]/div/button").click()
        if title1!=driver.title:
            print("Password done....")
        else:
            print("Password not change")
        return True


    except Exception as e:
        print("Error",e)



# url = "https://beta.myfuturely.com/password_reset/"
url = "https://beta.myfuturely.com/login/"
email = "mhaskesamadhan223@gmail.com"
password = "Pass@123456"
login_test(url, email, password)
# forget_password_check(url, email,"Pass@123456")