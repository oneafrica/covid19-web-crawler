countries_map = ['Angola', 'Burkina Faso', 'Burundi', 'Benin', 'Botswana', 'DRC', 'CAR', 'Congo',  'Ivory Coast',
                'Cameroon', 'Cabo Verde', 'Djibouti', 'Algeria', 'Egypt', 'Western Sahara', 'Eritrea', 'Ethiopia',
                'Gabon', 'Ghana', 'Gambia', 'Guinea', 'Equatorial Guinea', 'Guinea-Bissau', 'Kenya', 'Comoros', 
                'Liberia', 'Lesotho', 'Libya', 'Morocco', 'Madagascar', 'Mali', 'Mauritania', 'Mauritius', 'Malawi', 'Mozambique', 
                'Namibia', 'Niger', 'Nigeria', 'Seychelles', 'Rwanda', 'Sudan', 'Sierra Leone', 'Senegal', 'Somalia', 'South Sudan',
                'Sao Tome and Principe', 'Eswatini', 'Chad', 'Togo', 'Tunisia', 'Tanzania', 'Uganda', 'South Africa',
                'Zambia', 'Zimbabwe']

def fill_country_object(rows):
    countries = {}
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]

        country = {
            'name': cols[0],
            'totalCases': cols[1],
            'newCases': cols[2],
            'totalDeaths': cols[3],
            'newDeaths': cols[4],
            'totalRecovered': cols[5],
            'activeCases': cols[6],
            'seriousCritical': cols[7],
            'totalCasesByMillionPop': cols[8],
            'totalDeathsByMillionPop': cols[9],
            'totalTests': cols[10],
            'totalTestsByMillionPop': cols[11],
        }
        countries[country['name']] = country
    return countries

def fill_african_country_object(rows):
    countries = {}
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]

        country = {
            'name': cols[0],
            'totalCases': cols[1],
            'newCases': cols[2],
            'totalDeaths': cols[3],
            'newDeaths': cols[4],
            'totalRecovered': cols[5],
            'activeCases': cols[6],
            'seriousCritical': cols[7],
            'totalCasesByMillionPop': cols[8],
            'totalDeathsByMillionPop': cols[9],
            'totalTests': cols[10],
            'totalTestsByMillionPop': cols[11],
        }
        if country['name'] in countries_map:
            countries[country['name']] = country
    return countries

def delete_first_row(rows):
    temporary = []
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        temporary.append(cols)
    del temporary[0]
    return temporary