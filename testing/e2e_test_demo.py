
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    # Set up the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Step 1: Navigate to Google
        driver.get("https://www.google.com")
        print("Opened Google homepage.")

        # Step 2: Locate the search bar and enter "smart watch"
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("Apple smart watch")
        search_box.send_keys(Keys.RETURN)
        print("Performed Google search for 'smart watch'.")

        # Step 3: Wait for search results and click the first link
        first_result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div#search a h3"))
        )
        first_result.click()
        print("Clicked the first search result.")

        # Step 4: Check if "Apple Watch" is mentioned on the page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        page_source = driver.page_source
        if "Apple Watch" in page_source:
            print("Apple Watch is mentioned on the page.")
        else:
            print("Apple Watch is NOT mentioned on the page.")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_google_search()
