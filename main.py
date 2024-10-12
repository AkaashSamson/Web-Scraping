from selenium import webdriver
from selenium.webdriver.common.by import By

#to keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.amazon.in/Echo-Dot-5th-Gen-Alexa-smart-speaker/dp/B09B8XJDW5/ref=sr_1_1?crid=TPHMOX6BHVJU&dib=eyJ2IjoiMSJ9.oTYa296AD8YVM8t5jjE7M11tnmuMIRbZ0X0EaIm0WTDztwQsk1qf-QCy9Dm24r39L04jWBXccIZulVfxhRLT2Kl5jmP1xSOm7hjtDNdXwBFINuOqriC7wZ71Wq5dYdaLMvvMIlqcy_6wsjO6NTWxbtn5VJY4NDha7VSQt6dm-wWLQ_2w_VFtvoXBSlEwvQd6MOEiyO-GVXwFNFL3yeuGREI60uI-f2jxaYmr07jMPaI.nlFAko6xY0GnzYKnWshPX9TR5kUCP-jiic6kr-GXaNM&dib_tag=se&keywords=echo+dot&qid=1727511493&sprefix=echo+do%2Caps%2C920&sr=8-1")

price = driver.find_element(By.CLASS_NAME, "a-price-whole")

print(f"Price of the product is: {price.text}")

driver.quit()

