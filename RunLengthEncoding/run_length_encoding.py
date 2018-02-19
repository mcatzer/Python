def encode( InpStr ):
    count = 1
    prevCh = ''
    lst = []
    for character in InpStr:
        if character != prevCh:
            if prevCh:
                if count > 1:
                    lst.append( count )
                lst.append( prevCh )
            count = 1
            prevCh = character
        else:
            count += 1
    else:
        if count > 1:
            lst.append( count )
        if str(InpStr):
            lst.append( character )
    return ''.join(map(str, lst))

def decode( InpStr ):
    count = 0
    lst = []
    for character in InpStr:
        if character.isnumeric():
            count = ( count*10 )+ int(character)
        else:
            if count > 0:
                lst.append(character * count)
            else:
                lst.append(character)
            count = 0
    return ''.join(map(str, lst))
