# Kryžiukai-Nuliukai Žaidimas

Šis projektas yra paprastas "Kryžiukai-Nuliukai" žaidimas, sukurtas naudojant Python. Žaidimas leidžia dviem žaidėjams paeiliui įvesti savo simbolius (X arba 0) į 3x3 žaidimo lentą. Žaidimas baigiasi, kai vienas iš žaidėjų surenka tris savo simbolius eilėje, stulpelyje ar įstrižainėje, arba kai lenta yra pilna, paskelbiant lygiąsias.

Projektas yra padalintas į dvi pagrindines dalis:
- `kryz_nul_module.py`: Šiame faile yra visos pagalbinės funkcijos, kurios tvarko žaidimo lentos kūrimą, spausdinimą ir laimėtojo tikrinimą.
- `main.py`: Pagrindinis failas, kuriame yra žaidimo logika ir žaidėjo galimos įvestys.

## Žaidimo ypatumai 
- Žaidimo pradžioje žaidėjai turi galimybę pasirinkti, pradedanti simbolį (X arba 0).
- Viso žaidimo eigoje žaidėjai gali nutraukti žaidimą į terminalą įvedę žodį "pabaiga".
- Programa kiekvienos įvesties metu validuoja įvestį, tikrina ar yra laimėtojas, ar žaidimo lenta pilna, atspausdina žaidimo lentą su jau įvestais simboliais, rotuoja žaidėjų ėjimus.
- Programa yra informatyvi: pateikia žaidėjui galimas įvesties opcijas, skelbia laimėtoją arba lygiasias, arba informuoja apie žaidimo pabaigą.  

## Paleidimas
- Žaidimas paleidžiamas nukopijavus abi projekto dalis ir įkėlus juos į failą su tokiais pačiais pavadinimais, kaip pateikta aukščiau. 
- Terminale paleidžiamas kodas įvedus `python main.py`.

## Kaip žaisti

1. Paleidus programą, žaidėjams bus prašoma pasirinkti, kuris simbolis (X arba 0) pradės žaidimą.
2. Žaidėjai paeiliui įveda eilutės ir stulpelio numerius (1, 2 arba 3), kad įdėtų savo simbolį į lentą.
3. Žaidimas baigsis, kai vienas iš žaidėjų surinks tris simbolius iš eilės, arba kai lenta bus pilna. Jei nori baigti žaidimą bet kuriuo metu, reikia įvesti „pabaiga“.
