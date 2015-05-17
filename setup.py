from setuptools import setup

setup(name='westergaard_species',
      version='0.2',
      description=("Utilities typeset Westergaard's Species "
                   "Counterpoint analysis"),
      url='https://github.com/cryptonomicon314/westergaard-species.git',
      author='Cryptonomicon',
      author_email='cryptonomicon.314@gmail.com',
      license='MIT',
      packages=['westergaard_species'],
      install_requires=[
          'PyYAML',
          'iabjad'
      ],
      zip_safe=False)
