from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



def main_page_is_loding(url,path): 
    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    # options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    url = url +path
    driver.get(url)
    delay = 3 # seconds
    try:
        driver.find_element(By.CLASS_NAME,"flag-country-block").click()

        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'main-content')))
        print("Page is ready!")
        return True
    except TimeoutException:
        print ("Loading took too much time!")
        return False

def about_page_is_loding(url,path):
    # class => passsion-meets 
    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    # options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    url = url +path
    driver.get(url)
    delay = 3 # seconds
    try:
        if len(driver.find_elements(By.CLASS_NAME,"flag-country-block"))>0:
            driver.find_element(By.CLASS_NAME,"flag-country-block").click()

        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'passsion-meets')))
        print("About Page is ready!")
        return True
    except Exception as e:
        print ("Aboout Page is Not loding")
        return False
def plan_is_loding(url,path):
    # pricing-section-new
    options = webdriver.ChromeOptions()

    options.add_argument("--headless")      
    # options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    url = url +path
    driver.get(url)
    delay = 3 # seconds
    try:
        if len(driver.find_elements(By.CLASS_NAME,"flag-country-block"))>0:
            driver.find_element(By.CLASS_NAME,"flag-country-block").click()

        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'main-content')))
        print("Plan Page is ready!")
        return True
    except Exception as e:
        print ("Plan Page is Not loding",e)
        return False
def mentor_is_loding(url,path):
    # main-content
    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    # options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    url = url +path
    driver.get(url)
    delay = 3 # seconds
    try:
        if len(driver.find_elements(By.CLASS_NAME,"flag-country-block"))>0:
            driver.find_element(By.CLASS_NAME,"flag-country-block").click()

        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'main-content')))
        print("Mentor Page is ready!")
        return True
    except Exception as e:
        print ("Mentor Page is Not loding")
        return False

def student_is_loading(url,path):
    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    # options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    url = url +path
    driver.get(url)
    delay = 3 # seconds
    try:
        if len(driver.find_elements(By.CLASS_NAME,"flag-country-block"))>0:
            driver.find_element(By.CLASS_NAME,"flag-country-block").click()

        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'main-content')))
        studnet_from = driver.find_elements(By.XPATH,"//*[@id='lets-talk-f']")
        if len(studnet_from)==1:
            print("Got form..")
        print("Student Page is ready!")
        return True
    except Exception as e:
        print ("Studebt Page is Not loding")
        return False
def home_is_loading(url,path):
    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    # options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    url = url +path
    driver.get(url)
    delay = 3 # seconds
    try:
        if len(driver.find_elements(By.CLASS_NAME,"flag-country-block"))>0:
            driver.find_element(By.CLASS_NAME,"flag-country-block").click()

        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'main-content')))
        people_section = driver.find_elements(By.XPATH,"/html/body/div[1]/div/section[5]")
        if len(people_section)!=0:
            print("Got People..")
        print("Student Page is ready!")
        return True
    except Exception as e:
        print ("Studebt Page is Not loding")
        return False


url = "https://beta.myfuturely.com/"
# h = home_is_loading(url)
# a = about_page_is_loding(url,"about/")
print(url)
b= plan_is_loding(url,"plans/")
c = mentor_is_loding(url,"mentor/")
d = student_is_loading(url,"students/")
#  headless