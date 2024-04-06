from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests

# Initialize the webdriver
driver = webdriver.Firefox()

# Maximize window
driver.maximize_window()

# Get the specified url
driver.get("https://labour.gov.in/")

# Clicking the elements to reach the photo gallery
driver.find_element(By.LINK_TEXT,"Media").click()
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Click for more info of Press Releases").click()
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Photo Gallery").click()
time.sleep(3)

# Get the handles
window_handles = driver.window_handles
driver.switch_to.window(driver.window_handles[1])

# Path where you want to save the downloaded pictures
download_path = 'C:\\Ramya\\Workspace\\Python\\Tasks\\Task-20_30Mar24\\Pictures'

# Create download directory if it doesn't exist
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Find the photo elements and store in object picture_elements
picture_elements = driver.find_elements(By.XPATH,
                                        '//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody//div/img')

# Counter to keep track of downloaded pictures
downloaded_count = 0

# Iterate through the picture elements
for num, picture_element in enumerate(picture_elements):
    # Get the URL of the picture
    picture_url = picture_element.get_attribute('src')

    # Skip if no URL found
    if not picture_url:
        continue

    # Download the picture
    response = requests.get(picture_url)

    # Save the picture to disk
    with open(f'{download_path}/picture_{num}.jpg', 'wb') as file:
        file.write(response.content)

    # Increment downloaded count
    downloaded_count += 1

    # Break loop if 10 pictures have been downloaded
    if downloaded_count >= 10:
        break

# Close the WebDriver
driver.quit()
