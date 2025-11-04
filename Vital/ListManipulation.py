
def removeElementFromList(ls:list,ii:list):
    """REFL : remove element from list
    """
    li=[]
    for i in ls: 
        sub_li=[]
        if type(i)==list:
            for si in i:  
                if si not in ii:
                    #print(si) 
                    sub_li.append(si)
            li.append(sub_li)
        else:
           if i not in ii:
                    #print(si) 
                    li.append(i) 
    return li

def indexOfItems(li:list, re:any)->list:
    """IOT : index of items ,lol I just coppied it from the internet

    returns the indices of reapting elemnt `re` in `li`
    
    Args:
        li: list to search the repeating element for
        re : reapeting element to be searched
        
    ex : `li`=[0,20,4,5,20] `re`=20 , return is [1,4]

    """
    
    index_val = [] 
    i=0 #counter
    while i != len(li):
        try:
            ind = li[i:].index(re) #checking the index this line trims the first part of the list that dosent contain any instance of re
            index_val.append(ind+i)
            i = ind+1+i
        except ValueError:
            i = len(li)
    return index_val

def mostFrequentElement(lis):
	element_counts = set(lis)
	most_frequent_element = max(element_counts, key=lis.count)
	return most_frequent_element

def GetColoumsOf2DArray(matrix:list):
    cols = [ [] for _ in range(len(matrix[0])) ]
    
    for row in matrix:
        for blk_index,blk in enumerate(row):
            cols[blk_index].append(blk)
            
    return cols

