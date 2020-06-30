from pprint import pprint

from rivombrosa.marchingegno.shin import get_real_odds
from rivombrosa.sites.marathon import get_prices as get_marathon_prices
from rivombrosa.sites.pinnacle import get_prices as get_pinnacle_prices

urls_per_country = {
    'inghilterra': {'pinnacle': 'https://guest.api.arcadia.pinnacle.com/0.1/leagues/1980/matchups',
                    'marathon': 'https://www.marathonbet.it/it/betting/Football/England/Premier+League+-+21520'},
    'spagna': {'pinnacle': 'https://guest.api.arcadia.pinnacle.com/0.1/leagues/2196/matchups',
               'marathon': 'https://www.marathonbet.it/it/betting/Football/Spain/Primera+Division+-+8736'},
    'russia': {'pinnacle': 'https://guest.api.arcadia.pinnacle.com/0.1/leagues/2406/matchups',
               'marathon': 'https://www.marathonbet.it/it/betting/Football/Russia/Premier+League+-+22433'},
    'italia': {'pinnacle': 'https://guest.api.arcadia.pinnacle.com/0.1/leagues/2436/matchups',
               'marathon': 'https://www.marathonbet.it/it/popular/Football/Italy/Serie+A+-+22434'},
}

tiers = {
    'inghilterra': {'tier_1': [], 'tier_2': [], 'tier_3': []},
    'spagna': {'tier_1': [], 'tier_2': [], 'tier_3': []},
    'russia': {'tier_1': [], 'tier_2': [], 'tier_3': []},
    'italia': {'tier_1': [], 'tier_2': [], 'tier_3': []},
}
for country, urls in urls_per_country.items():
    pinnacle_data = get_pinnacle_prices(urls['pinnacle'])
    marathon_data = get_marathon_prices(urls['marathon'])

    for match, pinnacle_odds in pinnacle_data.items():
        real_odds = get_real_odds(pinnacle_odds)
        marathon_odds = marathon_data[match]
        value_coeffs = {
            '1': {'coeff': 1 / real_odds['1'] - 1 / marathon_odds['1'], 'marathon': marathon_odds['1'], 'stake': int(10 / (marathon_odds['1'] - 1))},
            'X': {'coeff': 1 / real_odds['X'] - 1 / marathon_odds['X'], 'marathon': marathon_odds['X'], 'stake': int(10 / (marathon_odds['X'] - 1))},
            '2': {'coeff': 1 / real_odds['2'] - 1 / marathon_odds['2'], 'marathon': marathon_odds['2'], 'stake': int(10 / (marathon_odds['2'] - 1))},
        }
        for k in value_coeffs:
            value_coeffs[k]['coeff'] = round((value_coeffs[k]['coeff'] * 100), 3)

        for k in value_coeffs:
            if value_coeffs[k]['coeff'] > 1.25:
                tiers[country]['tier_1'].append({f'{match} {k}': value_coeffs[k]})
            elif value_coeffs[k]['coeff'] > 1:
                tiers[country]['tier_2'].append({f'{match} {k}': value_coeffs[k]})
            elif value_coeffs[k]['coeff'] > 0.75:
                tiers[country]['tier_3'].append({f'{match} {k}': value_coeffs[k]})

pprint(tiers)