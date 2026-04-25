from pages.login_page import LoginPage
from pages.movies_page import MoviesPage
from utils.test_data import TestData
import time
import os


def test_movie_booking(driver):

    # Step 0: Login
    login = LoginPage(driver)
    login.login(TestData.EMAIL, TestData.PASSWORD)

    # Wait for page to fully load after login
    time.sleep(3)

    # Step 1: Go to Movies
    movie = MoviesPage(driver)
    movie.wait_for_clickable(movie.MOVIES_MENU)
    movie.go_to_movies()
    movie.wait_for_url_contains("movies")

    # Step 2: Select DNA movie - click Book Now
    movie.select_movie()
    movie.wait_for_url_contains("show-selection")

    # Step 3: Select City - Madurai
    movie.select_city()

    # Step 4: Select Show Time - 12:30 PM
    movie.select_show_time()
    movie.wait_for_url_contains("seat-selection")

    # Step 5: Select Seat A1
    movie.select_seat()

    # Step 6: Click Book Ticket
    movie.click_book_ticket()
    movie.wait_for_url_contains("booking")

    # Step 7: Continue Payment
    movie.continue_payment()

    # Step 8: Wait for manual Razorpay payment (60 seconds)
    success = movie.wait_for_manual_payment(timeout=60)

    # Step 9: Create screenshots folder if it does not exist
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Step 10: Take screenshot after booking-success confirmed
    current_url = driver.current_url
    print("Final URL: " + current_url)

    screenshot_path = os.path.join(screenshot_dir, "movie_booking_success.png")
    driver.save_screenshot(screenshot_path)
    print("Screenshot saved: " + os.path.abspath(screenshot_path))

    # Step 11: Assert
    assert "booking-success" in current_url, "Movie Booking FAILED - URL: " + current_url
    print("Movie Booking PASSED")
