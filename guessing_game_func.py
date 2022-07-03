from random import randint
def guess(num):
    rand=randint(0,5)
    if num==rand:
        return('you are god damn right')
    else:
        return('you are wrong:(')
guess(10)
