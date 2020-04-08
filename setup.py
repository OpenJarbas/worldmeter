from setuptools import setup

setup(
    name='worldmeter',
    version='0.2.0',
    packages=['worldmeter'],
    url='https://github.com/OpenJarbas/worldmeter',
    license='MIT',
    author='jarbasAI',
    install_requires=["bs4", "requests", "python-dateutil==2.6.0"],
    author_email='jarbasai@mailfence.com',
    description='stats for the world'
)
