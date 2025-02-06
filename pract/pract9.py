# import selenium
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# driver = selenium.webdriver.Chrome('../chromedriver-win64/chromedriver.exe')
# driver.get('http://127.0.0.1:5500/script_9.html')
# driver.maximize_window()
#
# wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
# alert_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[value="alert"]')))
# alert_btn.click()
# time.sleep(2)
# alert = driver.switch_to.alert
# print(alert.text)
# alert.dismiss()
#
#
#
# select = Select(driver.find_element(By.CSS_SELECTOR, '.meter-test'))
# select.select_by_index(0)
# opt1 = select.first_selected_option
# print(opt1.get_attribute('value'))
#
# select.select_by_value('1310')
# opt2 = select.first_selected_option
# print(opt2.text)
#
# time.sleep(2)
#
# js = "window.scrollTo(0, 2000)"
# driver.execute_script(js)
# time.sleep(2)
#
# actions = ActionChains(driver)
# actions.click_and_hold(driver.find_element(By.CSS_SELECTOR, ".hidden-button"))
# time.sleep(2)
#
#
# driver.quit()

dict = {'name': "aculink810", "physical": True, "reading": 100}
keys = tuple(dict.keys())
values = tuple(dict.values())
print(keys, values)