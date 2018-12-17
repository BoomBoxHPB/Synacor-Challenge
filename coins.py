import sys

def main():
    coins = [2,7,3,9,5]

    for a in coins:
        coins2 = list(coins)
        coins2.remove(a)
        for b in coins2:
            coins3 = list(coins2)
            coins3.remove(b)
            for c in coins3:
                coins4 = list(coins3)
                coins4.remove(c)
                for d in coins4:
                    coins5 = list(coins4)
                    coins5.remove(d)
                    for e in coins5:
                        total = a + ( b * c**2 ) + d**3 - e
                        if total == 399:
                            print(a,b,c,d,e,total)
main()