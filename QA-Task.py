from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options) 
driver.get("https://app.jubelio.com/login")

element = driver.find_element(By.NAME, "email")
element.clear()
element.send_keys("qa.rakamin.jubelio@gmail.com")

element_pass = driver.find_element(By.NAME, "password")
element_pass.clear()
element_pass.send_keys("Jubelio1223!")

driver.find_element(By.CSS_SELECTOR, "span.ladda-label").click()

driver.implicitly_wait(15)

try:
    driver.find_element(By.XPATH, "//span[contains(text(),'Dashboard')]")

    print("Login successful!")
    driver.quit()

except Exception as e:
    print("Error during login:", str(e))
    driver.quit()