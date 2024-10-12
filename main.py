from selenium import webdriver
from selenium.webdriver.common.by import By

#to keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")

# print(f"Price of the product is: {price.text}")

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))
print(driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a").text)

driver.quit()

