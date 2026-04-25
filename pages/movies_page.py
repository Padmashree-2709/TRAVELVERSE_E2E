from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base.base_page import BasePage
import time


class MoviesPage(BasePage):

    MOVIES_MENU = (By.XPATH, "//a[@href='/movies/']")

    BOOK_NOW = (By.XPATH, "(//div[@class='movie-card'])[1]//button[@class='book-btn']")

    CITY_SELECT = (By.ID, "citySelect")
    CONTINUE_BTN = (By.XPATH, "//button[contains(@onclick,'confirmCity')]")

    SHOW_TIME = (By.XPATH, "//span[@class='show-time' and contains(text(),'12:30 PM')]")

    SEAT_A1 = (By.XPATH, "//div[@data-seat-number='A1']")
    BOOK_TICKET_BTN = (By.XPATH, "//button[@type='submit' and contains(text(),'Book Ticket')]")

    CONTINUE_PAYMENT = (By.XPATH, "//button[contains(text(),'Continue Payment')]")

    def go_to_movies(self):
        self.wait_for_clickable(self.MOVIES_MENU)
        self.click(self.MOVIES_MENU)

    def select_movie(self):
        # Book Now is hidden inside overlay - click directly via JavaScript
        element = self.wait_for_element(self.BOOK_NOW)
        self.driver.execute_script("arguments[0].click();", element)

    def select_city(self):
        select = Select(self.wait_for_element(self.CITY_SELECT))
        select.select_by_value("2")
        self.click(self.CONTINUE_BTN)

    def select_show_time(self):
        self.click(self.SHOW_TIME)

    def select_seat(self):
        self.click(self.SEAT_A1)

    def click_book_ticket(self):
        self.click(self.BOOK_TICKET_BTN)

    def continue_payment(self):
        self.click(self.CONTINUE_PAYMENT)

    def wait_for_manual_payment(self, timeout=60):
        print("")
        print("Razorpay is open. Complete the payment manually.")
        print("Waiting up to " + str(timeout) + " seconds for booking-success page...")
        print("")

        for i in range(timeout):
            current_url = self.driver.current_url
            if "booking-success" in current_url:
                time.sleep(2)
                print("Booking success page loaded at " + str(i + 1) + " seconds.")
                return True
            time.sleep(1)

        return False
