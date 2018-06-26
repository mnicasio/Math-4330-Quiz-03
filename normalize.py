
def maxValue(vector):
    """[This function takes a vector and returns the largest absolute value of that vector]
    
    Arguments:
        vector {[list]} -- [this is a list of numbers]
    
    Returns:
        [newMax] -- [this is the largest number from the numbers in the vector]
    """
    newMax = 0
    "This is where we will store the largest number from the vector"
    for i in range(len(vector)):
        "this loops through each number from the vector and compares them until the largest number is found"
        if abs(vector[i]) > newMax:
            newMax = abs(vector[i])
    return newMax 

"This function loops through each number in the vector and takes the absolute value and then returns the largest number"
def infinNorm(vector):
    """[summary]
    
    Arguments:
        vector {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    newVector = []
    "this is where we will store the new vector"
    for i in range(len(vector)):
        "this loops through each number in the vector and returns the absolute value of the number"
        newVector.append(abs(vector[i]))
    return maxValue(vector) 

"This function takes each number in the vector and divides it by the max absolut value of the vector and then returns the new vector, this should result in the new max number being 1"    
def normalize(vector):
    """[summary]
    
    Arguments:
        vector {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    ans = [] 
    "this is where we will store the new vector"
    scalar = infinNorm(vector)
    "this will store the value for the infinity Norm of the vector"
    for i in range(len(vector)): 
        "this loops through each element in the vector and returns the value divided by the infinity norm"
        ans.append(vector[i]/scalar) 
    return ans 

"These are the three test parameters to use in the function, only the first set of parameters should work the other two should not work because the second  parameter is not the right dimension and the third  parameter is a string"

vector01 = [1,2,-4]
vector02 = 3
vector03= "five"

"this prints out the function using the vectors as parameters"
print(normalize(vector01))
#print(normalize(vector02))
#print(normalize(vector03))
