import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from exp.experiment import Experiment


def play_instructions(driver):
    driver.find_element(By.XPATH, '//button').click()


def play_phase_one_screen(driver):
    driver.find_element(By.ID, 'id-preference-0').click()
    driver.find_element(By.XPATH, '//button').click()


def play_phase_two_screen(driver):
    driver.execute_script("""$('input[type="range"]').val(10).change();""")
    driver.find_element(By.XPATH, "//input[@id='clicked']").value = '1'
    driver.find_element(By.XPATH, '//button').click()


def play_phase_three_screen(driver):
    input_field = driver.find_element(By.XPATH, "//input[@id='id_bid']")
    input_field.clear()
    input_field.send_keys(str(random.randint(1, 28)))
    driver.find_element(By.XPATH, '//button').click()


def start_two_player_session(driver, url):
    driver.get(url)

    links = driver.find_elements_by_partial_link_text("InitializeParticipant")

    for link in links:
        link.send_keys(Keys.COMMAND + Keys.ENTER)

    return len(driver.window_handles)

def play_phase_one(driver):
    play_instructions(driver)
    for round in range(Experiment.phase_one_rounds()):
        play_phase_one_screen(driver)


def play_phase_two(driver):
    play_instructions(driver)
    for round in range(Experiment.phase_two_rounds()):
        play_phase_two_screen(driver)


def play_phase_three(driver):
    play_instructions(driver)
    for round in range(Experiment.phase_three_rounds()):
        play_phase_three_screen(driver)


# Run with python -m browser_tests.browser_test
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    num_tabs = start_two_player_session(driver, "http://127.0.0.1:8000/demo/phase_one/")

    for i in range(1, num_tabs):
        driver.switch_to.window(driver.window_handles[i])
        play_phase_one(driver)
        play_phase_two(driver)
        play_phase_three(driver)



