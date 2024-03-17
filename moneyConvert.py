moneyStr=input()
exchangeRate=6.78
if moneyStr[0:3] in ["RMB","rmb"] :
    USD=eval(moneyStr[3:len(moneyStr)])/exchangeRate
    print("USD{:.2f}".format(USD))
elif moneyStr[0:3] in ["USD","usd"] :
    RMB=eval(moneyStr[3:len(moneyStr)])*exchangeRate
    print("RMB{:.2f}".format(RMB))
