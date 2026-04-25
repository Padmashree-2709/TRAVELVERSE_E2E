from pages.login_page import LoginPage
from utils.test_data import TestData
import os


def test_login(driver):

    # Step 1: Login
    login = LoginPage(driver)
    login.login(TestData.EMAIL, TestData.PASSWORD)

    # Step 2: Wait for page to load after login
    import time
    time.sleep(3)

    # Step 3: Create screenshots folder if it does not exist
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Step 4: Take screenshot
    screenshot_path = os.path.join(screenshot_dir, "login_success.png")
    driver.save_screenshot(screenshot_path)
    print("Screenshot saved: " + os.path.abspath(screenshot_path))

    # Step 5: Verify login success
    current_url = driver.current_url
    print("Final URL: " + current_url)

    assert "Invalid" not in driver.page_source, "Login FAILED - Invalid credentials"
    print("Login PASSED")
