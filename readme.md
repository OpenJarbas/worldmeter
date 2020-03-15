# Covid Reports

python api for https://www.worldometers.info/coronavirus/

Daily number reports for covid-19 cases

## Usage


```python
from covid_reports import CovidScrapper

c = CovidScrapper()

data = c.global_data()
```

output
```json
{
 'active_cases': 96892,
 'country': 'world',
 'critical': 5774,
 'date': '2020/03/15',
 'new_cases': 7624,
 'new_deaths': 304,
 'total_cases': 180448,
 'total_deaths': 6355,
 'total_recovered': 77201,
 }
```

```python
from covid_reports import CovidScrapper

c = CovidScrapper()

data = c.get_country_data("Portugal")  # country names, NOT country code
```

output
```json
{
'country': 'Portugal', 
'total_cases': '245', 
'new_cases': 76, 
'total_deaths': 0, 
'new_deaths': 0, 
'total_recovered': 2, 
'active_cases': 243, 
'critical': 9, 
'cases_per_1M': 24.0, 
'date': '2020/03/15',
}
```

## Install

```bash
pip install covid_reports
```
