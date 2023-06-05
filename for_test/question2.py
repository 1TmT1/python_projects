def get_num(nums, num):
    # new_list = []
    index = len(nums) - 1
    x = index
    while x > 0:
        if nums[x] % num != 0:
            nums.pop(x)
            index -= 1

        x = index


def main():
    nums = [5, 1, 8, 10, 9]
    get_num(nums, 2)
    print(nums)


if __name__ == "__main__":
    main()
