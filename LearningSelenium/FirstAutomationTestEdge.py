from selenium import webdriver
from selenium.webdriver.edge.service import Service


driver_service = Service(executable_path="C:\SeleniumWebDrivers\Edge(64bit)\msedgedriver.exe") #fixing DeprecationWarning
driver=webdriver.Edge(service=driver_service) #fixing DeprecationWarning


driver.get("https://www.rcvacademy.com")
driver.maximize_window()
print(driver.title)
driver.close()
