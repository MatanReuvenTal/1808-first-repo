from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Users\matan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.github.com")
input("Press enter to continue...")
