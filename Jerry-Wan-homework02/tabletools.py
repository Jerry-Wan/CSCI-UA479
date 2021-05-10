# tabletools.py
import csv

class LabeledList():
    def __init__(self,value = None,index = None):
        self.values = value
        self.index = index
        if self.index == None:
            result = []
            for a in range(len(value)):
                result.append(a)
            self.index = result
    
    def __str__(self):
        for a in range(len(self.values)):
            print(" "*(len(max(self.index))-len(self.index[a])-1),self.index[a],self.values[a])
        result = ''
        return result

    def __repr__(self):
        for a in range(len(self.values)):
            print(" "*(len(max(self.index))-len(self.index[a])-1),self.index[a],self.values[a])
        result = ''
        return result

    def __getitem__(self,key_list):
        if isinstance(key_list, list) == True:
            if type(key_list[0]) == bool:
                for a in range(len(key_list)):
                    if key_list[a] == True:
                        print(" "*(len(max(self.index))-len(self.index[a])-1),self.index[a],self.values[a])
            else:
                for a in range(len(key_list)):
                    for b in range(len(self.index)):
                        if self.index[b] == key_list[a]:
                            print(" "*(len(max(self.index))-len(self.index[b])-1),self.index[b],self.values[b])
        elif type(key_list) == str:
            for b in range(len(self.index)):
                        if self.index[b] == key_list:
                            print(" "*(len(max(self.index))-len(self.index[b])-1),self.index[b],self.values[b])
        elif isinstance(key_list, LabeledList) == True:
            print(type(key_list))
            for a in range(len(key_list.values)):
                for b in range(len(self.index)):
                        if self.index[b] == key_list.values[a]:
                            print(" "*(len(max(self.index))-len(self.index[b])-1),self.index[b],self.values[b])
        
    def __iter__(self):
        for a in range(len(self.values)):
            print(self.values[a])

    def __next__(self):
        for a in range(len(self.values)):
            yield self.values[a]

    def __eq__(self,scalar):
        lists = [self.values[i] == scalar for i in range(len(self.index))]
        result = LabeledList(lists, self.index)
        return result
    
    def __ne__(self,scalar):
        lists = [self.values[i] != scalar for i in range(len(self.index))]
        result = LabeledList(lists, self.index)
        return result
    
    def __gt__(self,scalar):
        lists = [self.values[i] > scalar for i in range(len(self.index))]
        result = LabeledList(lists, self.index)
        return result
    
    def __lt__(self,scalar):
        lists = [self.values[i] < scalar for i in range(len(self.index))]
        result = LabeledList(lists, self.index)
        return result

    def map(self,f):
        result = []
        for a in self.values:
            result.append(f(a))
        return LabeledList(result,self.index)
    
