
def recPrint(ls, index = 0):    
    if index == len(ls):
        print("Конец списка")
        return
    print(ls[index])
    recPrint(ls, index + 1)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
recPrint(my_list)