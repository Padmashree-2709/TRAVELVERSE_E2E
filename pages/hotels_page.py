from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base.base_page import BasePage
import time


class HotelsPage(BasePage):

    HOTELS_MENU = (By.XPATH, "//a[@href='/hotels/']")
    BOOK_ROOMS = (By.XPATH, "(//button[contains(@class,'btn-book')])[1]")

    CHECKIN = (By.ID, "checkinDateInput")
    CHECKOUT = (By.ID, "checkoutDateInput")

    ROOM_COUNT = (By.ID, "room_count")
    CONTINUE_PAYMENT = (By.XPATH, "//button[contains(text(),'Continue Payment')]")

    def go_to_hotels(self):
        self.wait_for_clickable(self.HOTELS_MENU)
        self.click(self.HOTELS_MENU)

    def select_hotel(self):
        element = self.wait_for_element(self.BOOK_ROOMS)
        self.driver.execute_script("arguments[0].click();", element)

    def fill_dates(self):
        # Set Check In date using JavaScript same as flights/trains/bus
        self.driver.execute_script("""
            var checkin = document.getElementById('checkinDateInput');
            checkin.value = '2026-05-01';
            checkin.dispatchEvent(new Event('change'));
            checkin.dispatchEvent(new Event('input'));
        """)
        time.sleep(1)

        # Set Check Out date using JavaScript
        self.driver.execute_script("""
            var checkout = document.getElementById('checkoutDateInput');
            checkout.value = '2026-05-03';
            checkout.dispatchEvent(new Event('change'));
            checkout.dispatchEvent(new Event('input'));
        """)
        time.sleep(1)

    def select_room_count(self):
        select = Select(self.wait_for_element(self.ROOM_COUNT))
        select.select_by_value("1")

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
