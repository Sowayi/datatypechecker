def data_type (x):
    
    if type (x) == str:
        
        return len (x)
    
    elif type (x) == None:
        
        return 'no value'
    
    elif type(x) == bool:
        
        return x
    
    if x == []:
        
        return x[2]
    
        #if lenth of whole list is smaller than length of list bearing 3 elements
    
        if len (x[:])< len(x[:2]):
            
            return None
    
    if type (x) == int:
        
        if x == 100:
            
            return 'equal to 100'
        
        elif x < 100:
            
            return 'less than 100'
        
        elif x > 100:
        
            return 'more than 100'
    
    
    
    

data_type ("home")
