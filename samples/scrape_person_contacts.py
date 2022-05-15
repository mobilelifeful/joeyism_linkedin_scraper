import os
from linkedin_scraper import Person, actions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=chrome_options)

email = os.getenv("LINKEDIN_USER")
password = os.getenv("LINKEDIN_PASSWORD")
actions.login(driver,'maxfield@gmail.com','080819') # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/maxfield-parker-4aa95610a/", driver=driver)
#person = Person("https://www.linkedin.com/in/maxfield-parker-4aa95610a/", driver=driver)

#print("Person: " + person)
print(type(person.c))
