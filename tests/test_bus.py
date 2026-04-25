from pages.login_page import LoginPage
from pages.bus_page import BusPage
from utils.test_data import TestData
import os


def test_bus_booking(driver):

    # Step 0: Login
    login = LoginPage(driver)
    login.login(TestData.EMAIL, TestData.PASSWORD)

    # Step 1: Go to Buses
    bus = BusPage(driver)
    bus.wait_for_clickable(bus.BUS_MENU)
    bus.go_to_buses()
    bus.wait_for_url_contains("buses")

    # Step 2: Select Bus
    bus.select_bus()
    bus.wait_for_url_contains("seat-selection")

    # Step 3: Select Seat A2
    bus.select_seat()

    # Step 4: Click Add Passengers button on seat selection page
    bus.click_add_passengers()
    bus.wait_for_url_contains("passenger")

    # Step 5: Fill Passenger Details
    bus.fill_passenger_details()

    # Step 6: Add Passenger
    bus.add_passenger()

    # Step 7: Continue Payment
    bus.continue_payment()

    # Step 8: Wait for manual Razorpay payment (60 seconds)
    success = bus.wait_for_manual_payment(timeout=60)

    # Step 9: Create screenshots folder if it does not exist
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Step 10: Take screenshot after booking-success confirmed
    current_url = driver.current_url
    print("Final URL: " + current_url)

    screenshot_path = os.path.join(screenshot_dir, "bus_booking_success.png")
    driver.save_screenshot(screenshot_path)
    print("Screenshot saved: " + os.path.abspath(screenshot_path))

    # Step 11: Assert
    assert "booking-success" in current_url, "Bus Booking FAILED - URL: " + current_url
    print("Bus Booking PASSED")
