import pandas as pd
import os

TVA_RATE = 0.20

def traiter_fichier(fichier):
    df = pd.read_csv(fichier, sep=None, engine='python')

    # Vérifications
    if df.empty:
        raise ValueError("Fichier vide")

    colonnes = {'ID', 'Prix', 'Quantite', 'Remise'}
    if not colonnes.issubset(df.columns):
        raise ValueError("Colonnes manquantes")

    df['Prix'] = pd.to_numeric(df['Prix'], errors='coerce')
    df['Quantite'] = pd.to_numeric(df['Quantite'], errors='coerce')
    df['Remise'] = pd.to_numeric(df['Remise'], errors='coerce')

    if df[['Prix','Quantite','Remise']].isnull().any().any():
        raise ValueError("Valeurs invalides")

    if (df[['Prix','Quantite','Remise']] < 0).any().any():
        raise ValueError("Valeurs négatives interdites")

    if (df['Remise'] > 100).any():
        raise ValueError("Remise invalide")

    # Calculs
    df['CA_Brut'] = df['Prix'] * df['Quantite']
    df['CA_Net'] = df['CA_Brut'] * (1 - df['Remise'] / 100)
    df['TVA'] = df['CA_Net'] * TVA_RATE

    # Export
    df.to_csv("resultats_final.csv", index=False)

    print("✅ Fichier généré : resultats_final.csv")

if __name__ == "__main__":
    traiter_fichier("ventes.csv")