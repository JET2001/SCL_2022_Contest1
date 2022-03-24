import sys
def question5(balance:dict, transactions: list):
    for t in transactions:
        p1, p2, amt = t
        ## p1 transfer amt to p2
        if balance[p1] < amt:
            continue
        balance[p1] -= amt
        balance[p2] += amt

    return balance
    # for person, bal in balance.items():
    #     print(person, bal)

balance = dict()
N,T = map(int, sys.stdin.readline().split())
for i in range(N):
    username, amount = sys.stdin.readline().split()
    balance[username]= int(amount)

transactions = []
for i in range(T):
    p1, p2, amt = sys.stdin.readline().split()
    transactions.append((p1,p2,int(amt)))

question5(balance, transactions)
for person in sorted(balance.keys()):
    print(person, balance[person])
