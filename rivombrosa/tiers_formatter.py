import datetime

import clipboard

from rivombrosa.marchingegno.comparator import get_tiers

flags = {
    'italia': '🇮🇹',
    'inghilterra': '🇬🇧',
    'spagna': '🇪🇸',
    'portogallo': '🇵🇹',
    'russia': '🇷🇺',
}

all_tiers = get_tiers()
result = f'*{datetime.datetime.now().strftime("%A, %d %B %Y, %H:%M")}*\n\n'
for country, tiers in all_tiers.items():
    if any([len(tiers['tier_1']), len(tiers['tier_2']), len(tiers['tier_3'])]):
        result += f'{flags[country]} _{country.capitalize()}_\n'

        for i in range(1, 4):
            result += f'*Tier {i}:*\n'
            if len(tiers[f'tier_{i}']):
                for info in tiers[f'tier_{i}']:
                    result += f'{info["match"]} *{info["outcome"]}* / {info["marathon"]} *({info["coeff"]}%)* > € {info["stake"] or 1}\n'
            else:
                result += f'_Nessun match nel Tier {i}_\n'
        result += '\n'

print(result)
clipboard.copy(result)
