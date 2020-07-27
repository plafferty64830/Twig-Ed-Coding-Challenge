# -*- coding: utf-8 -*-
"""
Spyder Editor

Date: 27/07/2020
Creator: Patrick Lafferty

How and why this works?
-----------------------

In response to the Twig Education Coding Challenge, I decided to use the Python
programming language even though it is not one of my primary lanaguages. 
After data validation, the desired length of the 'equal' groups is determined.
Once the desired length is determined, the array is looped over in order to 
populate a temporary array with length equal to the desired length. This
temporary array is then appended to our result array. This process is repeated 
until the end of the array is reached.


"""

def groupArrayElements(A,N):
    #variable declaration
    lenSplit = 0
    counter = 0
    result = []
    temp = []
    numChunks = 0
    leftLen = 0
    
    
    #validate the input data to ensure data is valid
    
    #make sure A is a list and it is not empty
    if not isinstance(A,list) or not A:
        return "Parameter A is either an empty list or an unexpected type"
    #make sure N is an integer and it's positive
    if not isinstance(N,int) or N < 0:
        return "Parameter N is either less than 0 or an unexpected data type"
    

    
    #check to see if the array can be split into equal parts
    mod = len(A) % N
    
    #if list doesn't split into chunks of the same length
    if mod > 0:
        lenSplit = (len(A) - mod) / N
    #otherwise if list can be split into equal parts
    else:
        lenSplit = len(A) / N
        


    #loop through array passed to function
    for i in range(0,len(A)):
        counter += 1
        #if counter is equal to the target chunk length i.e. lenSplit 
        if counter == lenSplit:
            numChunks += 1
            #first append the current item to the temp array
            temp.append(A[i])
            #append our chunk (i.e. temp) to the result array
            result.append(temp)
            
            #empty the temp array and initialise the counter in preperation for the next iteration
            temp = []
            counter = 0
            
            if numChunks == (N - 1):
                leftLen = len(A)-1 - i
                break
            
            
        else:
            temp.append(A[i])
    
    
    #get the final chunk from the array: length of array - index when the for loop was broken to the end of the array
    lastChunk = A[len(A) - leftLen:len(A)]
    #append the last chunk to the resultant array
    result.append(lastChunk)
    
    return result





