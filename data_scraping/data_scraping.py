import os
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time

# Step 1 - Find search bar, enter term "kuala lumpur", then activate search
url = "https://subway.com.my/find-a-subway"
# cService = webdriver.ChromeService(executable_path=r"D:\Repos\mindhive-opening\data_scraping")
driver = webdriver.Chrome()
search_term = "kuala lumpur"
# Entering search term before scraping
driver.get(url)
search_bar = driver.find_element(By.ID, 'fp_searchAddress')
search_bar.send_keys(search_term)
search_bar.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 10) # Timeout as search takes time

# Registering data into dataframe
entries = []

list = None
try:
    list = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'fp_listitem')]")))
    print("Ready")
except Exception as e:
    print("Timeout error: ${e}")


i = 0
for item in list:
    # print(item.get_attribute("data-latitude"))
    name = item.find_element(By.TAG_NAME, "h4").get_attribute("textContent")
    print(name)
    address = item.find_element(By.XPATH, ".//div[@class='location_left']/div[@class='infoboxcontent']/p").get_attribute("textContent")
    operating_hours = ""
    try:
        operating_hours = item.find_element(By.XPATH, ".//div[@class='infoboxcontent']/p[3]").get_attribute("textContent")
        operating_hours_2 = item.find_element(By.XPATH, ".//div[@class='infoboxcontent']/p[4]").get_attribute("textContent")
        if operating_hours != "":
            operating_hours = operating_hours + "; " + operating_hours_2
    except:
        pass
    waze_link = item.find_element(By.XPATH, ".//div[@class='directionButton']/a[2]").get_attribute("href")
    latitude = item.get_attribute("data-latitude")
    longitude = item.get_attribute("data-longitude")
    entries.append({
        "name": name,
        "address": address,
        "operating_hours": operating_hours,
        "waze_link": waze_link,
        "latitude": latitude,
        "longitude": longitude,
    })
    time.sleep(0.015)
    i += 1
    # if i > 15:
    #     break

print(entries)
# Storing data as CSV
current_directory = os.getcwd()  # Get the current working directory
csv_file_path = os.path.join(current_directory, 'dataset.csv')
df = pd.DataFrame(entries, columns=['name', 'address', 'operating_hours', 'waze_link', 'latitude', 'longitude'])
df.to_csv(csv_file_path, index=False)
driver.quit()
# # Add a delay between requests to avoid overwhelming the website with requests
# time.sleep(1)