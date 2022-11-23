from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def register_user(url,first_name,last_name,gender,are_you_14,email,password,number,how_did_you_know,school_region,school_city,school_name,your_grade,discount_code=None):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(url)  

    try:
        if len(driver.find_elements(By.XPATH,"//*[@id='changecountryModal']/div/div/div[2]/div[2]/a/img"))>0:
            driver.find_element(By.XPATH,"//*[@id='changecountryModal']/div/div/div[2]/div[2]/a/img").click()
        driver.find_element(By.ID,"id_first_name").send_keys(first_name)
        driver.find_element(By.ID,"id_last_name").send_keys(last_name)

        Gender_select = driver.find_element(By.ID,"id_gender")

        select = Select(Gender_select)
        select.select_by_value(gender)
        are_you_14_select = driver.find_element(By.ID,"id_are_you_fourteen_plus")

        select_14 = Select(are_you_14_select)
        select_14.select_by_value(are_you_14)
        driver.find_element(By.ID,"id_email").send_keys(email)
        driver.find_element(By.ID,"id_password").send_keys(password)
        driver.find_element(By.ID,"id_contact_number").send_keys(number)

        id_how_know_us_select = Select(driver.find_element(By.ID,"id_how_know_us"))
        id_how_know_us_select.select_by_value(how_did_you_know)
        time.sleep(5)
        if len(driver.find_elements(By.XPATH,"/html/body/div[2]/div/div/div[2]/a[1]"))!=0:
            driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/a[1]").click()
        driver.find_element(By.ID,"btn_next").click()
        if len(driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]"))==0:
            print("Some Problem come")
            return False
        if discount_code!=None:
            driver.find_element(By.ID,"id_discount_coupon_code").send_keys(discount_code)
            # if len(driver.find_elements(By.ID,"lbl-message"))!=0:
            #     print(driver.find_elements(By.ID,"lbl-message").text)
        print("==================")
        school_region_select = Select(driver.find_element(By.ID,"id-school-region"))
        school_region_select.select_by_value(school_region)
        time.sleep(5)
        
        school_city_select = Select(driver.find_element(By.ID,"id-school-city"))
        school_city_select.select_by_value(school_city)
        time.sleep(5)

        school_name_select = Select(driver.find_element(By.ID,"id-school-name"))
        school_name_select.select_by_value(school_name)
        if school_name=="Other":
            driver.find_element(By.ID,"id_school_name_other").send_keys("New school")
        your_grade_select = Select(driver.find_element(By.ID,"id-class-year"))
        your_grade_select.select_by_value(your_grade)
        time.sleep(5)
        # check box not working
        # check_box = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[3]/div[1]/divs")
        # print(check_box.get_attribute("checked"))
        # check_box.click()
        title = driver.title
        driver.find_element(By.ID,"btn-submit").click()
        time.sleep(5)
        print(driver.title)
        if title != driver.title:
            print("Register Done...")
            return True
        else:
            print("Register Not Done...")
            return False
    except Exception as e:
        print("Error come...",e)

register_user("https://beta.myfuturely.com/register/","sama", "mhakse", "Male", "Yes","mhaske+34@gmail.com","Pass@12345","9356484147","Facebook","California","ALAMEDA","Other","1","Test1")
