from setuptools import setup

setup(name='tourneykiosk',
      version='0.0.0a',
      description='Tourney Kiosk with Autoseed and Player Lookup',
      url='https://github.com/Savestate2A03/tourney-kiosk',
      author='Savestate',
      author_email='savestate@sav.estate',
      license='MIT',
      packages=['tourneykiosk'],
      install_requires=['braacket', 'cherrypy'])