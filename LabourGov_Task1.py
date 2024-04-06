from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class LabourGov:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()

    def maximize_start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)

    def documents(self):
        action = ActionChains(self.driver)
        documents = self.driver.find_element(By.LINK_TEXT,"Documents")
        action.move_to_element(documents).perform()
        time.sleep(3)

    def monthly_progress_report(self):
        self.driver.find_element(By.LINK_TEXT, "Monthly Progress Report").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Download(221.53 KB)')]").click()
        time.sleep(5)
        try:
            webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        except:
            print("Not able to inspect OK button")

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    url = "https://labour.gov.in/"
    labourgov = LabourGov(url)
    labourgov.maximize_start()
    labourgov.documents()
    labourgov.monthly_progress_report()
    labourgov.close()