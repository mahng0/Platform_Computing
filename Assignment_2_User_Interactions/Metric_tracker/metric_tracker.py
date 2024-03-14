from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def monitor_metrics(url):
    try:
        # Launch Chrome WebDriver
        driver = webdriver.Chrome()
        driver.get(url)

        # Wait for the page to load fully
        wait = WebDriverWait(driver, 30)  # Wait up to 30 seconds
        wait.until(EC.title_contains("About Me"))  # Wait for page title to contain "About Me"

        # Measure time when page is loaded
        start_time = time.time()

        # Get title of the page
        page_title = driver.title

        # Wait for the paragraph element to be present
        paragraph_element = wait.until(EC.presence_of_element_located((By.ID, "general_info_paragraph")))

        # Get text content of the paragraph
        paragraph_text = paragraph_element.text
        print("General Information Paragraph Text:", paragraph_text)

        # Measure time when page is closed
        end_time = time.time()
        time_spent = end_time - start_time

    except Exception as e:
        print("An error occurred:", e)
        time_spent = None
        page_title = None
        paragraph_text = None
        driver.quit()  # Make sure to quit the WebDriver on exception

    finally:
        # Quit WebDriver
        driver.quit()

    return time_spent, page_title, paragraph_text

if __name__ == "__main__":
    url = "file:///C:/Users/caleb/Documents/Platform_Computing/assignment_1/aboutME.html"
    time_spent, page_title, paragraph_text = monitor_metrics(url)

    print(f"Time spent on {url}: {time_spent} seconds")
    print(f"Page title: {page_title}")
    print(f"Paragraph contents: {paragraph_text}")
