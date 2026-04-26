# traitement.py

import pandas as pd
import os

TVA_RATE = 0.20


def charger_donnees(fichier):
    """
    Charge et valide le fichier CSV.
    """
    if not os.path.exists(fichier):
        raise FileNotFoundError(f"Fichier {fichier} introuvable.")

    df = pd.read_csv(fichier)

    if df.empty:
        raise ValueError("Fichier vide.")

    colonnes = {'ID', 'Prix', 'Quantite', 'Remise'}
    if not colonnes.issubset(df.columns):
        raise ValueError("Colonnes manquantes.")

    # Conversion des types
    df['Prix'] = pd.to_numeric(df['Prix'], errors='coerce')
    df['Quantite'] = pd.to_numeric(df['Quantite'], errors='coerce')
    df['Remise'] = pd.to_numeric(df['Remise'], errors='coerce')

    # Vérification valeurs invalides
    if df[['Prix','Quantite','Remise']].isnull().any().any():
        raise ValueError("Données invalides (valeurs non numériques).")

    if (df[['Prix','Quantite','Remise']] < 0).any().any():
        raise ValueError("Valeurs négatives interdites.")

    if (df['Remise'] > 100).any():
        raise ValueError("Remise > 100% invalide.")

    return df


def calculer_indicateurs(df):
    """
    Calcule CA Brut, CA Net et TVA.
    """
    df['CA_Brut'] = df['Prix'] * df['Quantite']
    df['CA_Net'] = df['CA_Brut'] * (1 - df['Remise'] / 100)
    df['TVA'] = df['CA_Net'] * TVA_RATE
    return df


def analyser(df):
    """
    Analyse les résultats globaux.
    """
    if df['CA_Net'].isnull().all():
        raise ValueError("Impossible de déterminer le produit max.")

    ca_total = df['CA_Net'].sum()
    produit_max = df.loc[df['CA_Net'].idxmax(), 'ID']

    return ca_total, produit_max


def traiter_fichier(fichier):
    """
    Pipeline complet de traitement.
    """
    df = charger_donnees(fichier)
    df = calculer_indicateurs(df)
    ca_total, produit_max = analyser(df)

    # Création dossier static si absent
    os.makedirs("static", exist_ok=True)

    # Export CSV
    df.to_csv("static/resultats_final.csv", index=False)

    return df, ca_total, produit_max