from setuptools import setup

setup(
   name='etl',
   version='0.0.1',
   description='Classes for ETL processes',
   author='Speedimus Maximus',
   author_email='speedy@ownjoo.org',
   packages=['etl'],
   install_requires=['pydantic',], #external packages as dependencies
)