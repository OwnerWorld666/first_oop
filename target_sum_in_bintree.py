inp = [int(x) if x else '' for x in input().split(',')]
arr = [[inp[0]]]
length = len(bin(len(inp))[2:])
k = 1
for i in range(1, length):
    if '' not in arr[i-1]:
        itera = inp[k:k + 2 ** i]
        k += 2 ** i
    else:
        itera = inp[k:k + 2 ** i - 2 * arr[i-1].count('')]
        k = k + 2 ** i - 2 * arr[i-1].count('')
    arr.append(itera)

#полноценное бинарное дерево в массиве
for i in range(1, length):
    if '' not in arr[i-1]:
        continue
    else:
        ind_arr = []
        for j in range(len(arr[i-1])):
            if arr[i-1][j] == '':
                ind_arr.append(j)
        for x in ind_arr:
            arr[i].insert(x*2,'')
            arr[i].insert(x*2+1,'')

print(f'Введенное бинарное дерево в виде списка: {arr}')

def bin_tree(tree, target, path=[], depth=0, index=0):
    if depth == len(tree) or sum(path) == target:
        if sum(path) == target:
            print(*path, sep='->')
        return

    left_child_ind = 2 * index
    right_child_ind = 2 * index + 1

    if left_child_ind < len(tree[depth]):
        left_child = tree[depth][left_child_ind]
        if left_child != '':
            bin_tree(tree, target, path + [left_child], depth + 1, left_child_ind)

    if right_child_ind < len(tree[depth]):
        right_child = tree[depth][right_child_ind]
        if right_child != '':
            bin_tree(tree, target, path + [right_child], depth + 1, right_child_ind)

req_sum = int(input("Требуемая сумма = "))
bin_tree(arr, req_sum)

#примеры для проверки
#5,4,8,11,,13,4,7,2,,,,1
#1,,5,7,8,4,9,11,3
#5,7,1,12,,2,6,8,,9,3,,4,30,20,,,,,,,