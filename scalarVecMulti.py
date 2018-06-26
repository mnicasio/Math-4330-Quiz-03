
def scalarVecMulti(scalar,vector):
    """["This function takes a scalar and a vector and iterates through each element of the vector and multiplies it by the scalar, the new result is then added to the empty vector ans, and then returns the result as the new vector ans"]
    
    Arguments:
        scalar {[integer]} -- [this is a single integer]
        vector {[list]} -- [this is a list of numbers]
    
    Returns:
        [ans] -- [this is the new vector created from the multiplication of the scalar with the vector]
    """
    ans =[]
    "we create a new empty list in which to place the new results"
    for i in range(len(vector)):
        "This loops through all the different elements of the vector and multiplies it by the scalar"
        ans.append(vector[i]*scalar)
    return ans 
"These are the three test parameters to use in the function, only the first set of parameters should work the other two should not work because the second set of parameters are not the right dimensions and the third set of parameters are not numbers"
vector01 = [1,2,3]
scalar01 = 3 

vector02 = 3
scalar02 = [1,2,3]

vector03 = "one, two, three"
scalar03 = "five"

"this prints out the function using the vectors as parameters"
print(scalarVecMulti(scalar01,vector01))
#print(scalarVecMulti(scalar02,vector02))
#print(scalarVecMulti(scalar03,vector03))