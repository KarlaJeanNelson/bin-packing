import csv
from operator import itemgetter
max_vol = 1.58
group_by_type = False
binlist=[]

def convert_vol(s):
    try:
        return float(s)
    except ValueError:
        return s

def sortlist(list):
    sorted_list = sorted(list, key=itemgetter(2), reverse=True)
    return sorted_list

def getlist():
    with open('items.csv', 'rb') as f:
        itemlist = list(csv.reader(f))
        del itemlist[0]
        for idx, val in enumerate(itemlist):
           newvol = convert_vol(val[2])
           val[2] = newvol
    return sortlist(itemlist)
    
print getlist()

def binitems(sortedlist):
    return binlist
