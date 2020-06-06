import requests
from bs4 import BeautifulSoup

class Deaths(object):
    def __init__(self, name):
        self.name = "Daily Deaths"

    def country():
        try:
            site = requests.get('https://www.worldometers.info/coronavirus/');
            deaths = ''
            if site.status_code is 200:
                soup = BeautifulSoup(site.content,"html.parser")
                tabl = soup.find_all(class_='table')
                td = tabl[0].find_all('td')

                counter = 0
                for t in td:
                    counter += 1
                    if counter == 158:
                        if t == ' ':
                            deaths = '0'
                            # print('none')
                        else:
                            deaths = t.text[1:]
            return int(deaths)
        except:
            print('couldn\'t fetch')

    def state():
        try:
            deaths = ''
            site = requests.get('https://www.worldometers.info/coronavirus/country/us/');
            if site.status_code is 200:
                soup = BeautifulSoup(site.content,"html.parser")
                tabl = soup.find_all(class_='table')
                td = tabl[0].find_all('td')

                counter = 0
                for t in td:
                    counter += 1
                    # print(counter, t)
                    if counter == 53:
                        f = t.text
                        if f == ' ':
                            deaths = '0'
                            # print('none')
                        else:
                            deaths = t.text[1:]
            return int(deaths)
        except:
            print("couldn\'t fetch")
    def city():
        try:
            deaths = ''
            site = requests.get('https://www.worldometers.info/coronavirus/usa/california/');
            if site.status_code is 200:
                soup = BeautifulSoup(site.content,"html.parser")
                tabl = soup.find_all(class_='table')
                td = tabl[0].find_all('td')

                counter = 0
                for t in td:
                    counter += 1
                    # print(counter, t)
                    if counter == 13:
                        f = t.text
                        if f == ' ':
                            deaths = '0'          
                            # print('none')
                        else:
                            deaths = t.text[1:]
            return int(deaths)
        except:
            print("couldn\'t fetch")
# print(country())
# print(state())
# print(city())