class Table():
    def __init__(self,values,index = None,columns = None):
        self.values = values
        self.index = index
        self.columns = columns
        if self.index == None:
            result = []
            for a in range(len(values)):
                result.append(str(a))
            self.index = result
        if self.columns == None:
            result = []
            for a in range(len(values[1])):
                result.append(str(a))
            self.columns = result

    def __str__(self):
        print(" "*2,end = "")
        for a in range(len(self.columns)):
            if a == 0:
                print(str(self.columns[a]).rjust(30),end ="")
            else:
                print(str(self.columns[a]).rjust(15),end ="")
        print("")
        for a in range(len(self.index)):
            print(str(self.index[a]).rjust(2),end = "")
            for b in range(len(self.columns)):
                if b == 0:
                    print(str(self .values[a][b]).rjust(30),end ="")
                else:
                    print(str(self.values[a][b]).rjust(15),end ="")
            if a< len(self.index)-1:
                print("")
        result = ''
        return result

    def __repr__(self):
        return str(self)

    def __getitem__(self, col_list):
        #print(type(col_list))
        #print('getit')
        if type(col_list) == list:
            #print('yeslist')
            if isinstance(col_list[0],bool):
                newIndex = []
                for a in range(len(self.index)):
                    if col_list[a] == True:
                        newIndex.append(self.index[a])
                #print(newIndex)
                datas = []
                for b in range(len(col_list)):
                    if col_list[b] == True:
                       datas.append(self.values[b])
                result = Table(datas,newIndex,self.columns)
                return result
            else:
                newData = []
                newCol = []
                for a in range(len(self.columns)):
                    if self.columns[a] in col_list:
                        newCol.append(self.columns[a])
                for b in range(len(self.index)):
                    temp = []
                    for a in range(len(self.columns)):
                        if self.columns[a] in col_list:
                            temp.append(self.values[b][a])
                    newData.append(temp)
                result = Table(newData,self.index,newCol)
                return result
        elif type(col_list) == str:
            check = []
            newData = []
            newCol = []
            for a in range(len(self.columns)):
                if self.columns[a] == col_list:
                    check.append(self.columns[a])
            for a in range(len(self.columns)):
                    if self.columns[a] in col_list:
                        newCol.append(self.columns[a])
            for b in range(len(self.index)):
                temp = []
                for a in range(len(self.columns)):
                    if self.columns[a] in col_list:
                        temp.append(self.values[b][a])
                if len(temp) == 1:
                    newData.append(temp[0])
                else:
                    newData.append(temp)
            if len(check) == 1:
                result = LabeledList(newData,self.index)
            else:
                result = Table(newData,self.index,newCol)
            return result
        elif isinstance(col_list, LabeledList) == True:
            #print('yesll')
            if type(col_list.values[0]) != bool:
                #print('no')
                newData = []
                newCol = []
                for a in range(len(self.columns)):
                    if self.columns[a] in col_list.values:
                        newCol.append[self.columns[a]]
                for b in range(len(self.index)):
                    temp = []
                    for a in range(len(self.columns)):
                        if self.columns[a] in newCol:
                            temp.append(self.values[b][a])
                    newData.append(temp)
                result = Table(newData,self.index,newCol)
                return result
            else:
                print('yes')
                newData = []
                newIndex = []
                for a in range(len(col_list.values)):
                    if col_list.values[a] == True:
                        newIndex.append(self.index[a])
                for b in range(len(self.values)):
                    if col_list.values[b] == True:
                        newData.append(self.values[b])
                result = Table(newData,newIndex,self.columns)
                return result

    def head(self,n):
        print(" "*2,end = "")
        for a in range(len(self.columns)):
            if a == 0:
                print(str(self.columns[a]).rjust(30),end ="")
            else:
                print(str(self.columns[a]).rjust(15),end ="")
        print("") 
        for a in range(n):
            print(str(self.index[a]).rjust(2),end = "")
            for b in range(len(self.columns)):
                if b == 0:
                    print(str(self.values[a][b]).rjust(30),end ="")
                else:
                    print(str(self.values[a][b]).rjust(15),end ="")
            if a< n-1:
                print("")

    def tail(self,n):
        print(" "*2,end = "")
        for a in range(len(self.columns)):
            if a == 0:
                print(str(self.columns[a]).rjust(30),end ="")
            else:
                print(str(self.columns[a]).rjust(15),end ="")
        print("") 
        for a in range(len(self.index)-n,len(self.index)):
            print(str(self.index[a]).rjust(2),end = "")
            for b in range(len(self.columns)):
                if b == 0:
                    print(str(self.values[a][b]).rjust(30),end ="")
                else:
                    print(str(self.values[a][b]).rjust(15),end ="")
            if a< len(self.index):
                print("")
    
    def startwith(self,n):
        newData = []
        for a in range(len(self.values)):
            if self.values[a][0].startswith(n) == True:
                newData.append(self.values[a])
        result = LabeledList(newData,self.index)
        return result
    
    def comlen(self,n):
        newData = []
        for a in range(len(self.values)):
            if len(self.values[a][0])<n:
                newData.append(self.values[a])
        result = LabeledList(newData,self.index)
        return result

    def shape(self):
        result = (len(self.index),len(self.columns))
        return result

def read_csv(fn):
    f = csv.reader(open(fn,'r'))
    allData = []
    for a in f:
        allData.append(a)
    data = []
    columns = allData[0]
    indexs = []
    for a in range(1,len(allData)):
        #indexs.append(allData[a][0])
        for b in range(len(allData[a])):
            try:
                allData[a][b] = float(allData[a][b])
            except ValueError:
                pass
        data.append(allData[a])
    result = Table(data,None,columns)
    #print(result.index)
    return result
