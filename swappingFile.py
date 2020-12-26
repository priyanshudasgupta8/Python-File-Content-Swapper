def swapFileData():
    file1 = input('Enter A File\'s Name: ')    
    file2 = input('Enter Another File\'s Name: ')
   
    f1 = open(file1, 'r')
    data_a = f1.read()
 
    f2 = open(file2, 'r')
    data_b = f2.read()


    with open(file1, 'w') as c:
        c.write(data_b)
    
    with open(file2, 'w') as d:
        d.write(data_a)

swapFileData()