from pprint import pprint

import requests

from rivombrosa.config import headers

if __name__ == '__main__':
    # url = 'https://www.bet365.it/#/AC/B1/C1/D13/E49487629/F2/'
    url = 'https://www.bet365.it/SportsBook.API/web?lid=6&zid=0&pd=%23AC%23B1%23C1%23D13%23E49487629%23F2%23&cid=97&ctid=97'
    s = requests.Session()
    text = s.get(url, headers=headers).content.decode('utf-8')

    def parse_response(text):
        total = []
        sections = text.split('|')
        for section in sections:
            pairs = section.split(';')
            total.append({x.split('=')[0]: x.split('=')[1] for x in pairs if len(x.split('=')) == 2})
        return total

    pprint(parse_response(text))

