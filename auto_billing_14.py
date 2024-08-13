import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# get window handle has three functions: driver.current_window_handle, driver.window_handles, driver.switch_to.window(handle)
driver = webdriver.Chrome('chromedriver-win64\chromedriver.exe')
driver.get('http://127.0.0.1:5500/script_14.html')
sleep(10)
driver.implicitly_wait(10)
# get current window handle
current_handle = driver.current_window_handle
screenshot_path = "./test/sc1.png"
driver.save_screenshot(screenshot_path)
print(f'current window handle is : {current_handle}')
sleep(10)

handles = driver.window_handles
# as window handles in the list reflects the open time order, the later opened, the index is bigger
# if just wanna to switch to the latest window handle can use
# driver.switch_to.window(handles[-1])
for handle in handles:
    sleep(3)
    if handle != current_handle:
        driver.switch_to.window(handle)
        break

sleep(3)
