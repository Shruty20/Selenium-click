
from selenium import webdriver
from selenium.webdriver.common.by import By

#keep window open after program finish

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.NAME, value="submit")
print(button.text)
print(button.size)
link = driver.find_element(By.ID, value="downloads")
downloads_link = link.find_element(By.TAG_NAME, "a")

# Get and print the text and href attributes of the <a> element
print("Text:", downloads_link.text)
print("Href Attribute:", downloads_link.get_attribute("href"))

code = driver.find_element(By.CLASS_NAME, value="comment")
print(code.text)

about_link = driver.find_element(By.XPATH, value='//*[@id="about"]/a')
print(about_link.get_attribute("href"))

all_name = driver.find_elements(By.CLASS_NAME)
print(all_name)

event_time = driver.find_elements_by_css_selector(".event-widget time")
event_name = driver.find_elements_by_css_selector(".event-widget li a")
events={}
for n in range(len(event_time)):
    events[n] = {
        'time':event_time[n].text,
        'name':event_name[n].text,

    }
print(events) #it's for selecting group of dates together at once n store in dictionary with event names

# driver.close()  #closes single tab where you open the page
driver.quit() #it quits the entire program









