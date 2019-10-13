
list1 = [('puct1: ', 10), ('puct2: ', 15), ('puct3: ',30)]
list2 = []
money = int(input('How huch money have'))

while money > 10:

        for index, item in enumerate(list1):
            print(index,',',item)


        input = input('Choose the product you want')
        if input== 'q':

            print('Program going to Exit')
            break
        elif input.isdigit():
            inputnum = int(input)
            if money > list1[inputnum][1] and inputnum >= 0 and inputnum < len(list1) - 1:

                list2.append(list1[inputnum])
                money -= list1[inputnum][1]
                print('You still have', money)

                print('You bought', list2)
else:
    print('You don\'t have enough money, must be grater than 10')
