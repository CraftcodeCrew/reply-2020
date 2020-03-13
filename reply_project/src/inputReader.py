import re

def read_file(file):
    with open(file) as f:
        content = f.read()
        contentsplit = re.split('^\d.*$', content, flags=re.MULTILINE)
        #print(map)
        #print("map:")
        #print(contentsplit[1].strip().split())
        #print("devs:")
        #print(contentsplit[2].strip().split('\n'))
        #print("pms:")
        #print(contentsplit[3].strip().split('\n'))
        return contentsplit[1].strip().split(), contentsplit[2].strip().split('\n'), contentsplit[3].strip().split('\n')

read_file('../a_solar.txt')