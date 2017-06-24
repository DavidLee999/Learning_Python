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
    
def permu(s):

    s_copy = list(s)
    if s_copy:
        results = []
    
        for ele in s_copy:
        
            temp = s_copy[:]
        
            temp.remove(ele)
        
            for res in permu(temp):
            
                results.append([ele] + res)
    
        return results
        
    else:
        
        return [[]]
    
    
a = permu('abc')

print(a)
# def get_all_permu(some_list):

    # if some_list:

        # all_p = []   #定义全部排列为一个列表

        # for x in some_list:  #第一次遍历：遍历列表中的所有元素

            # temp = some_list[:]

            # temp.remove(x)  #得到不包含x的列表

            # for y in get_all_permu(temp):  

            # #第二次遍历：遍历不包含x的所有元素的组合，这也是递归实施的地方

                # all_p.append([x] + y)  

               # #将x与不包含x的其他元素的所有组合放在一起，组成一个原列表的排列

        # return all_p

    # else:

        # return [[]] 