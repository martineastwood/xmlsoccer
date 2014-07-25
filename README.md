XmlSoccer Parser
=========

Simple Python client for interacting with the [XmlSoccer](http://www.xmlsoccer.com/) API.

# Basic Usage #

All of the XmlSoccer API methods can be accessed via the `call_api` function, as shown in the example below. 

```python
from xmlsoccer import xmlsoccer

xmls = XmlSoccer(api_key=YOUR_API_KEY, use_demo=False)

fixtures = xmls.call_api(method='GetHistoricMatchesByLeagueAndSeason',
                        seasonDateString='1314',
                        league='Scottish Premier League')
                        
teams = xmls.call_api(method='GetAllTeams')

leagues = xmls.call_api(method='GetAllLeagues')

standings = xmlsoccer.call_api(method='GetLeagueStandingsBySeason',
                               seasonDateString='1314',
                               league='English Premier League')
```

# compatibility #

The code has been successfully tested on Windows 7, OSX 10.9, Ubuntu and ElementaryOS Luna

Martin