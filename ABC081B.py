'''s = input()
token = s.split()

num list = [] #empty list
while token:
    num_list.append(int(token.pop(0))) ''''

size = int(input())
num_list = list(map(int, input().split()))

num div = 0
all_even = True
while all_even:
    for i in range(size):
        if num_list[1]%2 == 1:
           all_even = False
           break
        else:
            num_list[i] //= 2
    if all_even:
    num_div += 1
print(num_div)