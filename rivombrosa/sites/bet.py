from bs4 import BeautifulSoup

from rivombrosa.config import teams_mapping
from rivombrosa.utilitites.utils import subdivide

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

book = 'bet'
user_agent = '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'

def get_prices(url):
    options = Options()
    options.add_argument(user_agent)
    # options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    driver.set_window_position(0, 0)
    driver.set_window_size(375, 812)
    driver.get(url)

    try:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "gl-MarketGroup_Wrapper")))
        page = driver.page_source
    finally:
        driver.quit()
    soup = BeautifulSoup(page, 'html.parser')

    teams = subdivide([x.text for x in soup.select('.cm-ParticipantWithBookCloses_Name')], 2)

    odds_groups = [x.text for x in soup.select('.cm-ParticipantOddsWithHandicap_Odds')]
    odds_groups = [x for x in zip(*subdivide(odds_groups, len(odds_groups)/3))]

    # teams_map = teams_mapping[book]

    return {f'{team[0]} - {team[1]}': {'1': float(odds[0]), 'X': float(odds[1]), '2': float(odds[2])}
            for team, odds in zip(teams, odds_groups)}

if __name__ == '__main__':
    url = 'https://mobile.bet365.it/#/AC/B1/C1/D13/E49487629/F2/'
    prices = get_prices(url)
    print(prices)
