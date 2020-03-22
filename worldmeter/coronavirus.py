import bs4
from bs4 import BeautifulSoup
import requests
import time
from worldmeter.util import match_one, now_utc


class CovidMeter:
    def __init__(self, dateformat="YMD"):
        self.base_url = "https://www.worldometers.info/coronavirus/"
        self._by_country = {}
        self._scrapped = False
        self.date_format = dateformat
        assert dateformat in ["DMY", "YMD", "MDY", "unix"]

    def update(self):
        r = requests.get(self.base_url)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        self._scrapped = True

        table = soup.find("tbody")

        if self.date_format == "DMY":
            now = now_utc().strftime("%d/%m/%Y")
        elif self.date_format == "YMD":
            now = now_utc().strftime("%Y/%m/%d")
        elif self.date_format == "MDY":
            now = now_utc().strftime("%m/%d/%Y")
        else:
            now = time.time()
        for country_data in table:
            if not isinstance(country_data, bs4.element.Tag):
                continue
            try:
                data = country_data.find_all("td")
                data = [d.text.replace(",", "").replace("+", "").strip() or
                        "0" for d in data]
                name = data[0]
                self._by_country[name.lower()] = {
                    "country": name,
                    "total_cases": int(data[1]),
                    "new_cases": int(data[2]),
                    "total_deaths": int(data[3]),
                    "new_deaths": int(data[4]),
                    "total_recovered": int(data[5]),
                    "active_cases": int(data[6]),
                    "critical": int(data[7]),
                    "cases_per_1M": float(data[8]),
                    "date": now
                }
            except Exception as e:
                pass

    def get_country_data(self, country):
        if not self._scrapped:
            self.update()

        country = country.lower().strip()

        # HACK this is a quick and dirty way to match country names
        if country in ["united kingdom", "england"]:
            country = "uk"
        elif country in ["united states", "united states america",
                       "united states of america", "u.s.a."]:
            country = "usa"
        elif country in ["south korea", "s korea"]:
            country = "s. korea"

        return self._by_country.get(country) or \
               match_one(country, self._by_country)

    def total_new_deaths(self):
        total = 0
        if not self._scrapped:
            self.update()
        for c in self._by_country:
            total += self._by_country[c]["new_deaths"]
        return total

    def total_new_cases(self):
        total = 0
        if not self._scrapped:
            self.update()
        for c in self._by_country:
            total += self._by_country[c]["new_cases"]
        return total

    def total_cases(self):
        total = 0
        if not self._scrapped:
            self.update()
        for c in self._by_country:
            total += self._by_country[c]["total_cases"]
        return total

    def total_active_cases(self):
        total = 0
        if not self._scrapped:
            self.update()
        for c in self._by_country:
            total += self._by_country[c]["active_cases"]
        return total

    def total_critical_cases(self):
        total = 0
        if not self._scrapped:
            self.update()
        for c in self._by_country:
            total += self._by_country[c]["critical"]
        return total

    def total_recoveries(self):
        total = 0
        if not self._scrapped:
            self.update()
        for c in self._by_country:
            total += self._by_country[c]["total_recovered"]
        return total

    def total_deaths(self):
        total = 0
        if not self._scrapped:
            self.update()
        for c in self._by_country:
            total += self._by_country[c]["total_deaths"]
        return total

    def global_data(self):
        if self.date_format == "DMY":
            now = now_utc().strftime("%d/%m/%Y")
        elif self.date_format == "YMD":
            now = now_utc().strftime("%Y/%m/%d")
        elif self.date_format == "MDY":
            now = now_utc().strftime("%m/%d/%Y")
        else:
            now = time.time()

        return {
                    "country": "world",
                    "total_cases": self.total_cases(),
                    "new_cases": self.total_new_cases(),
                    "total_deaths": self.total_deaths(),
                    "new_deaths": self.total_new_deaths(),
                    "total_recovered":self.total_recoveries(),
                    "active_cases": self.total_active_cases(),
                    "critical": self.total_critical_cases(),
                    "date": now
                }
