import bs4
from bs4 import BeautifulSoup
import requests
import time
from worldmeter.util import match_one, now_utc


class Worldometer:
    def __init__(self, dateformat="YMD"):
        self.base_url = "http://deathmeters.info/"
        self._data = {}
        self._scrapped = False
        self.date_format = dateformat
        assert dateformat in ["DMY", "YMD", "MDY", "unix"]

    def update(self):
        r = requests.get(self.base_url)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        self._scrapped = True

        if self.date_format == "DMY":
            now = now_utc().strftime("%d/%m/%Y")
        elif self.date_format == "YMD":
            now = now_utc().strftime("%Y/%m/%d")
        elif self.date_format == "MDY":
            now = now_utc().strftime("%m/%d/%Y")
        else:
            now = time.time()
        return
        for country_data in soup.find_all("div", {"class": "counter-group"}):
            print(country_data.find("span", {"class": "counter-number"}))
            continue
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

w = Worldometer()
w.update()