
def main():
    nums = []
    combinations = []
    is_inside_comb = False
    for x in range(1, 10):
        nums.append(int(x))

    for x in nums:
        for j in nums:
            for z in nums:
                if x + j + z == 15:
                    for comb in combinations:
                        if comb[0] == x and comb[1] == j and comb[2] == z:
                            is_inside_comb = True
                            break
                        elif comb[0] == x and comb[2] == j and comb[1] == z:
                            is_inside_comb = True
                            break
                        elif comb[1] == x and comb[2] == j and comb[0] == z:
                            is_inside_comb = True
                            break
                        elif comb[1] == x and comb[0] == j and comb[2] == z:
                            is_inside_comb = True
                            break
                        elif comb[2] == x and comb[0] == j and comb[1] == z:
                            is_inside_comb = True
                            break
                        elif comb[2] == x and comb[1] == j and comb[1] == z:
                            is_inside_comb = True
                            break
                    if not is_inside_comb:
                        combinations.append([x, j, z])
                    else:
                        is_inside_comb = False

    for nums in combinations:
        if nums[0] == nums[1]:
            combinations.remove(nums)
        elif nums[1] == nums[2]:
            combinations.remove(nums)
        elif nums[0] == nums[2]:
            combinations.remove(nums)
    print(combinations)

    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in combinations:
        for j in x:
            counter[j - 1] = counter[j - 1] + 1

    for x in range(len(counter)):
        print(str(x) + "==>" + str(counter[x]))


if __name__ == "__main__":
    main()
