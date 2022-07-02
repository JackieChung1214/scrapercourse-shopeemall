#步驟1：在專案中新增scraper.py檔案
#步驟2：引用以下模組：
#2.1.瀏覽器驅動模組(webdriver)
from selenium import webdriver
#2.2.Chrome瀏覽器驅動程式管理員模組(ChromeDriverManager)
from webdriver_manager.chrome import ChromeDriverManager
#2.3.定位方法模組(By)
from selenium.webdriver.common.by import By
#2.4.時間模組(time)
import time 

#步驟3：利用瀏覽器驅動(webdriver)、Chrome瀏覽器驅動程式管理員(ChromeDriverManager)模組，來建立瀏覽器驅動物件。
driver=webdriver.Chrome(ChromeDriverManager().install())

#步驟4：利用瀏覽器驅動物件的get()方法發送請求到蝦皮商城網站的居家生活網頁。
driver.get('https://shopee.tw/mall/%E5%B1%85%E5%AE%B6%E7%94%9F%E6%B4%BB-cat.11040925')
#步驟5：利用時間(time)模組等待5秒。
time.sleep(5)

#步驟6：在商品名稱上點擊滑鼠右鍵，找到且複製商品區塊元素的class(樣式類別)。
#步驟7：利用Selenium套件的find_elements()方法搜尋商品區塊元素。
cards=driver.find_elements(By.CSS_SELECTOR,"div[class='col-xs-2 recommend-products-by-view__item-card-wrapper']")

items=[]
#步驟8：利用迴圈讀取搜尋到的商品區塊元素。
for card in cards:
    #步驟9：在商品名稱上點擊滑鼠右鍵，找到且複製商品名稱元素的class(樣式類別)。
    #步驟10：利用Selenium套件的find_element()方法及text屬性，爬取商品名稱的資料。
    title=card.find_element(By.CSS_SELECTOR,"div[class='ie3A+n bM+7UW Cve6sh']").text
    #步驟11：在商品價格上點擊滑鼠右鍵，找到且複製商品價格元素的class(樣式類別)。
    #步驟12：利用Selenium套件的find_element()方法及text屬性，爬取商品價格的資料。
    price=card.find_element(By.CSS_SELECTOR,"span[class='ZEgDH9']").text
    #步驟13：利用Selenium套件的find_element()及get_attribute()方法，爬取子網頁的網址。
    link=card.find_element(By.TAG_NAME,"a").get_attribute('href')
    #步驟14：打包爬取到的商品名稱、價格及子網頁網址資料。
    items.append((title,price,link))

#步驟15：利用print()方法印出打包後的商品資料。
print(items)