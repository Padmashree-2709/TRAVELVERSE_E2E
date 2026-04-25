from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.test_data import TestData
import time


class TrainsPage(BasePage):

    TRAINS_MENU = (By.XPATH, "//a[@href='/trains/']")
    BOOK_NOW = (By.XPATH, "(//button[contains(text(),'Book Now')])[1]")

    CLASS_SL = (By.XPATH, "//div[contains(@onclick,\"selectClass\") and .//h3[text()='SL']]")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    GENDER_FEMALE = (By.XPATH, "//div[@data-value='female']")
    DOB = (By.ID, "dobDateInput")

    NATIONALITY = (By.ID, "nationality")
    PHONE = (By.ID, "phone")
    EMAIL = (By.ID, "email")
    ADDRESS = (By.ID, "address")
    PINCODE = (By.ID, "pincode")
    PASSPORT = (By.ID, "passport")

    ADD_PASSENGER_BTN = (By.ID, "addPassengerBtn")
    CONTINUE_PAYMENT = (By.XPATH, "//button[contains(text(),'Continue Payment')]")

    def go_to_trains(self):
        self.wait_for_clickable(self.TRAINS_MENU)
        self.click(self.TRAINS_MENU)

    def select_train(self):
        self.click(self.BOOK_NOW)

    def select_class(self):
        self.click(self.CLASS_SL)

    def fill_passenger_details(self):
        self.send_keys(self.FIRST_NAME, TestData.FIRST_NAME)
        self.send_keys(self.LAST_NAME, TestData.LAST_NAME)
        self.click(self.GENDER_FEMALE)

        self.driver.execute_script("""
            var dob = document.getElementById('dobDateInput');
            dob.value = '2000-10-10';
            dob.dispatchEvent(new Event('change'));
            dob.dispatchEvent(new Event('input'));
        """)

        self.send_keys(self.NATIONALITY, "Indian")
        self.send_keys(self.PHONE, TestData.PHONE)
        self.send_keys(self.EMAIL, TestData.EMAIL_PASSENGER)
        self.send_keys(self.ADDRESS, "Chennai")
        self.send_keys(self.PINCODE, "600001")
        self.send_keys(self.PASSPORT, TestData.PASSPORT)

    def add_passenger(self):
        element = self.wait_for_element(self.ADD_PASSENGER_BTN)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        try:
            alert = self.driver.switch_to.alert
            print("Alert text: " + alert.text)
            alert.accept()
        except Exception:
            pass

        time.sleep(1)

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
