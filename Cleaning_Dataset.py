import pandas as pd

# Caricamento del dataset generato da Dataset_Importing.py
cards = pd.read_csv("cards.csv")

print(f"Numero totale di carte: {len(cards)}")

missing_values = cards.isna().sum()
print("\nValori mancanti per colonna:")
print(missing_values)

filtered_cards = cards[(cards['type'].isin(['Spell Card', 'Trap Card'])) & (cards['race'].isin(['Continuous', 'Counter','Countinuous','Normal','Equip','Field','Ritual','Quick-Play']))]
filtered_fusion = cards[(cards['type'].isin(['Fusion Monster', 'Link Monster', 'XYZ Monster','Synchro Monster','Synchro Tuner Monster', 'Pendulum Effect Fusion Monster','Synchro Pendulum Effect Monster','Pendulum Effect Fusion Monster','Token','XYZ Pendulum Effect Monster']))] 
filtered_main = cards[(cards['type'].isin(['Effect Monster','Normal Monster','Flip Effect Monster','Union Effect Monster','Pendulum Effect Monster','Tuner Monster','Gemini Monster','Normal Tuner Monster','Spirit Monster','Ritual Effect Monster','Skill Card','Ritual Monster','Toon Monster','Pendulum Normal Monster','Pendulum Tuner Effect Monster','Pendulum Effect Ritual Monster','Pendulum Flip Effect Monster']))] 

banned_cards = cards[(cards['ban_tcg'].isin(['Semi-Limited', 'Limited', 'Banned']))]
banned_cards2 = cards[(cards['ban_ocg'].isin(['Semi-Limited', 'Limited', 'Banned']))]
banned_cards3 = cards[(cards['ban_goat'].isin(['Semi-Limited', 'Limited', 'Banned']))]

cards_na = cards.dropna(subset=['level', 'attribute'])
category_orders = sorted(cards['level'].unique())

card_set_relation = pd.read_csv("cards_cardsets.csv")

card_set_relation = card_set_relation.drop(columns=["set_id", "set_code"])

card_set_relation = card_set_relation.rename(columns={"card_id": "id"})

print(f"\nCarte Magia/Trappola: {len(filtered_cards)}")
print(f"Carte Extra Deck: {len(filtered_fusion)}")
print(f"Carte Main Deck: {len(filtered_main)}")
print(f"Carte Bandite TCG: {len(banned_cards)}")
print(f"Carte Bandite OCG: {len(banned_cards2)}")
print(f"Carte Bandite GOAT: {len(banned_cards3)}")