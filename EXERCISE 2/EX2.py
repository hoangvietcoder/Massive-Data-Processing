from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

username = '1953801013255'
password = 'Nhumotgiacmo2512<3'
namHoc = '2021-2022'
hocKy = 'Học kỳ 2'
tuan = '16'

website = 'https://daotao.hcmulaw.edu.vn/?PageId=79d80304-9480-4c03-9f89-2246c66b050a&ModuleID=30174dea-54d6-4cfa' \
          '-9df8-4ad5494da6d1&Role=NV '
path = '.\Driver\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)
driver.find_element(By.ID, 'ctl09_txtUserName').send_keys(username)
driver.find_element(By.ID, 'ctl09_txtPassword').send_keys(password)
driver.find_element(By.ID, 'ctl09_btnDangnhap').click()
driver.find_element(By.LINK_TEXT, 'Thời khóa biểu - lịch thi').click()
selectNamHoc = Select(driver.find_element(By.ID, 'ctl09_ctl00_ddlNamHoc'))
selectNamHoc.select_by_value(namHoc)
selectHocKy = Select(driver.find_element(By.ID, 'ctl09_ctl00_ddlHocKy'))
selectHocKy.select_by_visible_text(hocKy)

selectTuan = Select(driver.find_element(By.ID, 'ctl09_ctl00_ddlTuan'))

selectTuan.select_by_visible_text(tuan)

soHang = len(driver.find_elements_by_xpath(
    '/html/body/form/div[4]/table/tbody/tr[2]/td/div/div/div/div[2]/div[3]/div/div/table/tbody/tr/td/table/tbody/tr['
    '2]/td/table/tbody/tr'))

soCot = len(driver.find_elements_by_xpath(
    '/html/body/form/div[4]/table/tbody/tr[2]/td/div/div/div/div[2]/div[3]/div/div/table/tbody/tr/td/table/tbody/tr['
    '2]/td/table/tbody/tr[1]/td'))

TKB = {'THỨ 2': [], 'THỨ 3': [], 'THỨ 4': [], 'THỨ 5': [], 'THỨ 6': [], 'THỨ 7': []}
for column in range(2, soCot):
    for row in range(2, soHang):
        path = '/html/body/form/div[4]/table/tbody/tr[2]/td/div/div/div/div[2]/div[' \
               '3]/div/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[' + str(row) + ']/td[' + str(column) \
               + \
               ']/b'
        if len(driver.find_element(By.XPATH, path)) > 0:
            THU = 'THỨ' + str(column)
            crawlXpath = '/html/body/form/div[4]/table/tbody/tr[2]/td/div/div/div/div[2]/div[' \
                         '3]/div/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[' + str(row) + \
                         ']/td[' + str(column) + ']'
            crawl = driver.find_element(By.XPATH, crawlXpath).text
            crawlList = crawl.split('\n')
            print(crawlList)
