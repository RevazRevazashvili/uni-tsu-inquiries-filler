from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # enter your lms login
    user.send_keys('')
    password.send_keys('')
    time.sleep(2)
    button.click()
except Exception as e:
    print(f"Error interacting with input fields using JavaScript: {e}")

time.sleep(1)
close_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='mdc-button mat-mdc-button _mat-animation-noopable mat-unthemed mat-mdc-button-base']")))
time.sleep(1)

close_button.click()
time.sleep(1)

i = 1
while i < 13:
    butt = wait.until(EC.presence_of_element_located((By.XPATH, f"(//button[@class='btn btn-outline-primary btn-borderNone'])[{i}]")))
    time.sleep(1)
    butt.click()
    time.sleep(1)

    t = True
    try:
        k = 1
        while t:
            agree = wait.until(EC.presence_of_element_located((By.XPATH, f"(//input[@value='23'])[{k}]")))
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
        # try:
        often = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='26']")))
        time.sleep(1)
        often.click()
        driver.execute_script("window.scrollBy(0, 150);")
        if not wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='31']"))):
            try:
                yes = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='31']")))
                time.sleep(1)
                yes.click()
            except Exception as e:
                if "unexpected alert open" in str(e):
                    alert = driver.switch_to.alert
                    print(f"Alert Text: {alert.text}")
                    alert.accept()
                    print("hello")
                else:
                    print(f"Exception: {e}")
            finally:
                driver.execute_script("window.scrollBy(0, 200);")
                finish = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']")))
                time.sleep(1)
                finish.click()
                time.sleep(3)
                alert = wait.until(EC.alert_is_present())
                alert.accept()
                time.sleep(1)
        else:
            try:
                raise TimeoutError
            except Exception as e:
                if "unexpected alert open" in str(e):
                    alert = driver.switch_to.alert
                    print(f"Alert Text: {alert.text}")
                    alert.accept()
                    print("hello")
                else:
                    print(f"Exception: {e}")
            finally:
                driver.execute_script("window.scrollBy(0, 200);")
                finish = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']")))
                time.sleep(1)
                finish.click()
                time.sleep(3)
                alert = wait.until(EC.alert_is_present())
                alert.accept()
                time.sleep(1)


        # if not wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='31']"))):
        # time.sleep(3)
        # driver.switch_to.alert.accept()

        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 200);")
        finish = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']")))
        time.sleep(1)
        finish.click()
        time.sleep(3)
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(1)
        # else:
        #     time.sleep(1)
        #     driver.execute_script("window.scrollBy(0, 200);")
        #     finish = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']")))
        #     time.sleep(1)
        #     finish.click()
        #     time.sleep(3)
        #     alert = wait.until(EC.alert_is_present())
        #     alert.accept()
        #     time.sleep(1)
        # except Exception as e:
        #     if "unexpected alert open" in str(e):
        #         alert = driver.switch_to.alert
        #         print(f"Alert Text: {alert.text}")
        #         alert.accept()
        #     else:
        #         print(f"Exception: {e}")
    i += 1

time.sleep(50)
driver.quit()