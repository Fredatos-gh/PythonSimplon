from pathlib import Path
from urllib.error import URLError

import pandas as pd
import plotly.express as px

DONNEES_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv'
DONNEES_LOCALES = Path(__file__).with_name('ventes-par-region.csv')
FICHIER_SORTIE = 'ventes-par-region.html'


def charger_donnees():
    try:
        return pd.read_csv(DONNEES_URL)
    except URLError:
        return pd.read_csv(DONNEES_LOCALES)


def main():
    données = charger_donnees()
    figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
    figure.write_html(FICHIER_SORTIE)
    print(f'{FICHIER_SORTIE} généré avec succès !')


if __name__ == '__main__':
    main()
