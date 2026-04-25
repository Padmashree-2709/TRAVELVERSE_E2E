from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def send_keys(self, locator, value):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(value)

    def wait_for_url_contains(self, text):
        self.wait.until(lambda driver: text in driver.current_url)
