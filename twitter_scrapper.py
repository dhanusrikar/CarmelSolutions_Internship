from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector
from time import sleep
import pandas as pd

driver = webdriver.Chrome(
    'C:/Users/srikar/Downloads/New folder (6)/chromedriver')
# driver.get('https://twitter.com/')
# username = driver.find_element_by_name("session_key")
# username.send_keys('01fe18bec060@kletech.ac.in')

# password = driver.find_element_by_name('session_password')
# password.send_keys('twitter0809')
# sleep(0.5)

# sign_in_button = driver.find_element_by_class_name(
#     'sign-in-form__submit-button')
# sign_in_button.click()
# sleep(2)

df = pd.read_csv(
    'https://raw.githubusercontent.com/dhanusrikar/CarmelSolutions_Internship/main/facs/faculty_data_with_linkedin_2.csv?token=AKGSGKBEYCNUWM5XQXHQW63BKVEPK'
)
# df = df[:10]
twitter_id = []
followers = []
followings = []

# //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/span #twitter id
# //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div[1]/a/span[1]/span #following
# //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div[2]/a/span[1]/span #followers

for i in df.Twitter:
    if str(i) == 'na':
        twitter_id.append('na')
        followers.append('na')
        followings.append('na')
        continue
    else:
        print(i)
        driver.get(i)
        sleep(7)
        following_xpath = './/*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a/span[1]/span'
        following = driver.find_element_by_xpath(following_xpath).text
        follower_xpath = './/*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span'
        follower = driver.find_element_by_xpath(follower_xpath).text
        user_id_xpath = './/*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/span'
        user_id = driver.find_element_by_xpath(user_id_xpath).text
        twitter_id.append(user_id)
        followers.append(follower)
        followings.append(following)
        print(following, " ", follower, " ", user_id)

df['Number of followers'] = followers
df['Following'] = followings
df['Twitter_ID'] = twitter_id
df.to_csv('twitter_data.csv', index=False)
