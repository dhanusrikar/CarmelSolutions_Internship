from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector
from time import sleep
import pandas as pd

driver = webdriver.Chrome(
    'C:/Users/srikar/Downloads/New folder (6)/chromedriver')
driver.get('https://linkedin.com/')
username = driver.find_element_by_name("session_key")
username.send_keys('srikar.spare@gmail.com')

password = driver.find_element_by_name('session_password')
password.send_keys('srikar08')
sleep(0.5)

sign_in_button = driver.find_element_by_class_name(
    'sign-in-form__submit-button')
sign_in_button.click()
sleep(2)

df = pd.read_csv(
    'https://raw.githubusercontent.com/dhanusrikar/CarmelSolutions_Internship/main/facs/faculty_data_with_linkedin_2.csv?token=AKGSGKBEYCNUWM5XQXHQW63BKVEPK'
)
# df = df[:10]
connections = []

links = df.LinkedIn
for link in links:
    if type(
            link
    ) == float or link == 'linkedin' or link == 'NA' or '@' in link or '/pub' in link:
        connections.append('na')
        print('na')
    elif '.com/in' in link:
        driver.get(link)
        try:
            connection = driver.find_element_by_xpath(
                './/*[@id="ember44"]/div[2]/ul/li/span/span').text
            connections.append(connection)
            print(connection)
        except:
            connections.append('na')
            print('na')
    else:
        driver.get('https://linkedin.com/in/' + link)
        try:
            connection = driver.find_element_by_xpath(
                './/*[@id="ember44"]/div[2]/ul/li/span/span').text
            connections.append(connection)
            print(connection)
        except:
            connections.append('na')
            print('na')

    sleep(2)

df['LinkedInConnections'] = connections
df.to_csv('file_with_connections.csv', index=False)

# driver.get('https://linkedin.com/in/dr-ankita-srivastava-42486a1b4')
# # sleep(0.5)

# # //*[@id="ember44"]/div[2]/ul/li/span/span
# connection = driver.find_element_by_xpath(
#     './/*[@id="ember44"]/div[2]/ul/li/span/span').text
# print(connection)