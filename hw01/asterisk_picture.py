def drawing_a_tree(x):
    i = 0
    while i < x:
        j = 0
        while j <= i:
            print('*', end="")
            j += 1
        i +=1
        print()

    k= 0
    while k < 5:
        print(4*'*')
        k +=1    

drawing_a_tree(20)