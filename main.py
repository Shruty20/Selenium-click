
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("enter your first name")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("enter your last name")
email = driver.find_element(By.NAME, value="email")
email.send_keys("enter your mail id")
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()










