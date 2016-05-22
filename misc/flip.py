import random

def flip():
    '''Return head or tails based on the random function
    '''
    outcomes = { 0:'heads',1:'tails'}
    sides = outcomes[random.randrange(2)]

    return sides

def main():
    heads = 0
    tails = 0
    
    action = input('Should I flip > (Y/N) ')
    
    if action == 'Y':
        for num in range(0,100000):
            headOrTails = flip()
            if headOrTails == 'heads':
               heads +=1
            else:
               tails +=1
    
    print ("Heads is {heads}".format(**locals()))
    print ("Tails is {tails}".format(**locals()))

main()

