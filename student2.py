class student:
    def __init__(self, name, rollNum, javaMarks, pythonMarks, mathsMarks):
        self.name = name
        self.rollNum = rollNum
        self.javaMarks = javaMarks
        self.pythonMarks = pythonMarks
        self.mathsMarks = mathsMarks
    def printAllDetails(self):
        print(self.name)
        print(self.rollNum)
        print(self.javaMarks)
        print(self.pythonMarks)
        print(self.mathsMarks)
obj = student("kumar", 501, 67, 45, 78)
obj.printAllDetails()
    

    
