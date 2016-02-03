class solution:
    def combine(aString, num):
        # aString = ['A','B','C']
        # num = [1,2,3,4]
        #v1
        #return map(lambda a, b: a + b, aString, num)
        #v2
        #return [x + y for x, y in zip(aString, num)]
        deck = []
        for i in range(max(len(aString),len(num))):
            try:
                card = aString[i] + str(num[i])
            except IndexError:
                if len(aString) > len(num):
                    num.append('')
                    card = aString[i] + str(num[i])
                elif len(aString) < len(num):
                    card = str(num[i])
                continue
            deck.append(card)
                
    aString = ['A','B','C']
    num = [1,2,3,4]
    print combine(aString, num)
    # results = ['A1','B2','C3', 4]