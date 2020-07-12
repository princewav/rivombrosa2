from pprint import pprint, pformat

from rivombrosa.config import urls_per_country, tiers
from rivombrosa.marchingegno.shin import get_real_odds, calcola_e, calcola_x
from rivombrosa.sites.marathon import get_prices as get_marathon_prices
from rivombrosa.sites.pinnacle import get_prices as get_pinnacle_prices

import clipboard


def get_tiers():
    for country, urls in urls_per_country.items():
        pinnacle_data = get_pinnacle_prices(urls['pinnacle'])
        marathon_data = get_marathon_prices(urls['marathon'])

        for match, pinnacle_odds in pinnacle_data.items():
            if pinnacle_odds:
                marathon_odds = marathon_data.get(match)
                real_odds = get_real_odds(pinnacle_odds)

                if marathon_odds:
                    real_odds_mara = get_real_odds(marathon_odds)
                    value_coeffs = {
                        '1': {'coeff': 1 / real_odds['1'] - 1 / marathon_odds['1'],
                              'marathon': marathon_odds['1'],
                              'stake': int(10 / (marathon_odds['1'] - 1)),
                              # 'allp': f'{pinnacle_odds["1"]} ({real_odds["1"]})  /// {pinnacle_odds["2"]} ({real_odds["2"]})',
                              # 'allm': f'{marathon_odds["1"]} ({real_odds_mara["1"]}) /// {marathon_odds["2"]} ({real_odds_mara["2"]})',
                              # 'ep': {1: calcola_e(20, pinnacle_odds['1'], real_odds['1']), 2: calcola_e(20, pinnacle_odds['2'], real_odds['2'])},
                              # 'em': {1: calcola_e(20, marathon_odds['1'], real_odds_mara['1']), 2: calcola_e(20, marathon_odds['2'], real_odds_mara['2'])},
                              # 'esps': {1: calcola_e(20, marathon_odds['1'], real_odds['1']), 2: calcola_e(20, marathon_odds['2'], real_odds['2'])},
                              'stakeone': {1: calcola_x(1, marathon_odds['1'], real_odds['1']), 'x': calcola_x(1, marathon_odds['X'], real_odds['X']),
                                           2: calcola_x(1, marathon_odds['2'], real_odds['2'])},
                              # 'real': real_odds['1'],
                              # 'pinna': pinnacle_odds['1'],
                              # 'z': real_odds['z'],
                              # 'incr': (((1 / pinnacle_odds['1']) - (1 / real_odds['1'])) / (1 / pinnacle_odds['1'])) * 100,
                              # 'incrodds': ((real_odds['1'] - pinnacle_odds['1']) / pinnacle_odds['1']) * 100,
                              },
                        'X': {'coeff': 1 / real_odds['X'] - 1 / marathon_odds['X'],
                              'marathon': marathon_odds['X'],
                              'stake': int(10 / (marathon_odds['X'] - 1)),
                              'stakeone': {1: calcola_x(1, marathon_odds['1'], real_odds['1']), 'x': calcola_x(1, marathon_odds['X'], real_odds['X']),
                                           2: calcola_x(1, marathon_odds['2'], real_odds['2'])},
                              # 'all': f'{pinnacle_odds["1"]} ({real_odds["1"]})  /// \n{pinnacle_odds["2"]} ({real_odds["2"]})',
                              # 'allm': f'{marathon_odds["1"]} ({real_odds_mara["1"]}) /// {marathon_odds["2"]} ({real_odds_mara["2"]})',
                              # 'ep': {1: calcola_e(20, pinnacle_odds['1'], real_odds['1']), 2: calcola_e(20, pinnacle_odds['2'], real_odds['2'])},
                              # 'em': {1: calcola_e(20, marathon_odds['1'], real_odds['1']), 2: calcola_e(20, marathon_odds['2'], real_odds['2'])},
                              # 'esps': {1: calcola_e(20, marathon_odds['1'], real_odds['1']), 2: calcola_e(20, marathon_odds['2'], real_odds['2'])},
                              # 'z': real_odds['z'],
                              # 'real': real_odds['X'],
                              # 'pinna': pinnacle_odds['X'],
                              # 'incr': (((1 / pinnacle_odds['X']) - (1 / real_odds['X'])) / (1 / pinnacle_odds['X'])) * 100,
                              # 'incrodds': ((real_odds['X'] - pinnacle_odds['X']) / pinnacle_odds['X']) * 100,
                              },
                        '2': {'coeff': 1 / real_odds['2'] - 1 / marathon_odds['2'],
                              'marathon': marathon_odds['2'],
                              'stake': int(10 / (marathon_odds['2'] - 1)),
                              'stakeone': {1: calcola_x(1, marathon_odds['1'], real_odds['1']), 'x': calcola_x(1, marathon_odds['X'], real_odds['X']),
                                           2: calcola_x(1, marathon_odds['2'], real_odds['2'])},
                              # 'z': real_odds['z'],
                              # 'all': f'{pinnacle_odds["1"]} ({real_odds["1"]})  /// \n{pinnacle_odds["2"]} ({real_odds["2"]})',
                              # 'allm': f'{marathon_odds["1"]} ({real_odds_mara["1"]}) /// {marathon_odds["2"]} ({real_odds_mara["2"]})',
                              # 'ep': {1: calcola_e(20, pinnacle_odds['1'], real_odds['1']), 2: calcola_e(20, pinnacle_odds['2'], real_odds['2'])},
                              # 'em': {1: calcola_e(20, marathon_odds['1'], real_odds['1']), 2: calcola_e(20, marathon_odds['2'], real_odds['2'])},
                              # 'esps': {1: calcola_e(20, marathon_odds['1'], real_odds['1']), 2: calcola_e(20, marathon_odds['2'], real_odds['2'])},
                              # 'real': real_odds['2'],
                              # 'pinna': pinnacle_odds['2'],
                              # 'incr': (((1 / pinnacle_odds['2']) - (1 / real_odds['2'])) / (1 / pinnacle_odds['2'])) * 100,
                              # 'incrodds': ((real_odds['2'] - pinnacle_odds['2']) / pinnacle_odds['2']) * 100,
                              },
                    }
                    for k in value_coeffs:
                        value_coeffs[k]['coeff'] = round((value_coeffs[k]['coeff'] * 100), 3)

                    for k in value_coeffs:
                        if value_coeffs[k]['coeff'] > 1.25:
                            tiers[country]['tier_1'].append({'match': f'{match}', 'outcome': k, **value_coeffs[k]})
                        elif value_coeffs[k]['coeff'] > 1:
                            tiers[country]['tier_2'].append({'match': f'{match}', 'outcome': k, **value_coeffs[k]})
                        elif value_coeffs[k]['coeff'] > 0.75:
                            tiers[country]['tier_3'].append({'match': f'{match}', 'outcome': k, **value_coeffs[k]})

    return (tiers)


if __name__ == '__main__':
    tiers = get_tiers()
    pprint(tiers)
    clipboard.copy(pformat(tiers))
