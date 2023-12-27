from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components1.filter import LeftFilter
from components1.base import Base
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")
search_term1 = "Rolex"
search_term2 = "Casio"
page = Base(driver)
left_filter = LeftFilter(driver)

print("---------- First Test ("+ search_term1 +") ----------")

# Verify Price and Title of Rolex

# Check the box

left_filter.select_brand(search_term1)

# Store the title and price of each of the two results

for i in (0, 1,):

    # Title and Price locators on base page

    title_xpath = '//ul[@class="srp-results srp-grid clearfix"]/li[@data-viewport][@data-gr2="'+ str(i + 2) + '"]//span[@role="heading"]'
    price_xpath = '//ul[@class="srp-results srp-grid clearfix"]/li[@data-viewport][@data-gr2="'+ str(i + 2) + '"]//span[@class="s-item__price"]'

    # Store data in respective variables

    base_title = page.retrieve_text(title_xpath)
    base_price_1 = page.retrieve_text(price_xpath)
    base_price = base_price_1.split("$")[1]

    # print(base_title)
    # print(base_price)

    # Validate that the two title results contain "Rolex"

    # brand_text = "Rolex"
    if search_term1 in base_title:
        print('The Title Text contains the brand, "' + search_term1 + '"')
    elif search_term1.upper() in base_title:
        print('The Title Text contains the brand, "' + search_term1 + '" (UPPER-CASE)')
    else:
        print(False)

    # Click on the item

    page.click((By.XPATH, title_xpath))

    # Switch to the item tab, for the item which was just opened

    driver.switch_to.window(driver.window_handles[i + 1])

    # Retrieve the title and price of the item, from the item page

    item_title_xpath = "//h1[@class='x-item-title__mainTitle']/span"
    item_price_xpath = "//div[@class='x-price-primary']/span"

    item_title = page.retrieve_text(item_title_xpath)
    item_price_before = page.retrieve_text(item_price_xpath)
    item_price_after = item_price_before.split("$")[1]

    # print(item_title)
    # print(item_price_after)
    # print(base_price)

    # Verify that the NAME of the product on the base page, matches the name of the product on the item detail page

    if item_title == base_title:
        print('The Titles Match: ', item_title)
    else:
        print('No Title Match')

    # Verify that the PRICE of the product on the base page, matches the price of the product on the item detail page

    if item_price_after == base_price:
        print('The Prices Match: ', item_price_after)
    else:
        print('No Price Match')

    # Go back to the base tab

    driver.switch_to.window(driver.window_handles[0])

print("---------- Second Test ("+ search_term2 +") ----------")

# Uncheck the first box

left_filter.select_brand(search_term1)

# Check the second box

# Check the box

left_filter.select_brand(search_term2)

# Validate that the last 2 results contain the second search term

for i in (0, 1):

    title_xpath = '//ul[@class="srp-results srp-grid clearfix"]/li[@data-viewport][last()-'+ str(i) +']//span[@role="heading"]'

    # time.sleep(10)

    base_title = page.retrieve_text(title_xpath)

    print(base_title)

    if search_term2 in base_title:
        print('The Title Text contains the brand, "' + search_term2 + '"')
    elif search_term2.upper() in base_title:
        print('The Title Text contains the brand, "' + search_term2 + '" (UPPER-CASE)')
    else:
        print(False)

driver.quit()



