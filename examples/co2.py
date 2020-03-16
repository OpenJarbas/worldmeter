from worldmeter.co2 import Co2Meter

c = Co2Meter()

data = c.get_global_data()
"""
{
'country': 'world',
 'date': 2016,
 'population': 7457840363.0,
 'total_emissions': 34565977532.0  # Tons
 }
"""

data = c.get_country_data("Portugal")  # country names, NOT country code

"""
{'1year_change': -2.36,  # percent
 'country': 'Portugal',
 'date': 2016,
 'per_capita': 4.86,
 'population': 10325538.0,
 'share': 0.14,
 'tons': 50142844.0}
"""