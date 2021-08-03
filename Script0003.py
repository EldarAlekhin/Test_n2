# Перечисление операций деления
# / обычная операция деления

#a = 10
#b = 3
#c = a/b 
#print(c)


# // дление с выводом результата как целого числа без остатка

#d = 20
#e = 3
#f = d//e
#print(f)

# % деление с выводом результата как остатка


#g = 14
#h = 3
#i = g%h
#print(i)


# socks
pricesocks = 3
moneysocks = 50

pairsbought = moneysocks // pricesocks
print(pairsbought)

moneySpent = pricesocks * pairsbought
socksMoneyRest = moneysocks - moneySpent
print(socksMoneyRest)

# t-chirts
pricetchirts = 7
moneytchirtss = 50

tchirtsbought = moneytchirtss // pricetchirts
print(tchirtsbought)

moneySpenttchirts = pricetchirts * tchirtsbought
tchirtsMoneyRest = moneytchirtss - moneySpenttchirts
print(tchirtsMoneyRest)


# shirts
priceshirts = 12
moneyshirts = 50

shirtsbought = moneyshirts // priceshirts
print(shirtsbought)

#moneySpentshirts = priceshirts * shirtsbought
#shirtsMoneyRest = moneyshirts - moneySpentshirts
shirtsMoneyRest = moneyshirts % priceshirts
print(shirtsMoneyRest)


resttotal  = socksMoneyRest + tchirtsMoneyRest + shirtsMoneyRest
print(resttotal)


print("-------------------")

ggg =  100 % 2.97
ddd = 100 // 2.97
hhh= 100 - ddd * 2.97

fff = 100 / 2.97

print(round(ggg,2))
print(ddd)
print(fff)
print(hhh)