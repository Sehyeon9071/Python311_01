# 무엇을 만들어 볼까요...

import random

## 플레이어 생성
player_info = {
    "ID" : input("ID를 입력하세요. : "),
    "name" : input("이름을 입력하세요. : "),
    "age" : input("나이를 입력하세요. : "),
    "sex" : input("성별을 입력하세요. : "),
    "height" : input("키를 입력하세요. : "),
    "weight" : input("몸무게를 입력하세요. : ")
}

print("게임을 시작합니다.")

monster_info = {
    "HP" : random.randint(520, 720),
}

monster_hp = monster_info["HP"]
print(f"Monster의 HP는 {monster_hp}입니다.")

weapon_info = {
    "fire_sword" : {
        "damage" : 55,
        "stamina" : 100
    },
    "electrical_sword" : {
        "damage" : 50,
        "stamina" : 130
    },
    "water_sword" : {
        "damage" : 45,
        "stamina" : 160
    }
}

player_weapon = random.choice(list(weapon_info.keys()))
print(f"Player의 무기는 {player_weapon}입니다.")
player_dmg = player_weapon["damage"]
print(f"Player의 무기 데미지는 {player_dmg}입니다.")
player_stamina = player_weapon["stamina"]
print(f"Player의 스테미너는 {player_stamina}입니다.")

while True:
    if monster_hp <= 0:
        print("Win\nMonster를 처치하였습니다.\n게임을 종료합니다.")
        break
    elif player_stamina <= 0:
        print("Lose\nPlayer의 스테미너가 전부 소모되었습니다.\n게임을 종료합니다.")
        break
    else:
        print("==================================")
        print(f"Monster HP : {monster_hp}")
        print(f"Player 스테미너 : {player_stamina}")
        print("==================================")
        attack = int(input("공격하시려면 1을 입력하세요."))

        if attack == 1:
            monster_hp -= player_dmg
            player_stamina -= 10
        elif:

        else:
            print("잘못된 숫자를 입력하셨습니다.")