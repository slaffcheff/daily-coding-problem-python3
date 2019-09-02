nums_list = list(map(int, input().split(",")))

k = int(input())

for index1 in range(len(nums_list)):
    for index2 in range(len(nums_list)):
        if index1 == index2:
            continue
        if nums_list[index1] + nums_list[index2] == k:
            print(True)
            exit(0)

print(False)