#I DONT WANT TO WORK FOR MCDONALDS. I LOVE BITCOIN EDITION
#BY: DARKHORSE369
#31,536,000 attempts per year
#946,080,000 attempts in 30 years
#i should buy 1 dollar of lottery every day for 30 years, my odds are def better. I need a quantum GPU!!!
#SEND ME A DONATION: 1JWLik86NuVydKUfWm3kMcCQwDAyYzujXJ
#Crashes after a while  -- connection error too many attempts
import argparse
import urllib3
from urllib3 import util
import json
import math
from bitcoinaddress import Wallet
import time

LIMIT = 120
SATOSHI = 1e+8
balance=0.0

#GET Generate random bitcoin public address with private key
#if current  balance > 0 *PRINT PRIVATE KEYS AND CASHOUT!
def check_balance(addresses,bitcoin_info):
    #Less printing, i my head hurts!
    #print('loading addresses...')
    #print(addresses) 
    #print('addresses loaded:', len(addresses))
    #print('getting balances info...')

    http = urllib3.PoolManager(timeout=util.Timeout(10))
    total = len(addresses)
    steps = math.floor(total / LIMIT)
    remind = total % LIMIT

    for step in range(steps + 1):
        url = 'https://blockchain.info/balance?active='
        if step < steps:
            for a in range(LIMIT):
                url += addresses + '|'
        else:
            for a in range(remind):
                url += addresses + '|'
        url = url[:-1]
        res = http.request('GET', url, timeout=util.Timeout(10), retries=util.Retry(10))
      

        data = json.loads(res.data.decode('utf-8'))
        k=json.dumps(data)
        #print(k)

        #Noob patch #1: generated address size 33 and 34.
        
        if len(addresses)==33:
         balance=float(k[56])
        elif len(addresses)==34:
            balance=float(k[57])
        else:
            print("ERROR: CHECK YOUR CODE!")
            break
    #debug test variable
    #balance=???

    if balance>0.0:
        print("JACKPOT!!!:")
        print(bitcoin_info)
        return 0

    else:
        return 1
        pass

print("##################################################")
print("Bitcoin LOVER v1 this might take an eternity!")
print("Donations accepted!: 1JWLik86NuVydKUfWm3kMcCQwDAyYzujXJ")
print("##################################################")

while True:
    wallet = Wallet()
    if check_balance(wallet.address.mainnet.pubaddr1,wallet) ==0:
        print("Congratulations you are rich!")
        #Noob Patch #2: Dont't allow commandline to leave me hanging in my misery
        while True:
            pause=input("System is waiting for you to cash out!!!")

    else:
        print("Mcdonalds is hiring... =(")
        time.sleep(1)
