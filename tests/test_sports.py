from pages.login_page import LoginPage
from pages.sports_page import SportsPage
from utils.test_data import TestData
import time
import os


def test_sport_booking(driver):

    # Step 0: Login
    login = LoginPage(driver)
    login.login(TestData.EMAIL, TestData.PASSWORD)

    # Wait for page to fully load after login
    time.sleep(3)

    # Step 1: Go to Sports
    sport = SportsPage(driver)
    sport.wait_for_clickable(sport.SPORTS_MENU)
    sport.go_to_sports()
    sport.wait_for_url_contains("sports")

    # Step 2: Click Book Ticket on Premium Foot Ball League
    sport.select_sport()
    sport.wait_for_url_contains("booking-details")

    # Step 3: Select Ticket Count - 2
    sport.select_ticket_count()

    # Step 4: Continue Payment
    sport.continue_payment()

    # Step 5: Wait for manual Razorpay payment (60 seconds)
    success = sport.wait_for_manual_payment(timeout=60)

    # Step 6: Create screenshots folder if it does not exist
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Step 7: Take screenshot after booking-success confirmed
    current_url = driver.current_url
    print("Final URL: " + current_url)

    screenshot_path = os.path.join(screenshot_dir, "sport_booking_success.png")
    driver.save_screenshot(screenshot_path)
    print("Screenshot saved: " + os.path.abspath(screenshot_path))

    # Step 8: Assert
    assert "booking-success" in current_url, "Sport Booking FAILED - URL: " + current_url
    print("Sport Booking PASSED")
