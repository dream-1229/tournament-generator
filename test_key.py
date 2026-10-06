import random

from data import all_class
from data import seed_position
from data import first_match_num_list


def choose_class():
    result = []
    i=1
    while True:
        class_address = int(input(f"出場クラス{i}:" ))
        
        if class_address==0:
            break
        else:       
            result.append(class_address)

        i+=1

    return result

def search_excellent_class():
    result = []
    
    i=1
    while True:
        class_address = int(input(f"優秀クラス{i}:" ))
        
        if class_address==0 or i==3:
            break
        else:       
            result.append(class_address)

        i+=1

    return result

def class_random(class_list, ex_class_list, num):
    class_list      = class_list[:]
    ex_class_list   = ex_class_list[:]
    result =[]
    seed_positions = seed_position[num - 8]     #シード位置を抽出
    total = len(class_list) + len(ex_class_list)        #処置回数用の値

    for i in range(total):
        if i in seed_positions:
            if ex_class_list:
                choice_class = random.choice(ex_class_list)
                ex_class_list.remove(choice_class)
            else:
                choice_class = random.choice(class_list)
                class_list.remove(choice_class)
        else:
            if class_list:
                choice_class = random.choice(class_list)
                class_list.remove(choice_class)
            else:
                choice_class = random.choice(ex_class_list)
                ex_class_list.remove(choice_class)

        result.append(choice_class)

    return result


def input_first_match(class_list, num):
    result = []
    first_match_list = first_match_num_list[num - 8]       #試合数に対応したfirst_matchの2次元目の配列を取得
    result = [[] for _ in range(len(first_match_list))]          #resultに1次元目の配列を確保

    for i in range(len(first_match_list)):
        for c in first_match_list[i]:
            result[i].append(class_list[c])

    return result




def translate_list(class_list):
    result = []

    for address in class_list:
        class_address_i = address // 10 - 1
        class_address_j = address % 10 - 1
        result.append(all_class[class_address_i][class_address_j])
    
    return result

def search_five(first_match_list):
    for i in range(len(first_match_list)):
        search_a    = False
        if len(first_match_list[i]) >= 2:
            search_a    = first_match_list[i][0] / 10 == 5 and first_match_list[i][1] / 10 == 5
        search_b    =False
        if len(first_match_list[i]) >= 4:
            search_b    = first_match_list[i][2] / 10 == 5 and first_match_list[i][3] / 10 == 5
        if search_a or search_b: 
            return False
    return True




def main_control():
    participate_class   = choose_class()   #出場クラスのリスト
    num_of_class        = len(participate_class)      #出場クラス数   
    excellent_class     = search_excellent_class()     #上位クラスのリスト(一位から三位)
    nomal_class         = [c for c in participate_class if c not in excellent_class]        #上位クラスではない参加クラスのリスト   list comprehensionを使用
    
    while True:
        random_class_list   = class_random(nomal_class, excellent_class, num_of_class)     #並び替えた後のリスト
        now_first_class          = input_first_match(random_class_list, num_of_class)      #初戦の試合番号を振り分け
        
        
        if search_five(now_first_class):
            break
    return random_class_list, now_first_class




def main_control_2(first_match_list):
    participate_class   = choose_class()   #出場クラスのリスト
    num_of_class        = len(participate_class)      #出場クラス数   
    excellent_class     = search_excellent_class()     #上位クラスのリスト(一位から三位)
    nomal_class         = [c for c in participate_class if c not in excellent_class]        #上位クラスではない参加クラスのリスト   list comprehensionを使用

    while True:
        random_class_list   = class_random(nomal_class, excellent_class, num_of_class)     #並び替えた後のリスト
        now_first_match          = input_first_match(random_class_list, num_of_class)      #初戦の試合番号を振り分け

        if  not search_five(now_first_match):
            continue

        len_list        = len(first_match_list)
        len_now_list    = len(now_first_match)

        if len_list > len_now_list:
            for _ in range(len_list - len_now_list):
                now_first_match.append([])

        elif len_list < len_now_list:
            for _ in range(len_now_list - len_list):
                first_match_list.append([])
        
        merged = []
        for i in range(len(now_first_match)):
            merged_match = now_first_match[i] + first_match_list[i]
            if len(merged_match) != len(set(merged_match)):
                break
            merged.append(merged_match)
        else:
            return random_class_list, merged


