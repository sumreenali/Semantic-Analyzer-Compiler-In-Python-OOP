
class VariableObject(object):

    def __init__(self):
        # this will hold the exec string for the variable declaration
        self.exec_string = ""

    def transpile(self,name,operator,value):
        # Append the python executable string converted using our parser
        self.exec_string +=name + " " + " " + operator + " " + value + "\n"
        return self.exec_string
