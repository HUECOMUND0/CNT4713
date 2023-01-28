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
        year_str = str(self.year)
        first_two_digits = year_str[:2]
        first_two_digits_repeated = first_two_digits * n
        odd_digits = "".join([year_str[i] for i in range(1, len(year_str), 2)])
        odd_digits_repeated = int(odd_digits) * n
        return first_two_digits_repeated + str(odd_digits_repeated)

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
    
#     ret = Assignment2.checkGoodString("f1obar0more")
#     print(ret)

#     ret = Assignment2.checkGoodString("foobar0more")
#     print(ret)
    
#     retval = Assignment2.connectTCP("www.google.com", 80)
#     if retval:
#         print("Connection established correctly")
#     else:
#         print("Some error")