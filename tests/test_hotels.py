from pages.login_page import LoginPage
from pages.hotels_page import HotelsPage
from utils.test_data import TestData
import time
import os


def test_hotel_booking(driver):

    # Step 0: Login
    login = LoginPage(driver)
    login.login(TestData.EMAIL, TestData.PASSWORD)

    # Wait for page to fully load after login
    time.sleep(3)

    # Step 1: Go to Hotels
    hotel = HotelsPage(driver)
    hotel.wait_for_clickable(hotel.HOTELS_MENU)
    hotel.go_to_hotels()
    hotel.wait_for_url_contains("hotels")

    # Step 2: Click Book Rooms on BeachFront Paradise
    hotel.select_hotel()
    hotel.wait_for_url_contains("booking-details")

    # Step 3: Fill Check In and Check Out dates
    hotel.fill_dates()

    # Step 4: Select Room Count - 1
    hotel.select_room_count()

    # Step 5: Continue Payment
    hotel.continue_payment()

    # Step 6: Wait for manual Razorpay payment (60 seconds)
    success = hotel.wait_for_manual_payment(timeout=60)

    # Step 7: Create screenshots folder if it does not exist
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Step 8: Take screenshot after booking-success confirmed
    current_url = driver.current_url
    print("Final URL: " + current_url)

    screenshot_path = os.path.join(screenshot_dir, "hotel_booking_success.png")
    driver.save_screenshot(screenshot_path)
    print("Screenshot saved: " + os.path.abspath(screenshot_path))

    # Step 9: Assert
    assert "booking-success" in current_url, "Hotel Booking FAILED - URL: " + current_url
    print("Hotel Booking PASSED")
