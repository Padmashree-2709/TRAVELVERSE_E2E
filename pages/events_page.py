from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base.base_page import BasePage
import time


class EventsPage(BasePage):

    EVENTS_MENU = (By.XPATH, "//a[@href='/events/']")
    BOOK_TICKET = (By.XPATH, "(//button[contains(@class,'btn-book')])[1]")

    TICKET_COUNT = (By.ID, "ticket_count")
    CONTINUE_PAYMENT = (By.XPATH, "//button[contains(text(),'Continue Payment')]")

    def go_to_events(self):
        self.wait_for_clickable(self.EVENTS_MENU)
        self.click(self.EVENTS_MENU)

    def select_event(self):
        # Book Ticket button - click via JavaScript
        element = self.wait_for_element(self.BOOK_TICKET)
        self.driver.execute_script("arguments[0].click();", element)

    def select_ticket_count(self):
        select = Select(self.wait_for_element(self.TICKET_COUNT))
        select.select_by_value("2")

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
