  
import selenium
from selenium.webdriver import Safari
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

# File to keep track of processed messages
PROCESSED_MESSAGES_FILE = "processed_messages.txt"

# Function to load processed messages
def load_processed_messages():
    if os.path.exists(PROCESSED_MESSAGES_FILE):
        with open(PROCESSED_MESSAGES_FILE, "r") as file:
            return set(file.read().splitlines())
    return set()

# Function to save processed messages
def save_processed_messages(processed_messages):
    with open(PROCESSED_MESSAGES_FILE, "w") as file:
        file.write("\n".join(processed_messages))

# Function to get new messages
def get_new_messages(messages, processed_messages):
    return [msg for msg in messages if msg not in processed_messages]

# Web scraping setup
LINK = 'https://web.whatsapp.com/'
driver = Safari()
driver.get(LINK)
wait = WebDriverWait(driver, 100)

# Our chat to scrape is called JLS 2027
target = '"JLS 2027"'  # keep it wrapped in quotes for it to work
search_text = 'JLS 2027'

# Searching for the chat to click on it
search_x_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
search_bar = wait.until(EC.presence_of_element_located((By.XPATH, search_x_path)))
time.sleep(5)
search_bar.click()
search_bar.send_keys(search_text)

# Clicking on the chat
x_arg = '//span[contains(@title, ' + target + ')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()

# Load processed messages from the file
processed_messages = load_processed_messages()

# Web scraping the chat
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
message_elements = soup.find_all('div', {'class': '_21Ahp'})

# Extract messages from the chat
current_messages = [str(message.text) for message in message_elements if 'You deleted this message' not in message.text]

# Get new messages by comparing with processed ones
new_messages = get_new_messages(current_messages, processed_messages)

# Display new messages
if new_messages:
    print("New messages:")
    for message in new_messages:
        print(message)
else:
    print("No new messages.")

# Update processed messages
processed_messages.update(new_messages)
save_processed_messages(processed_messages)

# Clean up
driver.quit()
