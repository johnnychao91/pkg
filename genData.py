
import pandas as pd
import json
import csv
from calculate_cp import generate_csv


with open('./data/pokemon.json', 'r', encoding='utf-8') as file:
    pokemon_data = json.load(file)

    
for pokemon in pokemon_data:
    dex = pokemon["dex"]
    base_attack = float(pokemon["baseStats"]["atk"])
    base_defense = float(pokemon["baseStats"]["def"])
    base_stamina = float(pokemon["baseStats"]["hp"])
    specie = pokemon['speciesId']
    if "_shadow" in specie:
        continue
    filename = "./data/cp_list/" + specie + "_cp.csv"
    print(dex)
    generate_csv(base_attack, base_defense, base_stamina, filename)
    
    
"""
# 載入 Excel 文件
file_path = './data/base_stats.xlsx'
excel_data = pd.read_excel(file_path)

# 顯示資料的前幾行以了解其結構
print(excel_data.head())

# 提取相關的列：寶可夢 ID、中文名稱、體力、攻擊、防禦
extracted_data = excel_data[['#', 'Unnamed: 2', '攻擊', '防禦', '體力']].dropna().reset_index(drop=True)
extracted_data.columns = ['ID', 'nameZH', 'attack', 'defense', 'stamina']

# 去除重複的行
unique_data = extracted_data.drop_duplicates(subset=['ID', 'nameZH', 'attack', 'defense', 'stamina'])

# 將結果輸出為 CSV 檔案
output_file_path = './data/base_stats.csv'
unique_data.to_csv(output_file_path, index=False)

print(f"資料已成功輸出至 {output_file_path}")
"""


"""
# 遍歷每隻寶可夢並列印其 atk, def, hp 數據
for pokemon in pokemon_data:
    attack = pokemon["baseStats"]["atk"]
    defense = pokemon["baseStats"]["def"]  # "def" 是 Python 的保留字，所以這裡使用 "def_" 代替
    stamina = pokemon["baseStats"]["hp"]
    print(f"{pokemon['speciesName']}: ATK = {attack}, DEF = {defense}, HP = {stamina}")
"""

"""
# 遍歷每隻寶可夢
for pokemon in pokemon_data:
    dex = pokemon["dex"]
    print(f"{pokemon['speciesName']}")
"""

"""
# Update pokemon_data with speciesNameZH from extracted_data
for index, row in extracted_data.iterrows():
    pokemon_id = str(int(row['ID']))  # Convert ID to string to match JSON keys
    species_name_zh = row['speciesNameZH']
    
    # Find matching Pokémon by ID and update the speciesNameZH field
    for pokemon in pokemon_data:
        if pokemon.get('id') == pokemon_id:
            pokemon['speciesNameZH'] = species_name_zh
            break

# Save the updated JSON data back to a file
updated_json_path = '/mnt/data/updated_pokemon.json'
with open(updated_json_path, 'w', encoding='utf-8') as file:
    json.dump(pokemon_data, file, ensure_ascii=False, indent=4)

updated_json_path
"""
