def acc(name,number,balance):
    return {'name':name,'number':number,'balance':balance}

def deposit(account,deposit):
    if deposit < 0:
        print('存入金额不能为负数')
    else:
         account['balance'] += deposit

def getout(account,getout):
    if getout < 0:
        print('取出金额不能为负数')
    elif getout > account['balance']:
        print('取出金额不能大于余额')
    else:
        account['balance'] -= getout

name = 'tanyong'
x = acc(name,123456,9000000000)

deposit(x,1000000)

getout(x,9000000000)

print(x)