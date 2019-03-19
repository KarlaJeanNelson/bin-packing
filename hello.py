import csv
from operator import itemgetter
max_vol = 1.58
group_by_type = True

class Bin(object):
    """ Container for items that keeps a running sum """
    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        item.append(id(self))
        self.items.append(item)
        self.sum += item[2]

    def __str__(self):
        """ Printable representation """
        return '%s' % str(self.items)
        
def convert_vol(s):
    try:
        return float(s)
    except ValueError:
        return s

def getlist():
    with open('items.csv', 'rb') as f:
        itemlist = list(csv.reader(f))
        del itemlist[0]
        for val in itemlist:
           newvol = convert_vol(val[2])
           val[2] = newvol
    sorted_list = sorted(itemlist, key=itemgetter(2), reverse=True)
    return sorted_list
    
def getgroups(itemlist):
    grouplist = set()
    for val in itemlist:
        grouplist.add(val[1])
    return grouplist
    
def filter_group(group, mylist):
    grouped = []
    print group
    for elem in mylist:
        if elem[1] == group:
            grouped.append(elem)
    # print grouped
    # print
    return grouped

def pack(values, maxvol):

    bins = []

    for item in values:
        # Try to fit item into a bin
        for bin in bins:
            if bin.sum + item[2] <= maxvol:
                # print 'Adding', item, 'to', bin
                bin.append(item)
                break
        else:
            # item didn't fit into any bin, start a new bin
            #print 'Making new bin for', item
            bin = Bin()
            bin.append(item)
            bins.append(bin)

    return bins
    
if __name__ == '__main__':

    def packAndShow(aList, maxValue):
        bins = pack(aList, maxValue)

        print 'Solution using', len(bins), 'boxes:'
        for bin in bins:
            print bin

        print
        
    def write_to_file(aList, maxValue):
        if group_by_type:
            bins = []
            groups = getgroups(aList)
            for group in groups:
                grouplist = filter_group(group, aList)
                grpbins = pack(grouplist, maxValue)
                bins.extend(grpbins)
        else:
            bins = pack(aList, maxValue)
        header = ['item_id','item_group','cubic_volume_ft','bid_id']
        with open("output.csv", "w+") as f:
            writer = csv.writer(f)
            writer.writerows([header])
            for bin in bins:
                writer.writerows(bin.items)
        
aList = getlist()
# packAndShow(aList, max_vol)
write_to_file(aList, max_vol)