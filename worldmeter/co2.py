import bs4
from bs4 import BeautifulSoup
import requests
from worldmeter.util import match_one


class Co2Meter:
    def __init__(self):
        self.base_url = "https://www.worldometers.info/co2-emissions/co2-emissions-by-country/"
        self._by_country = {}
        self._scrapped = False

    def update(self):
        r = requests.get(self.base_url)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        self._scrapped = True

        table = soup.find("tbody")
        for country_data in table:
            if not isinstance(country_data, bs4.element.Tag):
                continue
            try:
                data = country_data.find_all("td")

                data = [d.text.replace(",", "").replace("+", "")
                            .replace("%", "").strip() or
                        "0" for d in data]
                name = data[1]
                self._by_country[name.lower()] = {
                    "country": name,
                    "tons": float(data[2]),
                    "1year_change": float(data[3]),
                    "population": float(data[4]),
                    "per_capita": float(data[5]),
                    "share": float(data[6]),
                    "date": 2016
                }
            except Exception as e:
                pass

    def get_country_data(self, country):
        if not self._scrapped:
            self.update()
        country = country.lower().strip()
        return self._by_country.get(country) or \
               match_one(country, self._by_country)

    def total_emissions(self):
        total = 0
        if not self._scrapped:
            self.update()
        for c in self._by_country:
            total += self._by_country[c]["tons"]
        return total

    def total_population(self):
        total = 0
        if not self._scrapped:
            self.update()
        for c in self._by_country:
            total += self._by_country[c]["population"]
        return total

    def get_global_data(self):
        return {
                    "country": "world",
                    "total_emissions": self.total_emissions(),
                    "population": self.total_population(),
                    "date": 2016
                }
