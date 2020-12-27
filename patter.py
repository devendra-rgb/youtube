for i in range(5): # Rows
    for k in range(5-i):
        print( end=' ')
    for j in range(i): # Columns
        print('*',end=' ')
    print(end='\n')