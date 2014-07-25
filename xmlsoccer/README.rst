XmlSoccer
--------

To use (with caution), simply do::

    xmlsoccer = XmlSoccer(api_key='''GCVMINBHMWBPAJCAFTPREBLHPELIKMDNMWRESVUTPQBXOOAWWQ''',
                          use_demo=True)

    fixtures = xmlsoccer.call_api(method='GetHistoricMatchesByLeagueAndSeason',
                                  seasonDateString='1314',
                                  league='English Premier League')

    teams = xmlsoccer.call_api(method='GetAllTeams')

    leagues = xmlsoccer.call_api(method='GetAllLeagues')

    standings = xmlsoccer.call_api(method='GetLeagueStandingsBySeason',
                                   seasonDateString='1314',
                                   league='Scottish Premier League')