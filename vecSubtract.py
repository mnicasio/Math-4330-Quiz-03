
def vecSubtract(vector1, vector2):
    """[This vector takes two vectors and then iterates through each element of each vector and then subtracts them together and returns their subtraction result]
    
    Arguments:
        vector1 {[list]} -- [this is a list of numbers]
        vector2 {[list]} -- [this is a list of numbers]
    
    Returns:
        [ans] -- [this is the new vector that was created from the subtraction of our first two vectors]
    """
    ans = []
    "this is where we will store the new vector"
    for i in range(len(vector1)):
        for j in range(len(vector2)):
            "this loops through each element in each vector and subtracts them together"
            ans.append(vector1[i]- vector2[j])
        return ans

"These are the three test parameters to use in the function, only the first set of parameters should work the other two should not work because the second set of parameters are not the right dimensions and the third set of parameters are not numbers"
vector01 = [1,2,3]
vector02 = [3,4,5]

vector03 = 3
vector04 = [1,2,3]

vector05 = "one, two, three"
vector06 = "five"

"this prints out the function using the vectors as parameters"
print(vecSubtract(vector01,vector02))
#print(vecSubtract(vector03,vector04))
#print(vecSubtract(vector05,vector06))