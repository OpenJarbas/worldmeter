# Worldmeter


THIS IS CURRENTLY BROKEN

please check https://covid-19-apis.postman.com/ for alternatives

Webscrapping might break at any time, i do not want downstream apps using this and potentially breaking at a critical time



Daily number reports for covid-19 cases and other causes of death

python api for worldometers.info and deathmeters.info


## Install

```bash
pip install worldmeter
```

## Usage

### Coronavirus stats

```python
from worldmeter.coronavirus import CovidMeter

c = CovidMeter()

data = c.global_data()
"""
{'active_cases': 109014,
 'country': 'world',
 'critical': 6099,
 'date': '2020/03/16',
 'new_cases': 7347,
 'new_deaths': 220,
 'total_cases': 195211,
 'total_deaths': 7006,
 'total_recovered': 79191}
"""

data = c.get_country_data("Portugal")  # country names, NOT country code
"""
{'active_cases': 327,
 'cases_per_1M': 32.5,
 'country': 'Portugal',
 'critical': 18,
 'date': '2020/03/16',
 'new_cases': 86,
 'new_deaths': 1,
 'total_cases': 331,
 'total_deaths': 1,
 'total_recovered': 3}
"""
```

### Death Causes across the world

```python
from worldmeter.death import DeathMeter

c = DeathMeter()

data = c.get_death_data()

"""
{'daily': 121384,
 'yearly': 11883313,
 'date': '2020/03/16',
 'deaths_today': {'Alzheimer disease and other dementias': 3313,
                  'Birth asphyxia and birth trauma': 1493,
                  'Chronic obstructive pulmonary disease': 6821,
                  'Cirrhosis of the liver': 2500,
                  'Colorectal cancer': 1662,
                  'Coronary artery disease Coronary artery disease or Ischaemic heart disease.': 18826,
                  'Diabetes mellitus': 3410,
                  'Diarrhoeal diseases': 2986,
                  'HIV / AIDS': 2282,
                  'Hypertensive heart disease': 2027,
                  'Kidney diseases': 2427,
                  'Liver cancer': 1699,
                  'Lower respiratory tract infection': 6858,
                  'Preterm birth complications': 2282,
                  'Road injury': 2888,
                  'Stomach cancer': 1626,
                  'Stroke': 13425,
                  'Suicide': 1699,
                  'Trachea, bronchus, lung cancers': 3641,
                  'Tuberculosis': 2949},
 'top20_death_causes': {'Alzheimer disease and other dementias': 2.73,
                        'Birth asphyxia and birth trauma': 1.23,
                        'Chronic obstructive pulmonary disease': 5.62,
                        'Cirrhosis of the liver': 2.06,
                        'Colorectal cancer': 1.37,
                        'Coronary artery disease Coronary artery disease or Ischaemic heart disease.': 15.51,
                        'Diabetes mellitus': 2.81,
                        'Diarrhoeal diseases': 2.46,
                        'HIV / AIDS': 1.88,
                        'Hypertensive heart disease': 1.67,
                        'Kidney diseases': 2.0,
                        'Liver cancer': 1.4,
                        'Lower respiratory tract infection': 5.65,
                        'Preterm birth complications': 1.88,
                        'Road injury': 2.38,
                        'Stomach cancer': 1.34,
                        'Stroke': 11.06,
                        'Suicide': 1.4,
                        'Trachea, bronchus, lung cancers': 3.0,
                        'Tuberculosis': 2.43}
}
"""
```

### Population data

```python
from worldmeter.population import PopulationMeter

c = PopulationMeter()

data = c.get_population_data()
"""
{'births': 306859,
 'date': '2020/03/16',
 'deaths': 121803,
 'total': 7782911150,
 'total_female': 3857149794,
 'total_male': 3925761356}
"""

```


