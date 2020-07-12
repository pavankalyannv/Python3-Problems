#https://practice.geeksforgeeks.org/problems/convert-a-sentence-into-its-equivalent-mobile-numeric-keypad-sequence/0/


#code
for i in range(int(input())):
    s = input()
    arr = list(s)
    data = []
    collection = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
    for i in arr:
        if i ==' ':
            data.append(0)
        else:
            count = 0
            for item in collection:
                count += 1
                if i in item:
                    loc = item.index(i)
                    for i in range(loc+1):
                        data.append(count+1)
                else:
                    pass
                        
    for i in data:
        print(i,end='')
    print()
