from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_amazon(query, pages=2):
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-webgl")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    results = []

    for page in range(1, pages + 1):
        print(f"🔎 Scraping page {page}...")
        url = f"https://www.amazon.in/s?k={query}&page={page}"
        driver.get(url)
        time.sleep(3) 

        items = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

        for item in items:
         
            try:
                name = item.find_element(By.TAG_NAME, "h2").text
            except:
                name = "Not Available"

            # Price
            try:
                price = item.find_element(By.CLASS_NAME, "a-price-whole").text
            except:
                price = "Not Available"

            # Rating
            try:
                rating = item.find_element(By.XPATH, ".//span[@class='a-icon-alt']").get_attribute("innerHTML")
            except:
                rating = "Not Available"

            # Reviews
            try:
                reviews = item.find_element(By.XPATH, ".//span[@class='a-size-base s-underline-text']").text
            except:
                reviews = "Not Available"

            results.append({
                "Name": name,
                "Price": price,
                "Rating": rating,
                "Reviews": reviews
            })

    driver.quit()
    return results


if __name__ == "__main__":
    query = input("Enter product to search: ")
    data = scrape_amazon(query, pages=2)   

    df = pd.DataFrame(data)
    df.to_excel("amazonproduct.xlsx", index=False)

    print("Data saved to amazonproduct.xlsx")
