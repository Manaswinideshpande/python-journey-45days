import numpy as np

num = [1,2,3,4,5,6,7,8,9]
arr1 = np.array(num) 
reshape_arr =arr1.reshape(3,3)
print(arr1)
print(reshape_arr)# [[1 2 3]
                    #[4 5 6]
                    #[7 8 9]]

# Slicing 
print(reshape_arr[:,0]) #[1 4 7]
print(reshape_arr[0,:])#[1 2 3]

print(reshape_arr[0:1,0:1]) #[[1]]


print(reshape_arr[:,0:2])   #[[1 2]
                            #[4 5]
                            #[7 8]]
print(reshape_arr[0:2,0:2])        #[[1 2]
                                   #[4 5]]                        
                                   
 #copy Vs View
 # copy creates new array and it cannot get changed with respective to the original array ,
 # where as view is assigned value of original array and gets changed with respective to chages done in original array.
x= np.arange(11)
x1 = x # view
print(x)
print(x1)
x1[1] =10
print(x)
print(x1) # observation:x1 changed with respective to changes done in x array

print(np.shares_memory(x,x1))     # True 

x2 = np.copy(x) 
print(x)                         
print(x2)                         
x2[3] = 300
print(x)     # observation: x did'nt got changed when a value gets changed in x2                    
print(x2)                         


print(np.shares_memory(x,x2))     # False


z = x>3
print(z) # [f,t,f,f,t,t,t,t,t,t]
 
 
result1 = np.hstack((x,x2))
print(result1)

result2 = np.vstack((x,x2))
print(result2)

result3 = np.insert(x,4,x2)
print(result3)


result4 = np.delete(x,4)
print(result4)              #[ 0 10  2  3  5  6  7  8  9 10]



result5 = np.delete(x,9)                             #[ 0 10  2  3  4  5  6  7  8 10]
print(result5)

print(x)
# [ 0 10  2  3  4  5  6  7  8  9 10]

print(np.sin(x))
print(np.sin(0))

print(np.tan(x))
print(np.tan(0))

print(np.sum(x))
print(np.exp(x))
print(np.mean(x))

flatten_arr = x.flatten()

print(flatten_arr)
flatten_arr[0] = 1001
print(flatten_arr)


ravel_arr = x.ravel()
print(ravel_arr)
ravel_arr[0] = 1000
print(ravel_arr)
print(x)

