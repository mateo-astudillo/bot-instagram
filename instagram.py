import ssl
import os # environment variables
from dotenv import load_dotenv
from time import sleep # time chrage
from selenium import webdriver # google chrome controller
from selenium.webdriver.common.by import By # search
from selenium.webdriver.common.keys import Keys # login
from re import sub

def getUsers(number: int) -> list:
    CLASS_ELEMENTS = "_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm"
    CLASS_USER = " _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm"
    users = []
    time = 0.2
    for i in range( number ):
        sleep(time)
        elements = driver.find_elements(By.CSS_SELECTOR, f"div[class='{CLASS_ELEMENTS}'")
        e = elements[i].find_element(By.CSS_SELECTOR, f"div[class='{CLASS_USER}']")
        n_els = len(elements)
        users.append(e.text)
        print(e.text)
        driver.execute_script("arguments[0].scrollIntoView()", elements[n_els - 1])
        if n_els == number:
            time = 0
    return users

def getNumber(users: str) -> int:
    e = driver.find_element(By.CSS_SELECTOR, f"a[href='/{USER}/{users}/']")
    num = e.text
    num = sub("[^0-9]", "", num)
    return int(num)

# Data
load_dotenv()
INSTAGRAM_USER = os.getenv("INSTAGRAM_USER")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
PATH = os.getenv("PATH_CHROME_DRIVER")
USER = input("User: ")

# Init Google Chrome
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

# ssl
ssl._create_default_https_context = ssl._create_unverified_context

# login
sleep(4) # loading
username = driver.find_element("css selector", "input[name='username']")
password = driver.find_element("css selector", "input[name='password']")
username.clear()
password.clear()
username.send_keys(INSTAGRAM_USER)
password.send_keys(INSTAGRAM_PASSWORD)
login = driver.find_element("css selector", "button[type='submit']").click()

# Go followers
sleep(4) # loading
driver.get(f"https://www.instagram.com/{USER}/followers")

# Get followers
sleep(4) # loading
number_followers = getNumber("followers")
print("Followers: ", number_followers)
followers = getUsers(number_followers)

# Go following
sleep(4) # loading
driver.get(f"https://www.instagram.com/{USER}/following")

# Get followings
sleep(4) # loading
number_following = getNumber("following")
print("Following: ", number_following)
following = getUsers(number_following)

# Results
print("Usuarios que no te siguen: ")
for user in following:
    if user not in followers:
        print(user)
