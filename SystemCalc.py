class Matrix:
	mas = []
	rows = 0
	columns = 0

	def __init__(self):
		a = 0

	#def __getitem__(self,index):
	#	return self.mas[index[0] * self.columns + index[1]]

class equations:
	t = 0

import re
file = open("test.txt")
o = []
free = []
while 1:
    line = file.readline()
    if not line:
        break
    line = line.strip('\n')
    line = line.replace(' ','')
    array = line.split('=')
    digits = re.compile('[0-9]+')
    lst = digits.findall(line)
    charts = re.compile("[a-z]")
    lst1 = charts.findall(line)
    znaki = re.compile("[^a-zA-Z0-9_]")
    lst2 = znaki.findall(line)
    members = array[0]
    dig = []
    for i in range(len(lst)):
    	dig.append(0)
    if len(lst) == len(lst2):
    	for i in range(len(lst)):
    		if lst2[i] == '-':
    			dig[i] = -int(lst[i])
    		else:
    			dig[i] = int(lst[i])
    else:
    	dig[0] = int(lst[0])
    	for i in range(len(lst2)):
    		if lst2[i] == '-':
    			dig[i+1] = -int(lst[i+1])
    		else:
    			dig[i+1] = int(lst[i+1])
    #for i in range(len(dig)-1):
    #	o.append(dig[i])
    free.append(dig[len(dig)-1])
    D = {}
    for i in range(len(lst1)):
    	D[lst1[i]] = dig[i]
    b = D.keys()
    b.sort()
    for i in b:
    	o.append(D[i]) 
    	#o.append(D[b])
    #members = members.split('+')
    #members = [x.split('-') for x in members]
    #a = line.find('=')
    print lst, lst1, lst2, dig, D,b
print o, free




#print Matrix()[1,2]