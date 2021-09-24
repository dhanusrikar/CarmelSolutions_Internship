from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector
from time import sleep
import pandas as pd
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(
    chrome_options=chrome_options,
    executable_path=r'C:/Users/srikar/Downloads/New folder (6)/chromedriver')

driver.get('https://en-gb.facebook.com')
username = driver.find_element_by_name("email")
username.send_keys('01fe18bec060@kletech.ac.in')

password = driver.find_element_by_name('pass')
password.send_keys('twitter0809')
sleep(0.5)

sign_in_button = driver.find_element_by_name('login')
sign_in_button.click()
sleep(1)

df = pd.read_csv(
    'https://raw.githubusercontent.com/dhanusrikar/CarmelSolutions_Internship/main/facs/faculty_data_with_linkedin_2.csv?token=AKGSGKBEYCNUWM5XQXHQW63BKVEPK'
)

f = []

for i in df.Facebook:
    if str(i) == 'na':
        f.append('na')
        continue
    else:
        # print(i)
        i = i.replace('www', 'en-gb')
        # driver.get('https://en-gb.facebook.com/manjunath.mallashetty')
        driver.get(i)
        sleep(5)
        xpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[3]/div[1]/span/span[2]'
        try:
            friends = driver.find_element_by_xpath(xpath).text
            print(friends)
            f.append(friends)
        except:
            f.append('na')
            print('0')
df['facebook_friends'] = f
df.to_csv('with_facebook_friends.csv', index=False)