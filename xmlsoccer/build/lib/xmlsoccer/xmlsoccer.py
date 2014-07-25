import requests
from lxml import etree


class XmlSoccer(object):
    def __init__(self, api_key=None, use_demo=False):
        """Inits xmlsoccer class
        :param api_key: your api key
        :param use_demo: boolean whether to use the xmlsoccer demo account or not
        """
        self.api_key = api_key
        self.service_address = '''http://www.xmlsoccer.com/FootballData.asmx/'''
        self.demo_address = '''http://www.xmlsoccer.com/FootballDataDemo.asmx/'''
        self.demo = use_demo

    def set_api_key(self, api_key):
        """

        :param api_key: can set your api key here if not set via constructor
        """
        self.api_key = api_key

    def set_service_address(self, service_address):
        """

        :param service_address: can override xmlsoccer api address if required
        """
        self.service_address = service_address

    def set_demo_address(self, demo_address):
        """

        :param demo_address: can override demo api address if required
        """
        self.demo_address = demo_address

    def set_use_demo(self, use_demo):
        """

        :param use_demo: boolean whether to use xmlsoccer demo api or not
        """
        self.demo = use_demo

    def call_api(self, method=None, *args, **kwargs):
        """ Call the XMLSoccer API

        :param method: XMLSoccer function, e.g 'GetHistoricMatchesByLeagueAndSeason'
        :param args: E.g league, seasonString etc
        :param kwargs: .g league, seasonString etc
        :return: output from xmlsoccer as list of dicts
        :raise (Exception('Error: Method not passed to get_xmlsoccer')):
        """
        if method is None:
            raise(Exception('Error: Method not passed to call_api'))
        # create the url
        if not self.demo:
            address = self.service_address + method
        else:
            address = self.demo_address + method
        # create the request parameters
        params = dict()
        params['ApiKey'] = self.api_key
        for kwarg in kwargs:
            params[kwarg] = kwargs[kwarg]
        # list to store the data in
        data = []
        try:
            # make the request
            r = requests.get(address, params=params)
            # parse the xml
            root = etree.XML(r.text.encode('utf-8'))
            if len(root) == 0:
                raise(Exception(root.text))
            for child in list(root):
                tmp = dict()
                for element in list(child):
                    tmp[element.tag] = element.text
                data.append(tmp)
        except Exception, e:
            print str(e)
        # return the results
        return data


# def test():
    # xmlsoccer = XmlSoccer(api_key='''GCVMINBHMWBPAJCAFTPREBLHPELIKMDNMWRESVUTPQBXOOAWWQ''',
    #                       use_demo=False)
    #
    # fixtures = xmlsoccer.call_api(method='GetHistoricMatchesByLeagueAndSeason',
    #                               seasonDateString='1314',
    #                               league='English Premier League')
    #
    # teams = xmlsoccer.call_api(method='GetAllTeams')
    #
    # leagues = xmlsoccer.call_api(method='GetAllLeagues')
    #
    # standings = xmlsoccer.call_api(method='GetLeagueStandingsBySeason',
    #                                seasonDateString='1314',
    #                                league='Scottish Premier League')