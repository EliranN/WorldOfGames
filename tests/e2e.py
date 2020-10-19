import sys
from sys import argv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_scores_service(url, port) -> int:
    driver = webdriver.Chrome(ChromeDriverManager().install())

    try:
        driver.get("http://" + url + ":" + port)
        driver.implicitly_wait(5)
        actual = driver.find_element_by_id("score").text
        if 1 <= int(actual) <= 1000:
            driver.close()
            return 0
        else:
            return 1
    except Exception:
        driver.close()
        return 1


def main_function(url, port):
    if 0 == int(test_scores_service(url, port)):
        sys.exit(0)
    else:
        sys.exit(-1)


if __name__ == "__main__":
    try:
        print(len(argv))
        if len(argv) == 3:
            param_1 = argv[1:]
            param_2 = argv[2:]
            main_function(param_1, param_2)
        elif len(argv) == 2:
            param_1 = argv[1:]
            param_2 = "8777"
            main_function(param_1, param_2)
        elif len(argv) == 1:
            param_1 = "127.0.0.1"
            param_2 = "8777"
            main_function(param_1, param_2)
        else:
            print('Please provide IP and Port number...')
    except IndexError:
        param_1 = "172.18.0.2"
        param_2 = "8777"
