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

    rand_id = random.randint(0, 2)
    element = driver.find_element_by_id("id-preference-{}".format(rand_id))
    auction_id = element.get_attribute('data-auction-id')
    left_auction_id = driver.find_element_by_id("id-preference-1").get_attribute('data-auction-id')
    right_auction_id = driver.find_element_by_id("id-preference-2").get_attribute('data-auction-id')
    print("Stage 1: Selected Auction {} from ({}, {})".format(auction_id, left_auction_id, right_auction_id))
    element.click()
    # driver.find_element(By.ID, 'id-preference-0').click()
    driver.find_element(By.XPATH, '//button').click()


def play_phase_two_screen(driver, round):
    if round == 1:
        driver.save_screenshot('screenshots/phase_two_choice_screen.png')

    min_value = int(driver.find_element_by_id('cutoff').get_attribute('min'))
    max_value = int(driver.find_element_by_id('cutoff').get_attribute('max'))
    random_cutoff = random.randint(min_value, max_value)
    print("Stage 2: Selected Cutoff {}".format(random_cutoff))
    driver.execute_script("""$('input[type="range"]').val({}).change();""".format(random_cutoff))
    driver.find_element(By.XPATH, "//input[@id='clicked']").value = '1'
    driver.find_element(By.XPATH, '//button').click()


def play_phase_three_screen(driver, round):
    if round == 1:
        driver.save_screenshot('screenshots/phase_three_choice_screen.png')

    min_value = int(driver.find_element_by_id("id_bid").get_attribute('data-min'))
    max_value = int(driver.find_element_by_id("id_bid").get_attribute('data-max'))
    input_field = driver.find_element(By.XPATH, "//input[@id='id_bid']")
    input_field.clear()
    random_bid = random.randint(min_value, max_value)
    print("Stage 3: Entered Bid {}".format(random_bid))
    input_field.send_keys(str(random_bid))
    driver.find_element(By.XPATH, '//button').click()


def play_phase_four_screen(driver, round):
    if round == 1:
        driver.save_screenshot('screenshots/phase_four_choice_screen.png')

    driver.find_element(By.XPATH, "//input[@id='clicked']").value = '1'
    if random.randint(0, 1) == 0:
        print('Stage 4: Betting high on Red')
        driver.find_element(By.XPATH, "//button[@id='red-bet-button']").click()
    else:
        print('Stage 4: Betting high on Blue')
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
    die_side = int(driver.find_element_by_id("side").get_attribute('value'))
    print("Stage 4: Rolled Die Side {}".format(die_side))

    driver.find_element(By.XPATH, "//button[@id='next-button']").click()


def play_phase_one(driver):
    print('--Stage 1--')
    play_instructions(driver, 'one')
    for round in range(Experiment.phase_one_rounds()):
        play_phase_one_screen(driver, round)


def play_phase_two(driver):
    print('--Stage 2--')
    play_instructions(driver, 'two')
    for round in range(Experiment.phase_two_rounds()):
        play_phase_two_screen(driver, round)


def play_phase_three(driver):
    print('--Stage 3--')
    play_instructions(driver, 'three')
    for round in range(Experiment.phase_three_rounds()):
        play_phase_three_screen(driver, round)


def play_phase_four(driver):
    print('--Stage 4--')
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
        print("Opening browser tab {}".format(i))
        driver.switch_to.window(driver.window_handles[i])
        play_phase_one(driver)
        play_phase_two(driver)
        play_phase_three(driver)
        play_phase_four(driver)
