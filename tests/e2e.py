import sys
from time import sleep

from selenium import webdriver


def test_scores_service(url):
    driver = webdriver.Chrome(executable_path="tests/chromedriver.exe")
    driver.get(url)
    sleep(1)
    text = driver.find_element_by_id("score").text
    if 1 <= int(text) <= 1000:
        driver.close()
        return True
    else:
        driver.close()
        return False


def main_function():
    score = test_scores_service("http://192.168.99.100:8777")
    if score:
        print("=== Passed ===")
        sys.exit(0)
    else:
        print("=== Failed ===")
        sys.exit(-1)


main_function()
