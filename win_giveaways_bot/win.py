import selenium
import instaloader
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random


def login(username, password, driver):
    driver.implicitly_wait(5)
    driver.get("https://www.instagram.com/accounts/login/")
    count = 0
    global username_element, password_element
    dom = driver.find_element_by_xpath('//*')
    while count < 15:
        try:
            username_element = dom.find_element_by_name('username')
            password_element = dom.find_element_by_name('password')
            break
        except:
            time.sleep(1)
            count = count + 1
            print(count)
    time.sleep(random.randint(5, 8))
    username_element.send_keys(username)
    time.sleep(5)
    password_element.send_keys(password)
    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    time.sleep(3)
    login_button.click()
    time.sleep(10)
    driver.get("https://www.instagram.com/" + username)


def get_following(driver):
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
    time.sleep(1)
    scroll_div = driver.find_element_by_xpath('html/body/div[4]/div/div[2]')
    previous_height = 0
    current_height = 1
    while previous_height != current_height:
        previous_height = current_height
        current_height = driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;', scroll_div)
        time.sleep(1)
        if previous_height == current_height:
            time.sleep(2)
            current_height = driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;', scroll_div)
    list_of_users = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul')
    items = list_of_users.find_elements_by_tag_name('li')
    usernames = set()
    for item in items:
        username_element = item.find_element_by_class_name('FPmhX')
        usernames.add(username_element.text)
    driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
    return usernames


def follow_people(big_users, driver):
    time.sleep(3)
    for big_user in big_users:
        driver.get("https://www.instagram.com/" + big_user)
        time.sleep(4)
        followers_element = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers_element.click()
        time.sleep(random.randint(1, 4))
        scroll_box = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        last_height, height = 0, 1
        while last_height != height:
            last_height = height
            time.sleep(random.randint(2, 5))
            height = driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight;", scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        users = [name.text for name in links if name.text != '']
        return users


def comment_with_users(users, giveaway_post, driver):
    try:
        driver.get(giveaway_post)
        text_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "Ypffh")))
        text_box.click()
        time.sleep(random.randint(5, 12))
        # for user in users:
        text_box.send_keys(users)
        text_box.send_keys(Keys.ENTER)
    except:
        time.sleep(1)



def write_following_to_file(following_list):
    file = open("following.txt", "w+")
    file.write(str(following_list))
    file.close()


def main():
    driver = webdriver.Firefox(executable_path=r'{PATH_TO_BOT_BROWSER}')
    login("{USERNAME}", "{PASSWORD}", driver)
    big_users = ["{USERNAME}"]
    # users = follow_people(big_users, driver)
    giveaway_post = "https://www.instagram.com/p/CIDc-lLHKnL/"
    users = ["I have to win this PS5!", "I have to win this PS5!"]
    comment_with_users(random.choice(users), giveaway_post, driver)


if __name__ == "__main__":
    main()
