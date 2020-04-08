import bs4
from bs4 import BeautifulSoup
import requests
from worldmeter.util import match_one
from dateutil import parser


class CovidMeter:
    def __init__(self, dateformat="YMD"):
        self.base_url = "https://www.worldometers.info/coronavirus/"
        self._by_country = {}
        self._scrapped = False
        self.date_format = dateformat
        self.last_updated = None
        self.last_updated_str = "never"
        assert dateformat in ["DMY", "YMD", "MDY", "unix"]

    def update(self):
        r = requests.get(self.base_url)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")

        _styles = "font-size:13px; color:#999; margin-top:5px; text-align:center"

        self.last_updated_str = soup.find("div", {"style": _styles}).text \
            .replace("Last updated: ", "")
        self.last_updated = parser.parse(self.last_updated_str)
        if self.date_format == "DMY":
            dt = self.last_updated.strftime("%d/%m/%Y")
        elif self.date_format == "YMD":
            dt = self.last_updated.strftime("%Y/%m/%d")
        elif self.date_format == "MDY":
            dt = self.last_updated.strftime("%m/%d/%Y")
        else:
            dt = self.last_updated.timestamp()
        dt += " " + str(self.last_updated.time())

        for country_data in soup.find("tbody"):
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
                    "date": dt
                }
            except Exception as e:
                pass

        self._scrapped = True

    def get_all_countries(self):
        if not self._scrapped:
            self.update()
        return self._by_country

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
        if not self._scrapped:
            self.update()
        return self._by_country["world"]["new_deaths"]

    def total_new_cases(self):
        if not self._scrapped:
            self.update()
        return self._by_country["world"]["new_cases"]

    def total_cases(self):
        if not self._scrapped:
            self.update()
        return self._by_country["world"]["total_cases"]

    def total_active_cases(self):
        if not self._scrapped:
            self.update()
        return self._by_country["world"]["active_cases"]

    def total_critical_cases(self):
        if not self._scrapped:
            self.update()
        return self._by_country["world"]["critical"]

    def total_recoveries(self):
        if not self._scrapped:
            self.update()
        return self._by_country["world"]["total_recovered"]

    def total_deaths(self):
        if not self._scrapped:
            self.update()
        return self._by_country["world"]["total_deaths"]

    def global_data(self):
        if not self._scrapped:
            self.update()
        return self._by_country["world"]
