from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without UI

# Set up the WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Start time to measure page load
start_time = time.time()

# Open the website
driver.get("https://www.skysports.com/")

# Wait for elements to load
driver.implicitly_wait(5)

# Measure page load time
page_load_time = round(time.time() - start_time, 2)

# Extracting details
page_title = driver.title
page_url = driver.current_url

# Meta Description (if available)
meta_desc = driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content") if driver.find_elements(By.XPATH, "//meta[@name='description']") else "No meta description found"

# H1 Tag
h1_tag = driver.find_element(By.TAG_NAME, "h1").text if driver.find_elements(By.TAG_NAME, "h1") else "No H1 found"

# H2 Tags
h2_tags = [h2.text for h2 in driver.find_elements(By.TAG_NAME, "h2")][:5]  # Get first 5 H2 tags

# First 5 Links
links = [a.get_attribute("href") for a in driver.find_elements(By.TAG_NAME, "a") if a.get_attribute("href")][:5]

# First 5 Images
images = [img.get_attribute("src") for img in driver.find_elements(By.TAG_NAME, "img") if img.get_attribute("src")][:5]

# Extract Body Text
body_text = driver.find_element(By.TAG_NAME, "body").text[:500]  # Limit to 500 characters

# Extract Footer Text (if available)
footer_text = driver.find_element(By.TAG_NAME, "footer").text if driver.find_elements(By.TAG_NAME, "footer") else "No footer found"

# Print results
print("Page Title:", page_title)
print("Page URL:", page_url)
print("Meta Description:", meta_desc)
print("H1 Tag:", h1_tag)
print("H2 Tags:", h2_tags)
print("First 5 Links:", links)
print("First 5 Images:", images)
print("Body Text Preview:", body_text)
print("Footer Text:", footer_text)
print("Page Load Time:", page_load_time, "seconds")

# Close browser
driver.quit()
