from pprint import pprint

from rivombrosa.marchingegno.shin import get_real_odds
from rivombrosa.sites.marathon import get_prices as get_marathon_prices
from rivombrosa.sites.pinnacle import get_prices as get_pinnacle_prices

pinnacle_data = get_pinnacle_prices()
marathon_data = get_marathon_prices()

tier_1 = [] # 0.8 in su
tier_2 = [] # 0.5 < x < 0.8
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
        if value_coeffs[k]['coeff'] > 0.8:
            tier_1.append({f'{match} {k}': value_coeffs[k]})
        elif value_coeffs[k]['coeff'] > 0.5:
            tier_2.append({f'{match} {k}': value_coeffs[k]})

print('Tier 1')
pprint(tier_1)
print()
print('Tier 2')
pprint(tier_2)

