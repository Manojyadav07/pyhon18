a1=int(input())
ab=a1
sum=0
while a1>0:
  b=a1%10
  sum=sum+b*b*b
  a1=a1//10
if ab==sum:
  print("yes")
else:
  print("no")
