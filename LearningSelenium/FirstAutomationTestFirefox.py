from selenium import webdriver
from selenium.webdriver.firefox.service import Service

#driver = webdriver.Firefox(executable_path="C:\SeleniumWebDrivers\Firefox(32bit)\geckodriver.exe")


driver_service = Service(executable_path="C:\SeleniumWebDrivers\Firefox(32bit)\geckodriver.exe") #fixing DeprecationWarning
driver=webdriver.Firefox(service=driver_service) #fixing DeprecationWarning


driver.get("https://www.rcvacademy.com")
driver.maximize_window()
print(driver.title)
driver.close()
