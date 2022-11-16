# Opening Browser with an URL and fetching the Title of the webpage
# fixed DeprecationWarning: executable_path has been deprecated selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_service = Service(executable_path="C:\SeleniumWebDrivers\Google Chrome(32bit)\chromedriver.exe") #fixing DeprecationWarning
#driver_service = Service(executable_path="ChromeDriverManager().install())
driver=webdriver.Chrome(service=driver_service) #fixing DeprecationWarning
#driver = webdriver.Chrome(executable_path="C:\SeleniumWebDrivers\Google Chrome(32bit)\chromedriver.exe")

driver.get("https://www.rcvacademy.com")
driver.maximize_window()
print(driver.title)
driver.close()