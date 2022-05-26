import random

cards = []
for i in range(10):
    cardH = str(i+1)+"H"
    cards.append(cardH)
    cardD = str(i+1)+"D"
    cards.append(cardD)
    cardS = str(i+1)+"S"
    cards.append(cardS)
    cardC = str(i+1)+"C"
    cards.append(cardC)
for i in range(11, 14):
    if i==11:
        letter = "J";
    if i==12:
        letter = "Q"
    if i==13:
        letter = "K"
    cards.append('{}H'.format(letter))
    cards.append('{}D'.format(letter))
    cards.append('{}S'.format(letter))
    cards.append('{}C'.format(letter))

def dealOneCard():
    return cards[random.randint(0,52)]
print(dealOneCard())

#Deals n cards (return a list of n cards) randomly, without repeats
def dealCard(n):
    list = []
    temp = []
    num = 51
    for i in range(n):
        c = cards[random.randint(0,num)]
        list.append(c)
        cards.remove(c)
        temp.append(c)
        num = num - 1
    for i in range(n):
        cards.append(temp[i])
    for i in range(n):
        temp.remove(temp[0])
    return list

def returnStrCards(cards):
    string = ""
    for i in range(len(dealt)):
        string = string+dealt[i]+", "
    return string

#Simulates 100 five card hands, shuffling between  each deal, and saving the output in a file,
#with each five card hand on its own line
f = open("cards.txt", "w")
for i in range(100):
    dealt = dealCard(5)
    string = returnStrCards(dealt)
    f.write(string[0:len(string)-2]+"\n")
f.close()

for i in range(5):
    dealt = dealCard(5)
    string = returnStrCards(dealt)
    print(string[0:len(string)-2])

#Simulates 10000 hands being dealt and calculate the probability of getting at least 
#one pair of cards in a single five card hand.
totalCount = 0
for i in range(10000):
    numList = []
    count = 0
    dealt = dealCard(5)

    for i in range(5):
        if(len(dealt[i])==2):
            numList.append(dealt[i][0])
        if(len(dealt[i])==3):
            numList.append('10')
    
    for i in range(5):
        num = dealt[i][0]
        if numList.count(num) > 1:
            count = count + 1
    if count >= 1:
        totalCount = totalCount + 1
    
print("Probability of a pair: "+str(totalCount/10000))
