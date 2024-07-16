import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = selenium.webdriver.Chrome('./chromedriver-win64/chromedriver.exe')
driver.get('https://dev.acucloud.accuenergy.com')
driver.implicitly_wait(10)
driver.set_window_size(400, 800)
sleep(1)

driver.set_window_position(1000, 1000)
sleep(1)

driver.maximize_window()


wait = WebDriverWait(driver,10)
usr = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
pwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
sbt = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))

usr.send_keys('nacun.liu@accuenergy.com')
sleep(1)
pwd.send_keys('Toz13547')
sleep(1)


usr.send_keys(Keys.CONTROL, "a")
usr.send_keys(Keys.CONTROL, "c")
sleep(2)
usr.send_keys(Keys.DELETE)
sleep(2)
usr.send_keys(Keys.CONTROL, "V")
sleep(2)

sbt.click()

# sleep(10)
# alert = driver.find_element(By.XPATH, '//span[text()="Cancel"]')
# alert.click()
sleep(10)
#
# analysis = driver.find_element(By.CSS_SELECTOR, '.ant-menu-vertical li:nth-child(4)')
# analysis.click()
# sleep(3)

js = "alert('test driver.execute_script() success')"
driver.execute_script(js)
sleep(3)

at = driver.switch_to.alert
at.dismiss()
sleep(3)

driver.close()

