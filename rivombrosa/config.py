headers = {
    'authority': 'guest.api.arcadia.pinnacle.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json',
    'x-device-uuid': 'e5f83264-4afb5bcf-47bea0d1-93b5b53f',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'x-api-key': 'CmX2KcMrXuFmNg6YFbmTxE0y9CIrOi0R',
    'content-type': 'application/json',
    'origin': 'https://www.pinnacle.bet',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.pinnacle.bet/it/soccer/italy-serie-a/matchups/',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,nl;q=0.6',
}

teams_mapping = {
    'pinnacle': {'Torino': 'Torino', 'Lazio': 'Lazio', 'Genoa': 'Genoa', 'Juventus': 'Juventus', 'Bologna': 'Bologna', 'Cagliari': 'Cagliari', 'FC Internazionale': 'Inter',
                 'Brescia': 'Brescia', 'Fiorentina': 'Fiorentina', 'Sassuolo': 'Sassuolo', 'Lecce': 'Lecce', 'Sampdoria': 'Sampdoria', 'SPAL': 'SPAL', 'AC Milan': 'Milan',
                 'Hellas Verona FC': 'Verona', 'Parma FC': 'Parma', 'Atalanta BC': 'Atalanta', 'Napoli': 'Napoli', 'AS Roma': 'Roma', 'Udinese': 'Udinese'},
    'marathon': {'Torino': 'Torino', 'Lazio': 'Lazio', 'Genoa': 'Genoa', 'Juventus': 'Juventus', 'Bologna': 'Bologna', 'Cagliari': 'Cagliari', 'Inter': 'Inter',
                 'Brescia': 'Brescia', 'Fiorentina': 'Fiorentina', 'Sassuolo': 'Sassuolo', 'Lecce': 'Lecce', 'Sampdoria': 'Sampdoria', 'SPAL': 'SPAL', 'Milan': 'Milan',
                 'Verona': 'Verona', 'Parma': 'Parma', 'Atalanta': 'Atalanta', 'Napoli': 'Napoli', 'Roma': 'Roma', 'Udinese': 'Udinese'},
}

EXPECTED_EARNING = 10
