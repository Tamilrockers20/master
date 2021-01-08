stack=[]
size=5
top=-1
ok=1
while ok==1:
 print("1.push 2.pop 3.top\n")
 c=input("enter ur choice: ")
 if c=="1":
  n=int(input("enter the element to push: "))
  if(top==size-1):
   print("stack overflow !!!")
  else:
   top+=1
   stack.insert(top,n)
  
 elif c=="2":
  if(top==-1):
   print("stack underflow !!!")
  else:
   print(stack[top]," is popped ")
   top-=1

 elif c=="3":
  print("top : ",stack[top])
 for i in range(0,top+1):
  print(stack[i],end=" ")
 print("\n")
 ok=int(input("enter 1 to continue : "))
