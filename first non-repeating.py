# Python program to print the first non-repeating character
NO_OF_CHARS = 256
 
# Returns an array of size 256 containg count
# of characters in the passed char array
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+=1
    return count
 
# The function returns index of first non-repeating
# character in a string. If all characters are repeating
# then returns -1
def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
 
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index
 
# Driver program to test above function
string = "geeksforgeeks"
index = firstNonRepeating(string)
if index==1:
    print "Either all characters are repeating or string is empty"
else:
    print "First non-repeating character is " + string[index]
 
# This code is contributed by Bhavya Jain