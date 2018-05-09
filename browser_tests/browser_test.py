from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from auction.treatment_one import PHASE_ONE_AUCTION_PAIRS


def play_instructions(driver):
    driver.find_element(By.XPATH, '//button').click()


def play_phase_one_screen(driver):
    driver.find_element(By.ID, 'id-preference-0').click()
    driver.find_element(By.XPATH, '//button').click()


def play_phase_two_screen(driver):
    driver.execute_script("""$('input[type="range"]').val(10).change();""")


def start_two_player_session(driver, url):
    driver.get(url)

    links = driver.find_elements_by_partial_link_text("InitializeParticipant")

    for link in links:
        link.send_keys(Keys.COMMAND + Keys.ENTER)

    print("There are {} tabs open.".format(len(driver.window_handles)))


# Run with python -m browser_tests.browser_test
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    start_two_player_session(driver, "http://127.0.0.1:8000/demo/phase_one/")

    driver.switch_to.window(driver.window_handles[1])
    play_instructions(driver)
    for pair in PHASE_ONE_AUCTION_PAIRS:
        play_phase_one_screen(driver)

    play_instructions(driver)
    play_phase_two_screen(driver)


