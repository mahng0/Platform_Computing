from selenium import webdriver
import time

def check_for_url(page_source):
    # Search for the <a> tag in the webpage content
    if "<a" in page_source:
        return True
    else:
        return False

def main(file_path):
    # Set up Selenium webdriver
    driver = webdriver.Chrome()  # You may need to adjust this according to your browser and its driver

    # Open the local HTML file
    driver.get("file://" + file_path.replace("\\", "/"))

    # Wait for the page to fully load
    time.sleep(2)  # Adjust this sleep time as needed for the page to fully load

    # Get the HTML source of the webpage
    page_source = driver.page_source

    # Check for URL in the webpage content
    url_present = check_for_url(page_source)

    # Close the webdriver
    driver.quit()

    # Determine presence time based on URL presence
    if url_present:
        return "Presence Time: 10 seconds"
    else:
        return "Presence Time: 0 seconds"

if __name__ == "__main__":
    file_path = r"C:\Users\caleb\OneDrive\Documents\cse4500\assignment_1\aboutME.html"

    print("Running script against the local HTML file:")
    presence_time = main(file_path)
    print(presence_time)
