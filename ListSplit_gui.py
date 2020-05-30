
global bookname
global authorname
global quantity
global cost
global totalcost
global book
global count1
bookname=[]
authorname=[]
quantity=[]
cost=[]
book=[]
totalcost=0
count1=0

def listSplit():
    global bookname
    global authorname
    global quantity
    global cost,totalcost
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]
    book=[]
    totalcost=0
    global count1
    count1=0
    t=0
    with open("F:\python projects\LMS\Stock.txt","r") as f:
        #creating a list of lines in stock.txt
        lines=f.readlines()
        #removing \n from list
        lines=[x.strip('\n') for x in lines]
        #fetching each element one by one
        for i in range(len(lines)):
            ind=0
            #splitting one element of list into multiple elements
            for a in lines[i].split(','):
                if(ind==0):
                    bookname.append(a)
                    count1=count1+1
                elif(ind==1):
                    authorname.append(a)
                elif(ind==2):
                    quantity.append(a)
                elif(ind==3):
                    cost.append(a.strip("Rs"))
                    totalcost+=int(a.strip("Rs"))
                   
                ind+=1
    book.append(bookname)
    book.append(authorname)
    book.append(quantity)
    book.append(cost)
    return book

