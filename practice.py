array =[1,2,3,4,5,3,2,1]
first_index = 0
last_index = 0
def func(num):
    a = num
    for i in array:
        if i == num:
            first_index = array.index(i)
            print("first index:",first_index)
            last_index = len(array)-first_index
            print("last index:",last_index-1)

func(5)

