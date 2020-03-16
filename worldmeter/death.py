import requests
from bs4 import BeautifulSoup
import time
from worldmeter.util import now_utc
from worldmeter.population import PopulationMeter


class DeathMeter:
    def __init__(self, dateformat="YMD"):
        self.base_url = 'http://deathmeters.info/'
        self._data = {}
        self._scrapped = False
        self.date_format = dateformat
        self._aux_scrapper = PopulationMeter(dateformat)
        assert dateformat in ["DMY", "YMD", "MDY", "unix"]

    def update(self):
        html = requests.get(self.base_url).text
        soup = BeautifulSoup(html, 'html.parser')

        deaths = []
        for div in soup.find_all('td', class_='death_name'):
            death_name = div.text.split("\t")[0].strip()
            deaths.append(death_name)

        top20 = {}
        for idx, div in enumerate(soup.find_all('td', class_='death_perc')):
            top20[deaths[idx]] = float(div.text.replace("%", ""))

        self._data["top_causes"] = top20
        self._data["yearly_deaths"] = self._aux_scrapper.deaths("year")
        self._data["daily_deaths"] = self._aux_scrapper.deaths("day")
        self._scrapped = True

    def death_numbers(self, timescale="day"):

        if not self._scrapped:
            self.update()

        top_deaths = self.death_percent()

        if timescale == "day":
            deaths = self._data["daily_deaths"]
        else:
            deaths = self._data["yearly_deaths"]

        deaths_in_timescale = {}

        for cause in top_deaths:
            percent = top_deaths[cause]
            deaths_in_timescale[cause] = (int(percent * (deaths / 100)))

        return deaths_in_timescale

    def death_percent(self):

        if not self._scrapped:
            self.update()

        return self._data["top_causes"]

    def get_death_data(self):
        if self.date_format == "DMY":
            now = now_utc().strftime("%d/%m/%Y")
        elif self.date_format == "YMD":
            now = now_utc().strftime("%Y/%m/%d")
        elif self.date_format == "MDY":
            now = now_utc().strftime("%m/%d/%Y")
        else:
            now = time.time()

        return {
            "date": now,
            "top20_death_causes": self.death_percent(),
            "deaths_today": self.death_numbers(),
            "daily": self._data["daily_deaths"],
            "yearly": self._data["yearly_deaths"]
        }
