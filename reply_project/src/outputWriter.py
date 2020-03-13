# Input: [[8, 4], ['x'], [2, 1]]
# Output: txt UTF8

def write(output, filename):
    naame = filename + '_output.txt'
    with open(naame, 'wb') as f:
        for _list in output:
            for _string in _list:
                if len(_list) < 2 :
                    
                    f.write(str(_string).encode('ASCII'))  
                else:
                    if _list.index(_string) == 0 :
                       
                        f.write(str(_string).encode('ASCII') + " ".encode('ASCII'))
                    else:
                       
                        f.write(str(_string).encode('ASCII'))
            f.write('\n'.encode('ASCII'))
        f.close()
    print(naame)