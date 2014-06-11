import re

class Matrix:
	mas = []
	rows = 0
	columns = 0

	def __init__(self):
		a = 0

	def __getitem__(self,index):
		return self.mas[index[0] * self.columns + index[1]]

class equations:
    Amat  = []
    Bmat = []
    Xmat = []
    AmatHeight = 0
    AmatWidth = 0 

    def __init__(self):
        file = open("test.txt")
        o = [] #auxilary matrix
        self.AmatHeight = 0
        self.Amat = []  # The list of the coficents of variables 
        self.Bmat = []  # The list of numbers after '=' o_O
        self.Xmat = []  # The list of variables
        while 1:
            line = file.readline()
            if not line:
                break
            line = line.strip('\n')
            line = line.replace(' ','')
            array = line.split('=') # break the line in two parts
            lline = array[0]    # part with variables
            rline = array[1]    # the part following '='
            digits = re.compile('[0-9]+')
            lst = digits.findall(lline) #the list of value of the left part
            charts = re.compile("[a-z]")
            lst1 = charts.findall(lline)    #the list if variables of the left part
            znaki = re.compile("[^a-zA-Z0-9_]")
            lst2 = znaki.findall(lline) #the list of symbols of the left part
            self.AmatHeight = self.AmatHeight+1
            self.AmatWidth = len(lst)
            o = []
            rlst = digits.findall(rline)    #the list of value of the right part
            rlst2 = znaki.findall(rline)    #the list of symbols of the right part

            for i in range(len(lst)):   # this thing makes a list of cofficients
                o.append(0)             # of the left part
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

            if rlst2 == []:             # this one make a list of coefficients of the right part
                self.Bmat.append(int(rlst[0]))
            else:
                self.Bmat.append(-int(rlst[0]))


            D = {}
            for i in range(len(lst1)):  
                D[lst1[i]] = o[i]
            self.Xmat = D.keys()        # creates a list of variable
            self.Xmat.sort()            # and sorts it

            for i in self.Xmat:
                self.Amat.append(D[i])  # adds coefs to Amatrix in order of valuables
        print self.Amat , self.Bmat, self.Xmat, self.AmatHeight , self.AmatWidth


a = equations()
b = a.Bmat
print b





#print Matrix()