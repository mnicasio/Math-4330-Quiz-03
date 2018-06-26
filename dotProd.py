
def dotProd(vector, vector2):
  """[This function takes two vectors as its parameters and returns the dot product]
  
  Arguments:
    vector {[list]} -- [this will be a list of numbers ]
    vector2 {[list]} -- [this will be a list of numbers]
  
  Returns:
    [ans] -- [this is the new vector that was created after the dot product operation was taken]
  """
  ans = []
  "this is where we store the new vector"
  y = 0 
  "this is where we will add each element that undergoes multiplication"
  for i in range(len(vector)):
    for j in range(len(vector2)):
      "this loops through all elements of the two vectors and multiplies them and then adds them together "
      y += vector[i]*vector2[j]
    ans.append(y)
    "this adds the new value for y into the new vector"
    return ans 

"These are the three test parameters to use in the function, only the first set of parameters should work the other two should not work because the second set of parameters are not the right dimensions and the third set of parameters are not numbers"
vector = [1,2,3]
vector2 = [4,5,6]

vector3 = 3
vector4 = [1,2,3]

vector5 = "one, two, three"
vector6= "five"

"this prints out the function using the vectors as parameters"
print(dotProd(vector, vector2))
#print(dotProd(vector3, vector4))
#print(dotProd(vector5, vector6)

