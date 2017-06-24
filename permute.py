def permute( s, low, high ):
   
    s_copy = list(s)
    
    if ( low == high ):
        
        print(s)
        
    else:
    
        i = low
        
        while( i <= high ):
            
            s_copy[low], s_copy[i] = s_copy[i], s_copy[low]
            
            permute( s_copy, low + 1, high )
            
            s_copy[low], s_copy[i] = s_copy[i], s_copy[low]
            
            i = i + 1

def permut( s ):

    permute( s, 0, len(s) - 1 )
    
permut('abcd')
