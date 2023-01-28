class Assignment2:
    def __init__(self, year):
        self.year = year
        
    def tellAge(self, currentYear):
        age = currentYear - self.year
        print("Your age is", age)
        
    def listAnniversaries(self):
        anniversaries = []
        for i in range(10, 2022 - self.year + 1, 10):
            anniversaries.append(i)
        return anniversaries
    
    def modifyYear(self, n):
        val = ""
        y = ""
        year = str(self.year)
        index1 = year[0]
        index2 = year[1]
        for i in range(n):
            val += index1 + index2
        x = str(self.year * n)
        for i in range(0, len(x)):
            if(i % 2 == 0):
                y += x[i]
        return val + y

    def checkGoodString(string):
        if len(string) >= 9 and string[0].islower() and sum(i.isdigit() for i in string) == 1:
            return True
        else:
            return False
        
    def connectTcp(host, port):
        import socket
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.close()
            return True
        except:
            return False
    
# class TestAssignment2:
#     a = Assignment2(1782)
#     ret = a.modifyYear(3)
#     print(ret)
#    
#     ret = Assignment2.checkGoodString("f1obar0more")
#     print(ret)
# 
#     ret = Assignment2.checkGoodString("foobar0more")
#     print(ret)
# 
#     retval = Assignment2.connectTCP("www.google.com", 80)
#     if retval:
#         print("Connection established correctly")
#     else:
#         print("Some error")