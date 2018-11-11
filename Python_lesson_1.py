# 01. 파이썬 개요

## ---(Sun Nov 11 13:32:12 2018)---
print(3)
972*3
972*0.97


# 02. 파이썬 변수

bitcoin=9751500
bitcoin
id(bitcoin)

bitcoin = 121352
ripple = 13414
total = bitcoin * 10 + ripple * 5
total

print(total)
print("총평가금액: ", total)


# 03. 파이썬 문자열

mystring1 = 'a'
mystring2 = "a"
mystring3 = "abc mart"
id(mystring1)
id(mystring2)
id(mystring3)

mycoint = "bitcoin" # a typing Error
mycoin = "bitcoin"
mycoin[0]
mycoin[1]
mycoin[2]

greeting = "hello minsu"
greeting[0:5]
greeting[:5]
greeting[5:]
greeting[0:1]

ticker = "BTC_KRW"
ticker[0:3]
ticker[-3:]

mystring = "hello world"
len(mystring)

a = naver # Error because 'naver' has not been defined.

currency1 = "etc_krw"
currency2 = "eth_krw"
currency3 = "btc_krw"
print(currency1[0:2])
print(currency1[0:3])
print(currency2[0:3])
print(currency3[0:3])
print(currency3[:3])

ticker = 'btc_krw'
ticker.upper # Error
ticker.upper)_ # Error
ticker.upper()

ticker2 = ticker.upper()
ticker; ticker2 # only show the output of ticker2
ticker, ticker2

cap_ticker = ticker2[:3]
cap_ticker


# 04. 파이썬 리스트

hold = ["btc_krw", "xrp_krw", "eth_krw"]
hold[0]
hold[1]
hold[2]

hold[0] = "bch_krw"
hold

hold = []
hold
hold.append('btc')
hold.append('xrp')
hold.append('eth')
hold

del hold[0]
hold

a = [1,2,3,4]
max(a)
min(a)

## ex
close = [100, 200, 300, 400]
diff = max(close) - min(close)
diff*0.3

a
sum(a)/len(a)


# 05. 파이썬 튜플

close2 = (100, 200, 300, 400)
type(close2)


# 06. 파이썬 딕셔너리

icecream = {'merona' : 1000, 'gugucon' : 2000}
type(icecream)

# 파이썬 최신버전은 딕셔너리도 순서가 있다!

icecream[0]
icecream['merona']

cur_price = {}
cur_price["bitcoin"] = 9703000
cur_price["ripple"] = 707
cur_price

del cur_price['bitcoin']
cur_price

cur_price.key() # Error
cur_price.keys()
cur_price.values()

close_ripple = [980, 970, 950, 930, 900]
close_ripple

close_rip = {"0221" : 980, "0222" : 990, "0223", 1000} # Error
close_rip = {"02/21" : 980, "02/22" : 990, "02/23", 1000} # Error
close_rip = {"Feb21" : 980, "Feb22" : 990, "Feb23", 1000} # Error
close_rip = {'02/21' : 980, '02/22' : 990, '02/23' : 1000}
close_rip
sum(close_rip.values())/len(close_rip)
