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
