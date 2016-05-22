def checkGraduate(points):
    ''' Return if the student has graduated or not
    '''
    passOrFail = 'p'
    if int(points) < 120:
        passOrFail = 'FAIL'
    else:
        passOrFail = 'PASS'
    
    return passOrFail
    
def main():
    points = int(input('Enter your points please > '))
    result = checkGraduate(points)
    print('Your graduation result is for {points} is {result}'.format(**locals()))

main()

