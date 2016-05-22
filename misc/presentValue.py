import math

def main():
    futureValue = 100
    discountRate = 0.1
    term = 0
    pvFloor = 1
    
    # Calculate when the PV will be equal to 0
    while (pvFloor > 0) :
        
        term +=1
        presentValue = futureValue / math.pow((1 + discountRate),term)
        print ("Present Value is " , presentValue, "for term ", term)

        pvFloor = math.floor(presentValue)

    print('PV will be 0 after ',term, ' years')

main()

input('Press any key to continue...')

