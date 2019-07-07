m1=int(input())
a1b1=m1
sum=0
while m1>0:
  b1=m1%10
  sum=sum+b1*b1*b1
  m1=m1//10
if a1b1==sum:
  print("yes")
else:
  print("no")
