from pages.login_page import LoginPage
from pages.flights_page import FlightsPage
from utils.test_data import TestData
import os


def test_flight_booking(driver):

    # Step 0: Login
    login = LoginPage(driver)
    login.login(TestData.EMAIL, TestData.PASSWORD)

    # Step 1: Go to Flights
    flight = FlightsPage(driver)
    flight.wait_for_clickable(flight.FLIGHTS_MENU)
    flight.go_to_flights()
    flight.wait_for_url_contains("flights")

    # Step 2: Select Flight
    flight.select_flight()
    flight.wait_for_url_contains("seat")

    # Step 3: Seat Selection
    flight.select_seat()

    # Step 4: Open Passenger Form
    flight.click_add_passenger_seat()
    flight.wait_for_url_contains("passenger")

    # Step 5: Fill Passenger Details
    flight.fill_passenger_details()

    # Step 6: Add Passenger
    flight.add_passenger()

    # Step 7: Continue Payment
    flight.continue_payment()

    # Step 8: Wait for manual Razorpay payment (60 seconds)
    success = flight.wait_for_manual_payment(timeout=60)

    # Step 9: Create screenshots folder if it does not exist
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Step 10: Only after booking-success URL is confirmed, take screenshot
    current_url = driver.current_url
    print("Final URL: " + current_url)

    screenshot_path = os.path.join(screenshot_dir, "booking_success.png")
    driver.save_screenshot(screenshot_path)
    print("Screenshot saved: " + os.path.abspath(screenshot_path))

    # Step 11: Assert
    assert "booking-success" in current_url, "Booking FAILED - URL: " + current_url
    print("Flight Booking PASSED")
