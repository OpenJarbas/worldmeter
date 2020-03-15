from setuptools import setup

setup(
    name='covid_reports',
    version='0.1',
    packages=['covid_reports'],
    url='https://github.com/OpenJarbas/covid_reports',
    license='MIT',
    author='jarbasAI',
    install_requires=["bs4", "requests"],
    author_email='jarbasai@mailfence.com',
    description='covid-19 daily data'
)
