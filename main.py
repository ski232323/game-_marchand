
import random
money=100
marchandises={
    "or":{
        "stock":0,
        "prix":0
    },
    "argent":{
        "stock":0,
        "prix":0
    },
    "fruit":{
        "stock":1,
        "prix":0
    }

    
    
}
def print_marchandises():
    print(marchandises)
def buy(items_to_buy,) :
    global money
    if money-marchandises[items_to_buy]["prix"]<0:
        print("Not enough money") 
    else :
        try:
            money-=marchandises[items_to_buy]["prix"]
            marchandises[items_to_buy]["stock"]+=1
        except KeyError :
            print('no items')
def sell(items_to_sell) :
    global money
    if marchandises[items_to_sell]["stock"]>0:
        try : 
            marchandises[items_to_sell]["stock"]-=1
            money+=marchandises[items_to_sell]["price"]
        except KeyError:
            print("no items")
            
    else :
        print('Nothing to sell')
for _ in range(10):
    marchandises["fruit"]["prix"]=random.randint(5,15)
    marchandises["or"]["prix"]=random.randint(25,200)
    marchandises["argent"]["prix"]=random.randint(20,150)
    print_marchandises()
    action=input("voulez vous passez votre tour/buy/sell")
    if action =='buy':
       item_to_buy=input('item to buy:')
       buy(item_to_buy)
    if action =='sell':
        item_to_sell=input('item to sell :')
        sell(item_to_sell)
    print(money)
print("Tu a gagné/ perdu"+""+str(money-100))
        
   
   
