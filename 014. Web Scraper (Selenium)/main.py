from selenium import webdriver
import time

chrome_driver_path = r"C:\Users\Beno\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open chrome and the website itself
# Insert the name of the website
driver.get("") # Full link of the website

# Wait until the website is fully loaded
time.sleep(5)

# Scrape the total amount in your account
# Also possible to change the type of item scraped
# Check the HTML type
value = driver.find_element_by_class_name("dashboard_total_title")
print(value.text)

# Close chrome
driver.quit()