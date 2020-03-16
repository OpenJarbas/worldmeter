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