from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

service = webdriver.chrome.service.Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://uni.tsu.ge/login?returnUrl=%2F')
driver.maximize_window()

wait = WebDriverWait(driver, 10)
try:
    wait.until(ec.title_contains("TSU - Student Portal"))
except Exception as e:
    print(f"Error waiting for title: {e}")

try:
    user = driver.find_element(By.XPATH, "//input[@type='text']")
    password = driver.find_element(By.XPATH, "//input[@type='password']")
    button = driver.find_element(By.XPATH, "//button[@class='btn btn-custom btn-lg btn-block mt-3 login-button']")

    # enter your lms login
    user.send_keys('')
    password.send_keys('')
    time.sleep(2)
    button.click()
except Exception as e:
    print(f"Error interacting with input fields using JavaScript: {e}")

time.sleep(1)
close_button = wait.until(ec.presence_of_element_located((By.XPATH, "//button[@class='mdc-button mat-mdc-button _mat-animation-noopable mat-unthemed mat-mdc-button-base']")))
time.sleep(1)

close_button.click()
time.sleep(1)

i = 1
while i < 13:
    butt = wait.until(ec.element_to_be_clickable((By.XPATH, f"(//button[@class='btn btn-outline-primary btn-borderNone'])[{i}]")))
    driver.execute_script("arguments[0].scrollIntoView();", butt)
    time.sleep(1)  # Add a short delay
    butt.click()
    time.sleep(1)

    t = True
    try:
        k = 1
        while t:
            agree = wait.until(ec.presence_of_element_located((By.XPATH, f"(//input[@value='23'])[{k}]")))
            driver.execute_script("window.scrollBy(0, 100);")
            if agree:
                # if not agree.is_selected():
                time.sleep(1)
                agree.click()
            else:
                t = False
                break
            k += 1
    except Exception as e:
        if "unexpected alert open" in str(e):
            alert = driver.switch_to.alert
            print(f"Alert Text: {alert.text}")
            alert.accept()
        else:
            print(f"Exception: {e}")
    finally:
        often = wait.until(ec.presence_of_element_located((By.XPATH, "//input[@value='26']")))
        time.sleep(1)
        often.click()
        driver.execute_script("window.scrollBy(0, 100);")
        try:
            yes = wait.until(ec.presence_of_element_located((By.XPATH, "//input[@value='31']")))
            time.sleep(1)
            yes.click()
        except Exception as e:
            if "unexpected alert open" in str(e):
                alert = driver.switch_to.alert
                print(f"Alert Text: {alert.text}")
                alert.accept()
            else:
                print(f"Exception: {e}")
        finally:
            driver.execute_script("window.scrollBy(0, 200);")
            finish_locator = (By.CSS_SELECTOR, "button.btn.btn-primary")
            finish = wait.until(ec.element_to_be_clickable(finish_locator))
            time.sleep(1)
            finish.click()
            time.sleep(3)
            alert = wait.until(ec.alert_is_present())
            alert.accept()
            time.sleep(1)

    i += 1

time.sleep(50)
driver.quit()
