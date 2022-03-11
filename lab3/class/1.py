class String:
    def __init__ (self):
        pass
    
    def get_string(self, string):
        self.string = string
    
    def print_string(self):
        return self.string.upper()
        
Mystr = String()
Mystr.get_string(input())
print(Mystr.print_string())