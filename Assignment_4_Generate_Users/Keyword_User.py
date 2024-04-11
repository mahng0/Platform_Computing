from selenium import webdriver
import time

def extend_presence_time(keyword_found):
    if keyword_found:
        # Extend presence time by 10 seconds
        return 10
    else:
        return 0

def main(file_path, keyword):
    # Set up Selenium webdriver
    driver = webdriver.Chrome()  # You may need to adjust this according to your browser and its driver

    # Open the local HTML file
    driver.get("file://" + file_path.replace("\\", "/"))

    # Wait for the page to fully load
    time.sleep(2)  # Adjust this sleep time as needed for the page to fully load

    # Get the HTML source of the webpage
    page_source = driver.page_source

    # Print the page source to check if it's correct
    print("Page Source:")
    print(page_source)

    # Search for the keyword in the webpage content
    keyword_found = keyword.lower() in page_source.lower()

    # Extend presence time if keyword found
    extended_time = extend_presence_time(keyword_found)

    # Output presence time on the terminal
    print("Presence Time:", extended_time, "seconds")

    # Close the webdriver
    driver.quit()

if __name__ == "__main__":
    file_path = r"C:\Users\caleb\OneDrive\Documents\cse4500\assignment_1\aboutME.html"
    keyword = "Dragon"  # Keyword to search for

    print("Running script against the local HTML file:")
    main(file_path, keyword)
