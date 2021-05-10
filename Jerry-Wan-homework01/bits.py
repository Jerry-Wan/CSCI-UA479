# Part 1 goes here!
class DecodeError(Exception):
    pass

class ChunkError(Exception):
    pass

class BitList():
    def __init__(self,string):
        self.string = string
        for a in range(len(self.string)):
            if self.string[a] != '1' and self.string[a]!= '0' and self.string[a]!= 0 and self.string[a]!= 1:
                raise ValueError('Format is invalid; does not consist of only 0 and 1')

    def __eq__(self, other):
        if len(str(self)) != len(str(other)):
            return False
        strSelf = str(self)
        strOther = str(other)
        for a in range(len(strSelf)):
            if strSelf[a] != strOther[a]:
                return False
        return True

    @staticmethod
    def checkValue(self):
        for a in range(len(self.string)):
            if self.string[a] != '1' and self.string[a]!= '0' and self.string[a]!= 0 and self.string[a]!= 1:
                raise ValueError('Format is invalid; does not consist of only 0 and 1')
        
    @staticmethod
    def from_ints(*a):
        results = ''
        for b in a:
            results+=str(b)
        results = BitList(results)
        #results.checkValue()
        return results

    def __str__(self):
        return(self.string)

    def arithmetic_shift_left(self):
        new_string = self.string[1:]
        new_string +='0'
        self.string = new_string

    def arithmetic_shift_right(self):
        new_string = self.string[0]
        for a in range(len(self.string)-1):
            new_string += self.string[a]
        self.string = new_string

    def bitwise_and(self,otherBitList):
        result = ''
        for a in range(len(self.string)):
            if self.string[a] == otherBitList.string[a]  == '1':
                result += '1'
            else:
                result += '0'
        return result

    def chunk(self,chunk_length):
        if len(self.string)%chunk_length != 0:
            raise ChunkError("raises a ChunkError!")
        count = 0
        result = []
        temp = []
        for a in range(len(self.string)):
            count+=1
            temp.append(int(self.string[a]))
            if count%chunk_length == 0:
                result.append(temp)
                temp = []
        return result

    def decode_single(self,string):
        if len(string) == 8:
            if string[0] == '1':
                raise DecodeError("Sorry, invaild format.") 
            else:
                return chr(int(string,2))
        elif len(string) == 16:
            strings = string[2:8]+ string[10:]
            return chr(int(strings,2))
        elif len(string) == 24:
            strings = string[3:8]+ string[10:16]+string[18:]
            return chr(int(strings,2))
        else:
            strings = string[4:8]+ string[10:16]+string[18:24]+string[26:]
            return chr(int(strings,2))
    
    def decode(self,encoding='utf-8'):
        checkFlag = True
        if encoding == 'us-ascii' and len(self.string)%7 != 0:
            raise DecodeError("Sorry, invaild format.")
        if encoding == 'utf-8':
            
            if self.string[0] != '1' and len(self.string) > 8:
                raise DecodeError("Sorry, invaild format.")
            if self.string[0]=='1' and len(self.string) == 8:
                raise DecodeError("Sorry, invaild format.")
            if len(self.string)>8:
                count = 0
                for a in range(4):
                    if self.string[a] == '1':
                        count +=1
                if count*8 != len(self.string) and len(self.string)<=32:
                    checkFlag = False
                for b in range(len(self.string)-1):
                    if b%8 == 0 and b >0 and b%32 != 0:
                        if self.string[b] != '1':
                            checkFlag = False
            if checkFlag == False:
                raise DecodeError("Sorry, invaild format.")
        if encoding == "us-ascii":
            final_result = ""
            result = ""
            for a in range(len(self.string)):
                result +=  self.string[a]
                if (a+1)%7 == 0:
                    final_result += chr(int(result,2))
                    result = ""
            return final_result
        else:
            if len(self.string)%8 != 0:
                raise ValueError('Format is invalid')
            elif len(self.string) <=32:
                return self.decode_single(self.string)
            else:
                result = ""
                chars = []
                single = ""
                for a in range(len(self.string)):
                    single += self.string[a]
                    if (a+1)%32 == 0:
                        chars.append(single)
                        single =""
                if len(single) >0:
                    chars.append(single) 
                final_result = ""
                for a in range(len(chars)):
                    final_result += self.decode_single(chars[a])
                return final_result