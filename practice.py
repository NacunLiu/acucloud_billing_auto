import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = selenium.webdriver.Chrome('chromedriver-win64/chromedriver.exe')
driver.get('http://127.0.0.1:5500/script_9.html')
driver.maximize_window()
wait = WebDriverWait(driver, 10, 0.5)

actions = ActionChains(driver)
# actions.context_click()
# time.sleep(2)
# actions.double_click()

button_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='alert']")))
# actions.move_to_element(button_alert).perform()
# actions.click(button_alert).perform()
button_alert.click()
time.sleep(2)
alert = driver.switch_to.alert
time.sleep(2)
alert.dismiss()
time.sleep(2)

prompt_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='prompt']")))
prompt_button.click()
time.sleep(2)
pt = driver.switch_to.alert
time.sleep(2)
print(pt.text)
pt.accept()

js="window.scrollTo(0, 2000)"
driver.execute_script(js)
time.sleep(2)
actions.click_and_hold(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".hidden-button")))).perform()
time.sleep(2)
actions.release().perform()
time.sleep(2)

driver.switch_to.frame('reg')
f_user = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
f_login = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")


driver.quit()



