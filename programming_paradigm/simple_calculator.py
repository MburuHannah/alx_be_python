class SimpleCalculator:
    
    def add(self,f,g):
        return f+g
    def subtract(self,f,g):
        return f-g
    
    def multiply(self, f,g):
        return f*g
    def divide(self,f,g):
        try:
            f/g==0   
        except ZeroDivisionError:
           return None
        else:
         return f/g
     
    
    