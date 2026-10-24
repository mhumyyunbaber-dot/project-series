import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_and_save():

    folder_name = "scraped_data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Step 2: Open browser
    driver = webdriver.Chrome()
    driver.get("https://en.wikipedia.org/wiki/Open_source")  

    
    time.sleep(3)

    headings = driver.find_elements(By.TAG_NAME, "h2")
    data = [h.text for h in headings if h.text.strip() != ""]

    # Step 5: Save data into file inside folder
    file_path = os.path.join(folder_name, "open_source_headings.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        for line in data:
            f.write(line + "\n")

    print(f" Data scraped and saved to {file_path}")

    # Step 6: Close browser
    driver.quit()

scrape_and_save()
