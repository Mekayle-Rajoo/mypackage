def top_n(items,n):
    """this is going to return the top n items in an array in 
    descending order
    
    Args:
        items (array)- list or an array type object
        n (int)- number of items to return
        
    Return:
         Array: Top n numbers in descending order"""

    items.sort(reverse= True)
    items=items[0:n]

   

    return items
