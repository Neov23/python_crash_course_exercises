# Exercise 4-10 (from 4-7)

numbers = list(range(3, 31, 3))

for number in numbers:
    print(number)

print(f" \nThe first three numbers of this list are: {numbers[:3]}")
print(f"The two numbers of the middle of this list are: {numbers[4:6]}")
print(f"The last three numbers of this list are: {numbers[-3:]} \n")

# NOTE! I used two numbers as middle of list, cause the list elements are even

'''
I had to manually calculate which are the three middle elements of the list.
The best approach i could think of, for lists with too many elements, is to
use 'mid = int(len(list) / 2)' to find the index of the element in the middle.
Then, if i wanted to find the three middle elements, i would do 'mid-1',
'mid', 'mid+1'
'''