
import pandas as pd
import json
import csv

with open('./data/pokemon.json', 'r', encoding='utf-8') as file:
    pokemon_data = json.load(file)


filename = './data/pk_names.csv'
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nameID', "nameEN"])
                        
    for pokemon in pokemon_data:
        dex = pokemon["dex"]
        attack = pokemon["baseStats"]["atk"]
        defense = pokemon["baseStats"]["def"]
        stamina = pokemon["baseStats"]["hp"]
        speciesId = pokemon["speciesId"]
        speciesName = pokemon["speciesName"]
        writer.writerow([speciesId, speciesName])

print(f"'{filename}' done.")


filename = './data/pk_names.csv'
with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    pk_name = list(csv_reader)
    
filename = './data/pokemon_name.csv'
with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    pokemon_name = list(csv_reader)
    
pk_name_dict = {}
for pokemon in pokemon_name:
    pk_name_dict[pokemon['name'].lower().replace(". ","").replace(" ","").replace("-","").replace("_","").replace("'","")] = pokemon['nameZH']
    
for pokemon in pk_name:
    pokemon['nameZH'] = pokemon['nameID']
    
    pokemon['nameZH'] = pokemon['nameZH'].replace("pikachu_flying", "皮卡丘.飛翔")  
    pokemon['nameZH'] = pokemon['nameZH'].replace("nidoran_female", "尼多蘭")
    pokemon['nameZH'] = pokemon['nameZH'].replace("nidoran_male", "尼多朗")
    pokemon['nameZH'] = pokemon['nameZH'].replace("parasect", "派拉斯特")
    pokemon['nameZH'] = pokemon['nameZH'].replace("kadabra", "勇基拉")
    pokemon['nameZH'] = pokemon['nameZH'].replace("kabutops", "鐮刀盔")
    pokemon['nameZH'] = pokemon['nameZH'].replace("lanturnw", "電燈怪")
    pokemon['nameZH'] = pokemon['nameZH'].replace("azumarill", "瑪力露麗")
    pokemon['nameZH'] = pokemon['nameZH'].replace("castform_sunny", "飄浮泡泡.太陽")   
    pokemon['nameZH'] = pokemon['nameZH'].replace("cherrim_sunny", "櫻花兒.晴天")
    pokemon['nameZH'] = pokemon['nameZH'].replace("mime_jr", "魔尼尼")
    pokemon['nameZH'] = pokemon['nameZH'].replace("swoobat", "心蝙蝠")
    pokemon['nameZH'] = pokemon['nameZH'].replace("klinklang", "齒輪怪")
    pokemon['nameZH'] = pokemon['nameZH'].replace("volcarona", "火神蛾")
    pokemon['nameZH'] = pokemon['nameZH'].replace("meowstic_female", "超能妙喵.雌性")
    pokemon['nameZH'] = pokemon['nameZH'].replace("meowstic", "超能妙喵.雄性")
    pokemon['nameZH'] = pokemon['nameZH'].replace("crabrawler", "好勝蟹")
    pokemon['nameZH'] = pokemon['nameZH'].replace("pyukumuku", "拳海參")
    pokemon['nameZH'] = pokemon['nameZH'].replace("eiscue_ice", "冰砌鵝.結凍頭")   
    pokemon['nameZH'] = pokemon['nameZH'].replace("eiscue_noice", "冰砌鵝.解凍頭") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("kilowattrel", "大電海燕") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("palafin_hero", "海豚俠.全能") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("palafin_zero", "海豚俠.平凡") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("tatsugiri_curly", "米立龍.上弓")
    pokemon['nameZH'] = pokemon['nameZH'].replace("tatsugiri_droopy", "米立龍.下垂")
    pokemon['nameZH'] = pokemon['nameZH'].replace("tatsugiri_stretchy", "米立龍.平挺")
    pokemon['nameZH'] = pokemon['nameZH'].replace("dudunsparce_three", "土龍節節.三節")
    pokemon['nameZH'] = pokemon['nameZH'].replace("dudunsparce_two", "土龍節節.二節")
    pokemon['nameZH'] = pokemon['nameZH'].replace("dudunsparce", "土龍節節")
    pokemon['nameZH'] = pokemon['nameZH'].replace("pawmot", "巴布土撥")

    pokemon['nameZH'] = pokemon['nameZH'].replace("kyurem_black", "酋雷姆.焰黑")
    pokemon['nameZH'] = pokemon['nameZH'].replace("kyurem_white", "酋雷姆.焰白")
    pokemon['nameZH'] = pokemon['nameZH'].replace("keldeo_ordinary", "凱路迪歐.普通")
    pokemon['nameZH'] = pokemon['nameZH'].replace("keldeo_resolute", "凱路迪歐.覺悟")
    pokemon['nameZH'] = pokemon['nameZH'].replace("meloetta_aria", "美洛耶塔.歌聲")
    pokemon['nameZH'] = pokemon['nameZH'].replace("meloetta_pirouette", "美洛耶塔.舞步")
    pokemon['nameZH'] = pokemon['nameZH'].replace("genesect_burn", "蓋諾賽克特.火焰卡帶")
    pokemon['nameZH'] = pokemon['nameZH'].replace("genesect_chill", "蓋諾賽克特.冰凍卡帶")
    pokemon['nameZH'] = pokemon['nameZH'].replace("genesect_douse", "蓋諾賽克特.水流卡帶")
    pokemon['nameZH'] = pokemon['nameZH'].replace("genesect_shock", "蓋諾賽克特.閃電卡帶")
    pokemon['nameZH'] = pokemon['nameZH'].replace("zygarde_complete", "基格爾德.完全體")
    pokemon['nameZH'] = pokemon['nameZH'].replace("zygarde_10", "基格爾德.10%")
    pokemon['nameZH'] = pokemon['nameZH'].replace("zygarde", "基格爾德.50%")
    pokemon['nameZH'] = pokemon['nameZH'].replace("type_null", "屬性:空")
    pokemon['nameZH'] = pokemon['nameZH'].replace("eternatus_eternamax", "無極汰那.無極巨化") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("eternatus", "無極汰那")
    pokemon['nameZH'] = pokemon['nameZH'].replace("koraidon_apex", "故勒頓.完全")
    pokemon['nameZH'] = pokemon['nameZH'].replace("miraidon_ultimate", "密勒頓.完全")
     
    pokemon['nameZH'] = pokemon['nameZH'].replace("_shadow", ".暗影")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_alolan", ".阿羅拉")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_galarian", ".伽勒爾")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_hisuian", ".洗翠")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_paldean", ".帕底亞")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_mega", ".超級")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_mega_x", ".超級X")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_mega_y", ".超級Y")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_5th_anniversary", ".五周年")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_horizons", ".地平線")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_kariyushi", ".沖繩")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_libre", ".面罩摔角手")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_pop_star", ".偶像")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_rock_star", ".硬搖滾")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_shaymin", ".謝米圍巾")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_armored", ".裝甲")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_rainy", ".雨水")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_snowy", ".雪雲")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_primal", ".原始")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_attack", ".攻擊")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_defense", ".防禦")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_speed", ".速度")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_plant", ".草木")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_sandy", ".砂土")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_trash", ".垃圾")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_overcast", ".陰天")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_fan", ".旋轉")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_frost", ".結冰")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_heat", ".加熱")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_mow", ".切割")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_wash", ".清洗")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_origin", ".起源")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_altered", ".別種")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_land", ".陸上")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_sky", ".天空")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_zen", ".達摩模式")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_standard", ".普通模式")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_incarnate", ".化身")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_therian", ".靈獸")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_female", ".雌性")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_male", ".雄性")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_small", ".小")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_average", ".普通")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_large", ".大")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_super", ".特大")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_confined", ".懲戒")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_unbound", ".解放") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_baile", ".熱辣") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_pau", ".呼拉") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_pom_pom", ".啪滋") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_sensu", ".輕盈")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_dawn_wings", ".拂曉之翼") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_dusk_mane", ".黃昏之鬃") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_ultra", ".究極")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_dusk", ".黃昏") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_midday", ".白晝") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_midnight", ".黑夜") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_school", ".魚群") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_solo", ".單獨") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_core", ".核心") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_meteor", ".流星") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_dawn_wings", ".拂曉之翼") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_dusk_mane", ".黃昏之鬃") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_ultra", ".究極") 
    pokemon['nameZH'] = pokemon['nameZH'].replace("_amped", ".高調")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_low_key", ".低調")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_antique", ".真品")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_phony", ".贗品")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_full_belly", ".滿腹花紋")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_hangry", ".空腹花紋")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_crowned_sword", ".劍之王")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_crowned_shield", ".盾之王")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_hero", ".百戰勇者")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_rapid_strike", ".連擊流")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_single_strike", ".一擊流")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_ice_rider", ".騎白馬")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_blue", ".藍")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_green", ".綠")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_white", ".白")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_yellow", ".黃")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_family_of_four", ".四隻")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_family_of_three", ".三隻")
    
    pokemon['nameZH'] = pokemon['nameZH'].replace("_bug", ".蟲")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_dark", ".惡")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_dragon", ".龍")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_electric", ".電")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_fairy", ".妖精")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_fighting", ".格鬥")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_fire", ".火")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_flying", ".飛行")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_ghost", ".幽靈")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_grass", ".草")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_ground", ".地面")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_ice", ".冰")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_poison", ".毒")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_psychic", ".超能力")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_rock", ".岩石")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_steel", ".鋼")
    pokemon['nameZH'] = pokemon['nameZH'].replace("_water", ".水")
    
    for key in pk_name_dict.keys():
        pokemon['nameZH'] = pokemon['nameZH'].lower().replace(". ","").replace(" ","").replace("-","").replace("_","").replace("'","").replace(". ","")
        if key in pokemon['nameZH']:
            pokemon['nameZH'] = pokemon['nameZH'].replace(key, pk_name_dict[key])
            break
    pokemon['nameZH'] = pokemon['nameZH'].replace(".", " ")

filename = './data/pk_names.csv'
# 将修改后的数据写入新的CSV文件
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['nameID', "nameEN", 'nameZH']  # 确保字段名称与原CSV文件一致
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    csv_writer.writeheader()  # 写入表头
    csv_writer.writerows(pk_name)  # 写入修改后的数据行
print(f"'{filename}' done.")