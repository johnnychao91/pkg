import csv

def get_cp_multiplier(level):
    # 等級與CP Multiplier對應表
    level_to_cp_multiplier = {
        1: 0.094, 1.5: 0.1351374318, 2: 0.16639787, 2.5: 0.192650919, 3: 0.21573247, 
        3.5: 0.2365726613, 4: 0.25572005, 4.5: 0.2735303812, 5: 0.29024988, 5.5: 0.3060573775,
        6: 0.3210876, 6.5: 0.3354450362, 7: 0.34921268, 7.5: 0.3624577511, 8: 0.3752356,
        8.5: 0.387592416, 9: 0.39956728, 9.5: 0.4111935514, 10: 0.4225, 10.5: 0.4329264091,
        11: 0.44310755, 11.5: 0.4530599591, 12: 0.4627984, 12.5: 0.472336093, 13: 0.48168495,
        13.5: 0.4908558003, 14: 0.49985844, 14.5: 0.508701765, 15: 0.51739395, 15.5: 0.5259425113,
        16: 0.5343543, 16.5: 0.5426357375, 17: 0.5507927, 17.5: 0.5588305862, 18: 0.5667545,
        18.5: 0.5745691333, 19: 0.5822789, 19.5: 0.5898879072, 20: 0.5974, 20.5: 0.6048236651,
        21: 0.6121573, 21.5: 0.6194041216, 22: 0.6265671, 22.5: 0.6336491432, 23: 0.64065295,
        23.5: 0.6475809666, 24: 0.65443563, 24.5: 0.6612192524, 25: 0.667934, 25.5: 0.6745818959,
        26: 0.6811649, 26.5: 0.6876849038, 27: 0.69414365, 27.5: 0.70054287, 28: 0.7068842,
        28.5: 0.7131691091, 29: 0.7193991, 29.5: 0.7255756136, 30: 0.7317, 30.5: 0.7347410093,
        31: 0.7377695, 31.5: 0.7407855938, 32: 0.74378943, 32.5: 0.7467812109, 33: 0.74976104,
        33.5: 0.7527290867, 34: 0.7556855, 34.5: 0.7586303683, 35: 0.76156384, 35.5: 0.7644860647,
        36: 0.76739717, 36.5: 0.7702972656, 37: 0.7731865, 37.5: 0.7760649616, 38: 0.77893275,
        38.5: 0.7817900548, 39: 0.784637, 39.5: 0.7874736075, 40: 0.7903, 40.5: 0.792803968,
        41: 0.79530001, 41.5: 0.797800015, 42: 0.8003, 42.5: 0.802799995, 43: 0.8053,
        43.5: 0.8078, 44: 0.81029999, 44.5: 0.812799985, 45: 0.81529999, 45.5: 0.81779999,
        46: 0.82029999, 46.5: 0.82279999, 47: 0.82529999, 47.5: 0.82779999, 48: 0.83029999,
        48.5: 0.83279999, 49: 0.83529999, 49.5: 0.83779999, 50: 0.84029999, 50.5: 0.84279999,
        51: 0.84529999
    }
    
    return level_to_cp_multiplier.get(level, "等級無效")  # 查詢CP Multiplier，若等級無效則返回"等級無效"

def calculate_cp(base_attack, individual_attack, base_defense, individual_defense, base_stamina, individual_stamina, level):
    cp_multiplier = get_cp_multiplier(level)
    if cp_multiplier == "等級無效":
        return cp_multiplier
    cp = (base_attack + individual_attack) * ((base_defense + individual_defense) ** 0.5) * ((base_stamina + individual_stamina) ** 0.5) * (cp_multiplier ** 2) / 10
    if cp < 10:
        cp = 10
    return int(cp)

# 輸入各個參數
#base_attack = float(input("輸入種族攻擊力: "))
#base_defense = float(input("輸入種族防禦值: "))
#base_stamina = float(input("輸入種族體力值: "))
#individual_attack = float(input("輸入個體攻擊力: "))
#individual_defense = float(input("輸入個體防禦值: "))
#individual_stamina = float(input("輸入個體體力值: "))
#level = float(input("輸入等級: "))

# 輸入各個參數
filename = "pokemon_cp.csv"

def generate_csv(base_attack, base_defense, base_stamina, filename):
    levels = [i * 0.5 for i in range(2, 103)]  # 等級範圍從 1 到 51，每次增量 0.5
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["level", "attack", "defense", "stamina", "cp"])
        
        for level in levels:
            for attack in range(0, 16):
                for defense in range(0, 16):
                    for stamina in range(0, 16):
                        cp = calculate_cp(base_attack, attack, base_defense, defense, base_stamina, stamina, level)
                        if cp is not None:
                            writer.writerow([level, attack, defense, stamina, cp])

    print(f"{filename}_cp.csv done.")
