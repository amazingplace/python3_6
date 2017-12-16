from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib.request
import urllib3
import requests
import shutil
import time
user_info = {'email':'7rzj9u','password':'1994122500000'}
target_url = "http://www.bishefuwu.com/login-developer.html"
download_path = 'L:\\bishefuwu'
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir',download_path)
#设置为：2，自定义下载路径；1,默认路径； 0,桌面
profile.set_preference('browser.download.folderList', 2)
#开始下载时是否显示下载管理器
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.forbid_open_with',True)
profile.set_preference('browser.helperApps.neverAsk.openFile', 'application/octet-stream')
#对所给出文件类型不再弹出框进行询问
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream')
profile.set_preference('dom.disable_window_flip', True)
driver = webdriver.Firefox(firefox_profile=profile)

driver.get(target_url)
login_data = driver.find_element_by_name('username')
login_password = driver.find_element_by_name('password')
login_data.send_keys(user_info['email'])
login_password.send_keys(user_info['password'])
driver.find_element_by_css_selector('button').click()
try:
     element = WebDriverWait(driver, 100).until(
     EC.url_changes(target_url)
     )
finally:
    if element:
        target_url = driver.current_url
        print(driver.current_url)
        driver.get(target_url)
        txt = driver.find_element_by_css_selector('.icon.icon-list-ul').click()
        try:
             element = WebDriverWait(driver, 10).until(
             EC.url_changes(target_url)
             )
        finally:
            if element:
                target_url = driver.current_url
                driver.get(target_url)
                print(target_url)
                alloption = driver.find_elements_by_tag_name('option')
# for option in alloption:
#     print("Value is : %s" % option.get_attribute('value'))
alloption[1].click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.url_changes(target_url)
    )
finally:
    if element:
        target_url = driver.current_url
        driver.get(target_url)
        print(target_url)

all_link = driver.find_elements_by_link_text('详情')
temp_current = target_url
i = 0
main_window = driver.current_window_handle
print('mainwindow%s' %main_window.title())
for link in all_link:
    #print("href is : %s" % link.get_attribute('href'))
    strlink = '"'+link.get_attribute('href') + '"'
    js = 'window.open(' +strlink + ');'  # 新建的窗口
    #print(js)
    driver.execute_script(js)
    time.sleep(3)
    window_handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    i+=1
    driver.switch_to.window(window_handles[1])
    time.sleep(3)
    download_class = driver.find_element_by_class_name('btn.btn-inverse.btn-xs')
    download_link = download_class.get_attribute('href')
    download_filename_class = driver.find_elements_by_css_selector(\
        '.table.table-striped.table-bordered.table-hover \
        tr td')
    # download_filename_class.index('tr')
    # print(download_filename_class[0].text)
    download_filename = download_filename_class[0].text+download_filename_class[1].text
    # print(download_link)
    # print(download_filename)
    local = os.path.join(download_path,download_filename+str(i)+'.zip')
    urllib.request.urlretrieve(download_link,local)
    time.sleep(3)
    driver.close()
    #time.sleep(3)
    driver.switch_to.window(window_handles[0])
    time.sleep(3)
