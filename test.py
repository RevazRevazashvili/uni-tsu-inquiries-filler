from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Add this line
from selenium.webdriver.common.alert import Alert
import time


service = webdriver.chrome.service.Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://uni.tsu.ge/login?returnUrl=%2F')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.title_contains("TSU - Student Portal"))
except Exception as e:
    print(f"Error waiting for title: {e}")

try:
    user = driver.find_element(By.XPATH, "//input[@type='text']")
    password = driver.find_element(By.XPATH, "//input[@type='password']")
    button = driver.find_element(By.XPATH, "//button[@class='btn btn-custom btn-lg btn-block mt-3 login-button']")

    user.send_keys('59401133380')
    password.send_keys('rezo2001')
    button.click()
except Exception as e:
    print(f"Error interacting with input fields using JavaScript: {e}")

try:
    close_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='mdc-button mat-mdc-button _mat-animation-noopable mat-unthemed mat-mdc-button-base']")))
    close_button.click()
except Exception as e:
    print(f"Error closing the popup: {e}")

i = 1
while i < 13:
    butt = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//button[@class='btn btn-outline-primary btn-borderNone'])[{i}]")))
    butt.click()

    k = 1
    while True:
        try:
            agree = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//input[@value='23'])[{k}]")))
            driver.execute_script("window.scrollBy(0, 100);")
            agree.click()
            k += 1
        except EC.TimeoutException:
            break
        except Exception as e:
            print(f"Exception while agreeing: {e}")

    often = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='26']")))
    often.click()
    driver.execute_script("window.scrollBy(0, 150);")

    try:
        yes = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='31']")))
        yes.click()
    except EC.TimeoutException:
        pass
    except Exception as e:
        print(f"Exception while clicking 'Yes': {e}")

    driver.execute_script("window.scrollBy(0, 200);")

    finish = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
    finish.click()

    try:
        alert = wait.until(EC.alert_is_present())
        alert.accept()
    except EC.TimeoutException:
        pass
    except Exception as e:
        print(f"Exception while handling alert: {e}")

    i += 1

time.sleep(50)
driver.quit()
