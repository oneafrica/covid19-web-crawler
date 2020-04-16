import requests
from bs4 import BeautifulSoup
from ...utils import fill_country_object
from ...utils import fill_african_country_object, countries_map

from . import home_blueprint

from flask import current_app

@home_blueprint.route('/')
def home():
    response = requests.get(
        'https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')

    confirmedCases = soup.find_all(
        'div', class_='maincounter-number')[0].text.strip(' ').strip('\n')
    deathCases = soup.find_all(
        'div', class_='maincounter-number')[1].text.strip(' ').strip('\n')
    recovered = soup.find_all(
        'div', class_='maincounter-number')[2].text.strip(' ').strip('\n')
    closedCases = soup.find_all('div', class_='number-table-main')[1].text
    lastUpdate = soup.find_all(
        'div', style='font-size:13px; color:#999; margin-top:5px; text-align:center')[0].text
    activeCases = soup.find_all(class_='number-table-main')[0].text
    activeCasesMildCondition = soup.find_all(class_='number-table')[0].text
    activeCasesSeriousCondition = soup.find_all(class_='number-table')[1].text

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    countries = fill_country_object(rows)

    return {'confirmedCases': confirmedCases, 'deathCases': deathCases, "recovered": recovered,
            'closedCases': closedCases, 'countries': countries, 'lastUpdate': lastUpdate, 'activeCases': activeCases,
            'activeCasesMildCondition': activeCasesMildCondition,
            'activeCasesSeriousCondition': activeCasesSeriousCondition}


@home_blueprint.route('/api/v1/africa')
def africa():
    response = requests.get(
        'https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')

    # confirmedCases = soup.find_all(
    #     'div', class_='maincounter-number')[0].text.strip(' ').strip('\n')
    # deathCases = soup.find_all(
    #     'div', class_='maincounter-number')[1].text.strip(' ').strip('\n')
    # recovered = soup.find_all(
    #     'div', class_='maincounter-number')[2].text.strip(' ').strip('\n')
    # closedCases = soup.find_all('div', class_='number-table-main')[1].text
    lastUpdate = soup.find_all(
        'div', style='font-size:13px; color:#999; margin-top:5px; text-align:center')[0].text
    # activeCases = soup.find_all(class_='number-table-main')[0].text
    # activeCasesMildCondition = soup.find_all(class_='number-table')[0].text
    # activeCasesSeriousCondition = soup.find_all(class_='number-table')[1].text

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    countries = fill_african_country_object(rows)

    confirmedCases = 0
    deathCases = 0
    recovered = 0
    activeCasesSeriousCondition = 0
    

    for country in countries_map:
        if  country in countries:
            confirmedCases += int(countries[country]['totalCases'].replace(',', ''))
            if countries[country]['totalDeaths'].strip():
                deathCases += int(countries[country]['totalDeaths'].replace(',', ''))
            if countries[country]['totalRecovered'].strip():
                recovered += int(countries[country]['totalRecovered'].replace(',', ''))
            if countries[country]['seriousCritical'].strip():
                activeCasesSeriousCondition += int(countries[country]['seriousCritical'].replace(',', ''))
    
    
    closedCases = deathCases + recovered
    activeCases = confirmedCases - closedCases
    activeCasesMildCondition = activeCases - activeCasesSeriousCondition


    return {'confirmedCases': str(format(confirmedCases, ',d')), 'deathCases': str(format(deathCases, ',d')), "recovered": str(format(recovered, ',d')),
            'closedCases': str(format(closedCases, ',d')), 'countries': countries, 'lastUpdate': lastUpdate, 'activeCases': str(format(activeCases, ',d')),
            'activeCasesMildCondition': str(format(activeCasesMildCondition, ',d')),
            'activeCasesSeriousCondition': str(format(activeCasesSeriousCondition, ',d'))}

@home_blueprint.route('/api/v1/africa-cdc')
def africacdc():
    response = requests.get('https://africacdc.org/covid-19/').content
    soup = BeautifulSoup(response, 'html.parser')

    current_app.logger.info(soup)

    return soup
