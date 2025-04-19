import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website): 
    # Log the start of the scraping process
    print("Launching Chrome browser...")

    # Specify the path to the ChromeDriver executable
    # Leave as "" if chromedriver is in your PATH, otherwise set absolute path
    chrome_driver_path = "./chromedriver"

    # Set up Chrome options (can add headless mode, disable GPU, etc.)
    options = webdriver.ChromeOptions()
    # Example: Uncomment the next line to run in headless mode
    # options.add_argument("--headless")

    # Initialize the Chrome WebDriver with specified service and options
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        # Open the target website
        driver.get(website)
        print("Page loaded...")

        # Extract the page's full HTML source
        html = driver.page_source
        time.sleep(10)

        # Return the HTML for downstream parsing/processing
        return html

    finally:
        # Ensure the browser is closed, even if an error occurs
        driver.quit()
