import random
import sys
from itertools import combinations as comb # itertools for iteration,looping,permutation,combinatorics

# item you want to rank
item_list = ["Edamame", "Here Comes The Sun", "Industry Baby", "The Kiss Of Venus",
            "Leave The Door Open", "Lumberjack",   "Nothing New", 
            "Spiral" , "Welcome To The Internet", "What It Feels Like"]

item_comb = list(comb(item_list, 2))
random.shuffle(item_comb)
item_score = [0] * len(item_list)

print(f"There will be {len(item_comb)} combinations.")
yn = input("Go Ahead y/n: ")

if yn == 'n':
    sys.exit("Ranking Aborted")
    
for i in item_comb:
    rand_order = random.randrange(2)
    if rand_order == 0:
        print(f'1: {i[0]:<30s}/\t2: {i[1]:<30s}')
        select = int(input("Select: "))
        while select not in (1, 2):
            print("Error! Select Again")
            select = int(input("Select: "))
        if select == 1:
            item_score[item_list.index(i[0])] += 1
        elif select == 2:
            item_score[item_list.index(i[1])] += 1
    else:
        print(f'1: {i[1]:<30s}/\t2: {i[0]:<30s}')
        select = int(input("Select: "))
        while select not in (1, 2):
            print("Error! Select Again")
            select = int(input("Select: "))
        if select == 1:
            item_score[item_list.index(i[1])] += 1
        elif select == 2:
            item_score[item_list.index(i[0])] += 1

print()
print()

item_score_copy = item_score.copy()
for i in range(len(item_list)):
    max_index = item_score_copy.index(max(item_score_copy))
    print(f"{item_list[max_index]:<30s}:\t{str(item_score_copy[max_index]):<30s}")
    item_score_copy[max_index] = -1