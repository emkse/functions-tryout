def nmlf():
    naam = 'naam: '
    leeftijd = 'leeftijd: '
    while naam != 'stop' and leeftijd != 'stop':
        naam = input('naam: ')
        if naam == 'stop':
            break
        leeftijd = input('leeftijd: ')
        if leeftijd == 'stop':
            break
        
        print('hallo', naam,'je leeftijd is', leeftijd, 'jaar' )
nmlf()

