from pages.login_page import LoginPage
from utils.test_data import TestData
from selenium.webdriver.common.by import By
import time
import os


def test_logout(driver):

    # Step 0: Login first
    login = LoginPage(driver)
    login.login(TestData.EMAIL, TestData.PASSWORD)

    # Wait for page to fully load after login
    time.sleep(3)

    # Step 1: Click Logout
    logout_btn = driver.find_element(By.XPATH, "//a[@href='/users/user_logout/']")
    logout_btn.click()

    # Step 2: Wait for page to load after logout
    time.sleep(2)

    # Step 3: Create screenshots folder if it does not exist
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Step 4: Take screenshot
    screenshot_path = os.path.join(screenshot_dir, "logout_success.png")
    driver.save_screenshot(screenshot_path)
    print("Screenshot saved: " + os.path.abspath(screenshot_path))

    # Step 5: Verify logout - home page loads and login button is visible
    current_url = driver.current_url
    print("Final URL: " + current_url)

    # After logout redirects to home page - verify Logout button is gone
    assert "user_logout" not in current_url, "Logout FAILED - URL: " + current_url
    assert "Logout" not in driver.page_source or "login" in driver.page_source.lower(), "Logout FAILED"
    print("Logout PASSED")
