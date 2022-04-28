def convert(number):
    sound_should_be=[]
    number = int(number)
    if number % 3 == 0:
        sound_should_be.append('Pling')
    if number % 5 == 0:
        sound_should_be.append('Plang')
    if number % 7 == 0:
        sound_should_be.append('Plong')
    if len(sound_should_be )>0:
        return(''.join(sound_should_be))
    else:
        return(str(number))