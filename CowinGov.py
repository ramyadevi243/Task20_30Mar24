from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Created a class called CowinGov
class CowinGov:
    # Calling constructor with parameter url
    def __init__(self, url):
        self.url = url
        # Initializing Firefox
        self.driver = webdriver.Firefox()

    # Created a method for maximizing and getting specified url
    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)

    # Find and click on the "FAQ" link
    def faq_link(self):
        faq = self.driver.find_element(By.XPATH, "//a[contains(text(), 'FAQ')]")
        faq.click()
        time.sleep(3)

    def partner_link(self):
        # Find and click on the "Partners" link
        partners = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Partners')]")
        partners.click()
        time.sleep(3)

    # Get window handles for all open windows
    def window_handles(self):
        window_handles = self.driver.window_handles
        print("Window/Frame IDs:")
        for handle in window_handles:
            print(handle)

    # Close the newly opened windows and switch back to the original window
    def close_new_windows(self):
        window_handles = self.driver.window_handles
        for handle in window_handles[1:]:
            self.driver.switch_to.window(handle)
            self.driver.close()

# Executing the main method and calling all defined methods
if __name__ == "__main__":
    url = "https://www.cowin.gov.in/"
    cowin = CowinGov(url)
    cowin.start()
    cowin.faq_link()
    cowin.partner_link()
    cowin.window_handles()
    cowin.close_new_windows()

