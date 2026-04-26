#  Sales Automation Project — Data Processing Pipeline

**Matière :** Logiciels  
**Auteurs :** antoul ibtihel && ben abdallah emna && mechi rania 

---

## 📋 Description

Ce projet consiste à développer un script Python permettant d’automatiser l’analyse des ventes d’une entreprise e-commerce.

Le programme lit un fichier CSV contenant les données de ventes, effectue plusieurs calculs (chiffre d’affaires, TVA, etc.) et génère un nouveau fichier contenant les résultats.

---

##  Fichiers du projet

| Fichier | Description |
|---|---|
| `main.py` | Script principal |
| `ventes.csv` | Données de ventes brutes |
| `resultats_final.csv` | Résultats calculés exportés |
| `graphique.png` | Graphique CA Net par produit |

---

##  Fonctionnalités

Fonctionnalités
Lecture du fichier ventes.csv
Calcul du Chiffre d’Affaires Brut :
Prix × Quantité
Calcul du Chiffre d’Affaires Net :
après application de la remise (%)
Calcul de la TVA (20%)
Calcul du CA Total de l’entreprise
Identification du produit le plus rentable
Génération automatique du fichier resultats_final.csv 
Visualisation graphique du CA Net par produit avec Matplotlib

---

##  Installation

```bash
pip install pandas matplotlib openpyxl
```

## ▶️ Exécution

```bash
python main.py
```

---

## 📊 Exemple de résultat

```
===== RÉSULTATS =====
 ID   Prix  Quantite  Remise  CA_Brut  CA_Net    TVA
109   20.0         7     0.0    140.0  140.00  28.00
108   45.0         3    20.0    135.0  108.00  21.60
...
 CA Total : 850.75 €
 Meilleur produit ID : 109