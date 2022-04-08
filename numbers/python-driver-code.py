# Python Driver Code

def solve(n: int) -> str:
  # Your code goes here
    l=[]
s=str(n)
x=len(s)//2
print(x)
if (len(s)%2==0):
    l=list(s)
    x=int(x)
    p=l[:x]
    q=l[x:]
   
    s1 = [str(i) for i in p]
     
   
    res1 = int("".join(s1))
    s2 = [str(i) for i in q]
     
   
    res2 = int("".join(s2))
   
    if res1 > res2 :
        return "magic number"
    else:
        return "normal number"
else:
    x=int(x)
    l=list(s)
    p=l[:x]
    q=l[x+1:]
    s1 = [str(i) for i in p]
     
   
    res1 = int("".join(s1))
    s2 = [str(i) for i in q]
     
   
    res2 = int("".join(s2))
   
    if res1 > res2 :
        print("magic number")
    else:
        return "normal number"

  # n is the given input
  return "Special"

# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  test_case = input()
  answer = solve(test_case)
  print(answer)
