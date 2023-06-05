from itertools import combinations_with_replacement


# Get all permutations of [1, 2, 3]
perm = combinations_with_replacement(["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 2)

lst = [''.join(x) for x in perm]

start_mac_list = combinations_with_replacement(lst, 4)

final_lst = [''.join(x) for x in start_mac_list]

lst_mac_file = open("macs.txt", "w")

for x in final_lst:
    lst_mac_file.write(x + "\n")

lst_mac_file.close()
