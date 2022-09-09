def ordering_beers(beers):
    if beers == 0: return 'Woda mineralna poprosze'
    if beers == 1: return 'Jedno piwo poprosze'
    if beers > 99 or beers < 0: raise ValueError
    numbers = ["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc" , "siedem", "osiem", "dziewiec", "dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie", "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"]
    bignum = ['','', "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]
    if str(beers)[-1] in '234' and beers not in [12, 13, 14]:
        bb = ' piwa'
    else:
        bb = ' piw'   
    if beers < 20:
        return numbers[beers].capitalize() + bb + ' poprosze'
    elif beers % 10 == 0:
        return bignum[int(str(beers)[0])].capitalize() + bb + ' poprosze'
    else:
        return bignum[int(str(beers)[0])].capitalize() + ' ' + numbers[int(str(beers)[1])] + bb + ' poprosze'
