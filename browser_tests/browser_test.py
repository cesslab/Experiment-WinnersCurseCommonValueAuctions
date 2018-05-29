import random
import os
import glob
from os import environ

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from exp.experiment import Experiment

SCREEN_SHOT_PATH = environ.get('SCREEN_SHOT_PATH')
SITE_URL = environ.get('SITE_URL')


def play_instructions(browser, phase):
    browser.save_screenshot('{}/phase_{}_instructions.png'.format(SCREEN_SHOT_PATH, phase))
    browser.find_element(By.XPATH, '//button').click()


def play_phase_one_screen(browser, round_number):
    if round_number == 1:
        browser.save_screenshot('{}/phase_one_choice_screen.png'.format(SCREEN_SHOT_PATH))

    rand_id = random.randint(0, 2)
    element = browser.find_element_by_id("id-preference-{}".format(rand_id))
    auction_id = element.get_attribute('data-auction-id')
    left_auction_id = browser.find_element_by_id("id-preference-1").get_attribute('data-auction-id')
    right_auction_id = browser.find_element_by_id("id-preference-2").get_attribute('data-auction-id')
    print("Stage 1: Selected Auction {} from ({}, {})".format(auction_id, left_auction_id, right_auction_id))
    element.click()
    # driver.find_element(By.ID, 'id-preference-0').click()
    browser.find_element(By.XPATH, '//button').click()


def play_phase_two_screen(browser, round_number):
    if round_number == 1:
        browser.save_screenshot('{}/phase_two_choice_screen.png'.format(SCREEN_SHOT_PATH))

    min_value = int(browser.find_element_by_id('cutoff').get_attribute('min'))
    max_value = int(browser.find_element_by_id('cutoff').get_attribute('max'))
    random_cutoff = random.randint(min_value, max_value)
    print("Stage 2: Selected Cutoff {}".format(random_cutoff))
    browser.execute_script("""$('input[type="range"]').val({}).change();""".format(random_cutoff))
    browser.find_element(By.XPATH, "//input[@id='clicked']").value = '1'
    browser.find_element(By.XPATH, '//button').click()


def play_phase_three_screen(browser, round_number):
    if round_number == 1:
        browser.save_screenshot('{}/phase_three_choice_screen.png'.format(SCREEN_SHOT_PATH))

    min_value = int(browser.find_element_by_id("id_bid").get_attribute('data-min'))
    max_value = int(browser.find_element_by_id("id_bid").get_attribute('data-max'))
    input_field = browser.find_element(By.XPATH, "//input[@id='id_bid']")
    input_field.clear()
    random_bid = random.randint(min_value, max_value)
    print("Stage 3: Entered Bid {}".format(random_bid))
    input_field.send_keys(str(random_bid))
    browser.find_element(By.XPATH, '//button').click()


def play_phase_four_screen(browser, round_number):
    browser.save_screenshot('{}/phase_four_choice_screen_round_{}.png'.format(round_number, SCREEN_SHOT_PATH))

    browser.find_element(By.XPATH, "//input[@id='clicked']").value = '1'
    if random.randint(0, 1) == 0:
        print('Stage 4: Betting high on Red')
        browser.find_element(By.XPATH, "//button[@id='red-bet-button']").click()
    else:
        print('Stage 4: Betting high on Blue')
        browser.find_element(By.XPATH, "//button[@id='blue-bet-button']").click()

    browser.execute_script("""$('input[type="range"]').val({}).change();""".format(random.randint(0, 10)))
    browser.find_element(By.XPATH, "//button[@id='next-button']").click()


def print_links(links):
    print("Player Links: ")
    for link in links:
        print(link.get_attribute('href'))


def play_roll_die(browser):
    browser.save_screenshot('{}/phase_four_roll_die_screen.png'.format(SCREEN_SHOT_PATH))
    browser.find_element(By.XPATH, "//button[@id='die-button']").click()
    die_side = int(browser.find_element_by_id("side").get_attribute('value'))
    print("Stage 4: Rolled Die Side {}".format(die_side))

    browser.find_element(By.XPATH, "//button[@id='next-button']").click()


def play_phase_one(browser):
    print('--Stage 1--')
    play_instructions(browser, 'one')
    for round_number in range(Experiment.phase_one_rounds()):
        play_phase_one_screen(browser, round_number)


def play_phase_two(browser):
    print('--Stage 2--')
    play_instructions(browser, 'two')
    for round_number in range(Experiment.phase_two_rounds()):
        play_phase_two_screen(browser, round_number)


def play_phase_three(browser):
    print('--Stage 3--')
    play_instructions(browser, 'three')
    for round_number in range(Experiment.phase_three_rounds()):
        play_phase_three_screen(browser, round_number)


def play_phase_four(browser):
    print('--Stage 4--')
    play_instructions(browser, 'four')
    play_roll_die(browser)
    for round_number in range(Experiment.phase_four_rounds()):
        play_phase_four_screen(browser, round_number)


def play_payoffs(browser):
    print('--Stage Payoffs--')

    browser.save_screenshot('{}/earnings_1.png'.format(SCREEN_SHOT_PATH))
    browser.find_element(By.XPATH, "//button[@id='next-button']").click()

    browser.save_screenshot('{}/earnings_2.png'.format(SCREEN_SHOT_PATH))
    browser.find_element(By.XPATH, "//button[@id='next-button']").click()

    browser.save_screenshot('{}/earnings_measurement_stage.png'.format(SCREEN_SHOT_PATH))
    browser.find_element(By.XPATH, "//button[@id='next-button']").click()

    browser.save_screenshot('{}/total_earnings.png'.format(SCREEN_SHOT_PATH))
    browser.find_element(By.XPATH, "//button[@id='next-button']").click()


def delete_old_screen_shots():
    files = glob.glob(SCREEN_SHOT_PATH + '/*')
    for f in files:
        os.remove(f)


# Run with python -m browser_tests.browser_test
if __name__ == "__main__":
    delete_old_screen_shots()
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument('--window-size=1200,900')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(30)

    driver.get(SITE_URL)
    links = driver.find_elements_by_partial_link_text("InitializeParticipant")
    for i in range(len(links)):
        driver.switch_to.window(driver.window_handles[0])
        links[i].send_keys(Keys.COMMAND + Keys.ENTER)
        print("Opening browser tab {}".format(i+1))
        driver.switch_to.window(driver.window_handles[i+1])
        play_phase_one(driver)
        play_phase_two(driver)
        play_phase_three(driver)
        play_phase_four(driver)

    driver.set_window_size(1200, 1750)
    for i in range(len(links)):
        driver.switch_to.window(driver.window_handles[i+1])
        play_payoffs(driver)
