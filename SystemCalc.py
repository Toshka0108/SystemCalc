import re

class Matrix:
	mas = []
	rows = 0
	columns = 0

	def __init__(self):
		a = 0

	#def __getitem__(self,index):
	#	return self.mas[index[0] * self.columns + index[1]]

class equations:
    Amat = []
    Bmat = []
    Xmat = []
    AmatHeight = 0
    AmatWidth = 0 

    def __init__(self):
        file = open("test.txt")
        o = []
        self.AmatHeight = 0
        self.Amat = []
        self.Bmat = []
        self.Xmat = []
        while 1:
            line = file.readline()
            if not line:
                break
            line = line.strip('\n')
            line = line.replace(' ','')
            array = line.split('=')
            lline = array[0]
            rline = array[1]
            digits = re.compile('[0-9]+')
            lst = digits.findall(lline)
            charts = re.compile("[a-z]")
            lst1 = charts.findall(lline)
            znaki = re.compile("[^a-zA-Z0-9_]")
            lst2 = znaki.findall(lline)
            self.AmatHeight = self.AmatHeight+1
            self.AmatWidth = len(lst)
            o = []
            rlst = digits.findall(rline)
            rlst2 = znaki.findall(rline)
            for i in range(len(lst)):
                o.append(0)
            if len(lst) == len(lst2):
                for i in range(len(lst)):
                    if lst2[i] == '-':
                        o[i] = -int(lst[i])
                    else:
                        o[i] = int(lst[i])
            else:
                o[0] = int(lst[0])
                for i in range(len(lst2)):
                    if lst2[i] == '-':
                        o[i+1] = -int(lst[i+1])
                    else:
                        o[i+1] = int(lst[i+1])
            if rlst2 == []:
                self.Bmat.append(int(rlst[0]))
            else:
                self.Bmat.append(-int(rlst[0]))
            D = {}
            for i in range(len(lst1)):
                D[lst1[i]] = o[i]
            self.Xmat = D.keys()
            self.Xmat.sort()
            for i in self.Xmat:
                self.Amat.append(D[i])
        print self.Amat , self.Bmat, self.Xmat, self.AmatHeight , self.AmatWidth


a = equations()





#print Matrix()