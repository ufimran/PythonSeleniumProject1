
#Mozilla Working
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#google chrome not working
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.rcvacademy.com")
driver.maximize_window()
print(driver.title)
driver.close()



