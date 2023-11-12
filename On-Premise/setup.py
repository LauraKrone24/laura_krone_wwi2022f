from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory+"/doc", 'ReadMe.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='Big Data Abgabe On-Premise Laura Krone',
      version='1.0',
      description='Dies ist eine Abgabe für das Modul Big Data ',
      url='https://git.dhbw-stuttgart.de/laurakrone/wwi2022f_laurakrone.git',
      python_requires='==3.12.0',
      setup_requires=['setuptools-pep8'],
      author='Laura Krone',
      author_email='wi22001@lehre.dhbw-stuttgart.de',
      exclude_package_data = {"": ["binary, doc"]},
      long_description = long_description,
      license='MIT',
      packages=find_packages('src', exclude=["tests"]),
      package_dir={'':'src'},
      test_suite="tests",
      #include here all binary variables
      install_requires = ['pyspark >= 2.4.8', 'pandas >= 1.0.1', 'xlrd >= 1.0.0', 'psutil >=5.9'],
      zip_safe=False)
