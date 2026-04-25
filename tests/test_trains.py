from pages.login_page import LoginPage
from pages.trains_page import TrainsPage
from utils.test_data import TestData
import os


def test_train_booking(driver):

    # Step 0: Login
    login = LoginPage(driver)
    login.login(TestData.EMAIL, TestData.PASSWORD)

    # Step 1: Go to Trains
    train = TrainsPage(driver)
    train.wait_for_clickable(train.TRAINS_MENU)
    train.go_to_trains()
    train.wait_for_url_contains("trains")

    # Step 2: Select Train
    train.select_train()
    train.wait_for_url_contains("class-selection")

    # Step 3: Select Class SL
    train.select_class()
    train.wait_for_url_contains("passenger")

    # Step 4: Fill Passenger Details
    train.fill_passenger_details()

    # Step 5: Add Passenger
    train.add_passenger()

    # Step 6: Continue Payment
    train.continue_payment()

    # Step 7: Wait for manual Razorpay payment (60 seconds)
    success = train.wait_for_manual_payment(timeout=60)

    # Step 8: Create screenshots folder if it does not exist
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Step 9: Take screenshot after booking-success confirmed
    current_url = driver.current_url
    print("Final URL: " + current_url)

    screenshot_path = os.path.join(screenshot_dir, "train_booking_success.png")
    driver.save_screenshot(screenshot_path)
    print("Screenshot saved: " + os.path.abspath(screenshot_path))

    # Step 10: Assert
    assert "booking-success" in current_url, "Train Booking FAILED - URL: " + current_url
    print("Train Booking PASSED")
