from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from utils.test_data import TestData
import time


class FlightsPage(BasePage):

    FLIGHTS_MENU = (By.XPATH, "//a[@href='/flights/']")
    BOOK_NOW = (By.XPATH, "(//button[contains(text(),'Book Now')])[1]")

    SEAT = (By.XPATH, "//div[@data-seat-number='E2']")
    ADD_PASSENGER_SEAT = (By.XPATH, "//button[contains(text(),'Add Passengers')]")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    GENDER_MALE = (By.XPATH, "//div[@data-value='male']")
    DOB = (By.ID, "dobDateInput")

    NATIONALITY = (By.ID, "nationality")
    PHONE = (By.ID, "phone")
    EMAIL = (By.ID, "email")
    ADDRESS = (By.ID, "address")
    PINCODE = (By.ID, "pincode")
    PASSPORT = (By.ID, "passport")

    MEAL = (By.ID, "meal")
    LUGGAGE = (By.ID, "luggage")

    ADD_PASSENGER_FORM = (By.ID, "addPassengerBtn")
    CONTINUE_PAYMENT = (By.XPATH, "//button[contains(text(),'Continue Payment')]")

    def go_to_flights(self):
        self.wait_for_clickable(self.FLIGHTS_MENU)
        self.click(self.FLIGHTS_MENU)

    def select_flight(self):
        self.click(self.BOOK_NOW)

    def select_seat(self):
        self.click(self.SEAT)

    def click_add_passenger_seat(self):
        self.click(self.ADD_PASSENGER_SEAT)

    def fill_passenger_details(self):
        self.send_keys(self.FIRST_NAME, TestData.FIRST_NAME)
        self.send_keys(self.LAST_NAME, TestData.LAST_NAME)
        self.click(self.GENDER_MALE)

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

        Select(self.wait_for_element(self.MEAL)).select_by_value("non_veg")
        Select(self.wait_for_element(self.LUGGAGE)).select_by_value("checkin")

    def add_passenger(self):
        element = self.wait_for_element(self.ADD_PASSENGER_FORM)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        try:
            alert = self.driver.switch_to.alert
            print("Alert text:", alert.text)
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
                # Wait 2 more seconds for the page to fully render
                time.sleep(2)
                print("Booking success page loaded at " + str(i + 1) + " seconds.")
                return True
            time.sleep(1)

        return False
