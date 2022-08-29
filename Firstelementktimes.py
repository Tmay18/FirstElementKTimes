"""
Given an array of N integers. Find the first element that occurs at least K number of times.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function firstElementKTime()
which takes the array A[], its size N, and an integer K as inputs and returns the required answer.
If the answer is not present in the array, return -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N, K <= 105
1<= A <= 106
"""
def firstElementKTime(a, n, k):
        dict={}
        ktimes=[]
        indexx=[]
        for x in a:
            if x in dict:
                #to increment the occurence of a number that existed before
                dict[x]+=1
                if dict[x]==k:
                    element_ktimes=x
                    return element_ktimes
            else:
                #to store the first occurence of a number and assign it value 1
                dict[x]=1
                if dict[x]==k:
                    element_ktimes=x
                    return element_ktimes
        return -1
n=int(input("Enter a Natural number for the size of an array"))
array=[]
for i in range(0,n):
    element=int(input("Enter the number"))
    array.append(element)
k=int(input("Enter the no of times you want to check the occurence of element"))
Soln=firstElementKTime(array,n,k)
if Soln==-1:
    print("no such number found")
else:
    print("First element to occur",k," times is:",Soln)
