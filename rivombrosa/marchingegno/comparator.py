from pprint import pprint

from rivombrosa.config import urls_per_country, tiers
from rivombrosa.marchingegno.shin import get_real_odds
from rivombrosa.sites.marathon import get_prices as get_marathon_prices
from rivombrosa.sites.pinnacle import get_prices as get_pinnacle_prices


def get_tiers():
    for country, urls in urls_per_country.items():
        pinnacle_data = get_pinnacle_prices(urls['pinnacle'])
        marathon_data = get_marathon_prices(urls['marathon'])

        for match, pinnacle_odds in pinnacle_data.items():
            if pinnacle_odds:
                marathon_odds = marathon_data.get(match)
                real_odds = get_real_odds(pinnacle_odds)

                if marathon_odds:
                    value_coeffs = {
                        '1': {'coeff': 1 / real_odds['1'] - 1 / marathon_odds['1'], 'marathon': marathon_odds['1'], 'stake': int(10 / (marathon_odds['1'] - 1))},
                        'X': {'coeff': 1 / real_odds['X'] - 1 / marathon_odds['X'], 'marathon': marathon_odds['X'], 'stake': int(10 / (marathon_odds['X'] - 1))},
                        '2': {'coeff': 1 / real_odds['2'] - 1 / marathon_odds['2'], 'marathon': marathon_odds['2'], 'stake': int(10 / (marathon_odds['2'] - 1))},
                    }
                    for k in value_coeffs:
                        value_coeffs[k]['coeff'] = round((value_coeffs[k]['coeff'] * 100), 3)

                    for k in value_coeffs:
                        if value_coeffs[k]['coeff'] > 1.25:
                            tiers[country]['tier_1'].append({'match':f'{match}', 'outcome': k, **value_coeffs[k]})
                        elif value_coeffs[k]['coeff'] > 1:
                            tiers[country]['tier_2'].append({'match':f'{match}', 'outcome': k, **value_coeffs[k]})
                        elif value_coeffs[k]['coeff'] > 0.75:
                            tiers[country]['tier_3'].append({'match':f'{match}', 'outcome': k, **value_coeffs[k]})

    return(tiers)

if __name__ == '__main__':
    pprint(tiers)

