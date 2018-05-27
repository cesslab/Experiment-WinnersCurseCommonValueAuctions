import random
from os import environ

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from exp.experiment import Experiment


def play_instructions(driver, phase):
    driver.save_screenshot('{}/phase_{}_instructions.png'.format(environ.get('SCREENSHOT_PATH'), phase))
    driver.find_element(By.XPATH, '//button').click()


def play_phase_one_screen(driver, round):
    if round == 1:
        driver.save_screenshot('screenshots/phase_one_choice_screen.png')

    driver.find_element(By.ID, 'id-preference-0').click()
    driver.find_element(By.XPATH, '//button').click()


def play_phase_two_screen(driver, round):
    if round == 1:
        driver.save_screenshot('screenshots/phase_two_choice_screen.png')

    driver.execute_script("""$('input[type="range"]').val(10).change();""")
    driver.find_element(By.XPATH, "//input[@id='clicked']").value = '1'
    driver.find_element(By.XPATH, '//button').click()


def play_phase_three_screen(driver, round):
    if round == 1:
        driver.save_screenshot('screenshots/phase_three_choice_screen.png')

    input_field = driver.find_element(By.XPATH, "//input[@id='id_bid']")
    input_field.clear()
    input_field.send_keys(str(random.randint(1, 28)))
    driver.find_element(By.XPATH, '//button').click()


def play_phase_four_screen(driver, round):
    if round == 1:
        driver.save_screenshot('screenshots/phase_four_choice_screen.png')

    driver.find_element(By.XPATH, "//input[@id='clicked']").value = '1'
    if random.randint(0, 1) == 0:
        driver.find_element(By.XPATH, "//button[@id='red-bet-button']").click()
    else:
        driver.find_element(By.XPATH, "//button[@id='blue-bet-button']").click()

    driver.execute_script("""$('input[type="range"]').val({}).change();""".format(random.randint(0, 10)))

    driver.find_element(By.XPATH, "//button[@id='next-button']").click()


def start_two_player_session(driver, url):
    driver.get(url)

    links = driver.find_elements_by_partial_link_text("InitializeParticipant")

    for link in links:
        link.send_keys(Keys.COMMAND + Keys.ENTER)

    return len(driver.window_handles)


def play_roll_die(driver):
    driver.save_screenshot('screenshots/phase_four_roll_die_screen.png')
    driver.find_element(By.XPATH, "//button[@id='die-button']").click()
    driver.find_element(By.XPATH, "//button[@id='next-button']").click()


def play_phase_one(driver):
    play_instructions(driver, 'one')
    for round in range(Experiment.phase_one_rounds()):
        play_phase_one_screen(driver, round)


def play_phase_two(driver):
    play_instructions(driver, 'two')
    for round in range(Experiment.phase_two_rounds()):
        play_phase_two_screen(driver, round)


def play_phase_three(driver):
    play_instructions(driver, 'three')
    for round in range(Experiment.phase_three_rounds()):
        play_phase_three_screen(driver, round)


def play_phase_four(driver):
    play_instructions(driver, 'four')
    play_roll_die(driver)
    for round in range(Experiment.phase_four_rounds()):
        play_phase_four_screen(driver, round)


# Run with python -m browser_tests.browser_test
if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument('--window-size=1300,1400')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(30)
    num_tabs = start_two_player_session(driver, "http://127.0.0.1:8000/demo/phase_one/")

    for i in range(1, num_tabs):
        driver.switch_to.window(driver.window_handles[i])
        play_phase_one(driver)
        play_phase_two(driver)
        play_phase_three(driver)
        play_phase_four(driver)
