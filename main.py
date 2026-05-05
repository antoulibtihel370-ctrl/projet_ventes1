import pandas as pd
import matplotlib.pyplot as plt

TVA_RATE = 0.20

def traiter_fichier(fichier):
    try:
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

        # Export CSV
        df.to_csv("resultats_final.csv", index=False)
        print("✅ Fichier généré : resultats_final.csv")

        # 📊 Graphique
        ids = df['ID']
        ca = df['CA_Net']

        # Couleurs (vert si >= moyenne, rouge sinon)
        moyenne = ca.mean()
        couleurs = ['green' if val >= moyenne else 'red' for val in ca]

        plt.figure()
        plt.bar(ids, ca, color=couleurs)

        plt.title("CA Net par produit")
        plt.xlabel("ID Produit")
        plt.ylabel("CA Net")

        plt.savefig("graphique.png")  # sauvegarde image
        plt.show()

        print("📊 Graphique généré : graphique.png")

    except Exception as e:
        print("❌ Erreur :", e)


if __name__ == "__main__":
    traiter_fichier("ventes.csv")
