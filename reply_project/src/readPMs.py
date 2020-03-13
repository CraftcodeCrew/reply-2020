def read_pms(pms):
    useless_shits = []
    for pm in pms:
        descriptions = pm.split(' ')
        useless_shits.append(descriptions)
    return useless_shits
