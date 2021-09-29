class Father:  
	def dad(self):  		
	    print("Father")
	def fun(self):  
	    print("Dancer") 
           
class Mother:  
    def mom(self):  		
	    print("Mother")        
     
class Child(Father, Mother):  
	def fun(self):  
	    print("Both dancer and singer") 

obj = Child()
obj.fun()		 	
obj.mom()	
obj.dad()	