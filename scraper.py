from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains
#引用模組
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(ChromeDriverManager().install())

for page in range(1,3):


    driver.get(f'https://shopee.tw/mall/%E5%B1%85%E5%AE%B6%E7%94%9F%E6%B4%BB-cat.11040925/popular?pageNumber={page}')
    #time.sleep(5)

    ActionChains(driver).move_by_offset(100,100).click().perform()

    locator=(By.CSS_SELECTOR,"div[class='col-xs-2 recommend-products-by-view__item-card-wrapper']")
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located(locator),
        "找不到指定元素"
    )

    cards=driver.find_elements(By.CSS_SELECTOR,"div[class='col-xs-2 recommend-products-by-view__item-card-wrapper']")

    items=[]
    for card in cards:
        title=card.find_element(By.CSS_SELECTOR,"div[class='ie3A+n bM+7UW Cve6sh']").text
        price=card.find_element(By.CSS_SELECTOR,"span[class='ZEgDH9']").text
        link=card.find_element(By.TAG_NAME,"a").get_attribute('href')
        items.append((title,price,link))

    #print(items)

    result=[]
    for item in items:
        driver.get(item[2])

        #設定滑鼠滾動次數
        for i in range(5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)

        comments=driver.find_elements(By.CSS_SELECTOR,"div[class='Em3Qhp']")
        for comment in comments:
            result.append((item[0],item[1],comment.text))
        break

    print(f"第{page}頁")
    print(result)