from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

url = "https://www.billa.at/search/results?category=&searchTerm=bier"

options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)
driver.get(url)


print(driver.title)

assert "BILLA" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source



driver.close()



