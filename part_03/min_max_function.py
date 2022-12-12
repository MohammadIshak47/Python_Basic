# list = [5,2,9,5,11]
# # print(min(list))
# print(max(list))
'''
def greatest_num(list_num):
    return max(list_num)-min(list_num)


list_num = [1,3,5,99,433,12,13]
print(greatest_num(list_num))

'''

## problem _01 : Given input [1,2,3,[3,4],[7,9]] . findout numbers of list
## Solution


def sublist_counter(list_item):
    count = 0
    for i in list_item:
        if type(i) == list:
            count+=1
    return count

list_item = [1,2,3,[3,4],[7,9]] 

print(sublist_counter(list_item))




