import requests


def stage2():
    n = int(input())
    print(f"I have {n} conicoins.")
    print(f"{n} conicoins cost {n*100} dollars.")
    print("I am rich! Yippee!")


def stage3():
    print("Please, enter the number of conicoins you have:")
    n = int(input())
    print("Please, enter the exchange rate:")
    e = float(input())
    print(f"The total amount of dollars: {n*e}")


def stage4():
    n = float(input())
    print(f"I will get {n*2.98} RUB from the sale of {n} conicoins.")
    print(f"I will get {n*0.82} ARS from the sale of {n} conicoins.")
    print(f"I will get {n*0.17} HNL from the sale of {n} conicoins.")
    print(f"I will get {n*1.9622} AUD from the sale of {n} conicoins.")
    print(f"I will get {n*0.208} MAD from the sale of {n} conicoins.")


def stage5():
    code = input()
    url = "http://www.floatrates.com/daily/{}.json".format(code.lower())
    r = requests.get(url).json()
    print(r['usd'])
    print(r['eur'])
    print(r)


def currencyConverter():
    #the currency that you have. It is default for all the calculations
    myCurr = input().lower()
    # Cache USD rate andEUR rates
    cache = {}
    url = "http://www.floatrates.com/daily/{}.json".format(myCurr)
    # retrieve data from url
    r = requests.get(url).json()
    # If myCurr==usd , save exchange rate to eur
    if myCurr == "usd":
        cache["eur"] = r['eur']['rate']
    # If myCurr==eur , save exchange rate to usd
    elif myCurr == "eur":
        cache["usd"] = r['usd']['rate', 2]
    # else save both for usd and eur
    else:
        cache['eur'] = r['eur']['rate']
        cache["usd"] = r['usd']['rate']
    # the currency code that you want to exchange money for
    while True:
        toCurr = input().lower()
        if toCurr == "":
            exit()
        # amount of money you have
        else:
            amt = float(input())
            # Checking the cache...
            print("Checking the cache...")
            if toCurr in cache.keys():
                print("Oh! It is in the cache!")
                print(f'You received {round(amt*cache[toCurr], 2)} {toCurr.upper()}')
            else:
                print("Sorry, but it is not in the cache!")
                r = requests.get(url).json()
                rate = r[toCurr]['rate']
                print(f'You received {round(amt*rate, 2)} {toCurr.upper()}.')
                cache[toCurr] = rate


if __name__ == "__main__":
    #stage2()
   # stage3()
   #stage4()
   #stage5()
    currencyConverter()