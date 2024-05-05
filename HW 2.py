from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def run_test_case():
    # get the path to the ChromeDriver executable
    driver_path = ChromeDriverManager().install()

    # create a new Chrome browser instance
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # open the url
    driver.get('https://https://www.amazon.com/ap/signin/ref=cart_empty_sign_in?openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fcart%3Fapp-nav-type%3Dnone%26dc%3Ddf&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

    # Amazon logo
    driver.find_element(By.XPATH, value="//class[@aria-label='Amazon']")
    # Email field
    driver.find_element(By.XPATH, value="//input[@type='email']")
    # Continue button
    driver.find_element(By.XPATH, value="//input[@id='continue']")
    # Conditons of use
    driver.find_element(By.XPATH, value="//a[text()='Conditions of Use']")
    # Privacy link
    driver.find_element(By.XPATH, value="//a[text()='Privacy Notice']")
    # Need help link
    driver.find_element(By.XPATH, value="//span[contains(text(),'Need help?')]")
    # Forgot password
    driver.find_element(By.XPATH, value="//a[contains(text(),'Forgot your password?')]")
    # Other issues with Sign-In
    driver.find_element(By.XPATH, value="//a[contains(text(),'Other issues with Sign-In')]")
    # Create your Amazon account
    driver.find_element(By.XPATH, value="////a[@id='createAccountSubmit']")


if __name__ == "__main__":
    run_test_case()
