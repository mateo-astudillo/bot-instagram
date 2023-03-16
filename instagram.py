import ssl
import os # environment variables
from dotenv import load_dotenv
from time import sleep # time chrage
from selenium import webdriver # google chrome controller
from selenium.webdriver.common.by import By # search
from selenium.webdriver.common.keys import Keys # login
from re import sub

def getUsers(number: int) -> list:
    CLASS_ELEMENTS = "x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xh8yej3 x193iq5w x1lliihq x1dm5mii x16mil14 xiojian x1yutycm"
    CLASS_USER = "x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1"

    n = 0
    n_prev = 0
    elements = []
    while n != number:
        if n == n_prev:
            elements = driver.find_elements(By.CSS_SELECTOR, f"div[class='{CLASS_ELEMENTS}'")
            n = len(elements)
            sleep(0.2)
        else:
            n_prev = n
            driver.execute_script("arguments[0].scrollIntoView()", elements[n - 1])
            sleep(1)
    users = []
    elements = driver.find_elements(By.CSS_SELECTOR, f"div[class='{CLASS_USER}']")
    for e in elements:
        users.append(e.text)
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
