import requests
from bs4 import BeautifulSoup
import time
from worldmeter.util import now_utc


class PopulationMeter:
    def __init__(self, dateformat="YMD"):
        self.base_url = 'https://countrymeters.info/en/World'
        self._data = {}
        self._scrapped = False
        self.date_format = dateformat
        assert dateformat in ["DMY", "YMD", "MDY", "unix"]

    def update(self):
        html = requests.get(self.base_url).text
        soup = BeautifulSoup(html, 'html.parser')
        self._data["total"] = int(soup.find(id='cp1').text
                                  .replace(',', ''))
        self._data["male"] = int(soup.find(id='cp2').text
                                 .replace(',', ''))
        self._data["female"] = int(soup.find(id='cp3').text
                                   .replace(',', ''))

        self._data["daily_births"] = int(soup.find(id='cp7').text
                                         .replace(',', ''))
        self._data["yearly_births"] = int(soup.find(id='cp6').text
                                          .replace(',', ''))

        self._data["daily_deaths"] = int(soup.find(id='cp9').text
                                         .replace(',', ''))
        self._data["yearly_deaths"] = int(soup.find(id='cp8').text
                                          .replace(',', ''))

        top_deaths = soup.find('div', class_='death_top')
        top_deaths = top_deaths.text.replace(" %", "").splitlines()[4:-4]
        top_deaths = list(filter(None, top_deaths))
        while 'Connecting . . .' in top_deaths: top_deaths.remove(
            'Connecting . . .')
        self._data["death_causes"] = top_deaths
        self._scrapped = True

    def world_population(self, option='total'):
        if not self._scrapped:
            self.update()
        if option.lower() == 'total':
            return self._data["total"]

        elif option.lower() == 'male':
            return self._data["male"]

        elif option.lower() == 'female':
            return self._data["female"]

    def births(self, timescale="day"):

        if not self._scrapped:
            self.update()

        if timescale.lower() == 'year':
            return self._data["yearly_births"]

        if timescale.lower() == 'day':
            return self._data["daily_births"]

    def deaths(self, timescale="day"):

        if not self._scrapped:
            self.update()
        if timescale.lower() == 'year':
            return self._data["yearly_deaths"]

        if timescale.lower() == 'day':
            return self._data["daily_deaths"]

    def death_numbers(self, timescale="day"):

        if not self._scrapped:
            self.update()

        top_deaths = self._data["death_causes"]

        deaths = self.deaths(timescale=timescale)

        deaths_in_timescale = []

        for element in top_deaths[1::2]:
            deaths_in_timescale.append(int(float(element) * (deaths / 100)))

        top_deaths_causes_timescale = dict(
            zip(top_deaths[0::2], deaths_in_timescale))

        return top_deaths_causes_timescale

    def death_percent(self):

        if not self._scrapped:
            self.update()

        return self._data["death_causes"]

    def get_population_data(self):
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
            "total": self.world_population("total"),
            "total_male": self.world_population("male"),
            "total_female": self.world_population("female"),
            "births": self.births(),
            "deaths": self.deaths()
        }
