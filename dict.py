d={}
n=int(input("Enter number of students"))
for i in range(n):
    k=input("enter name of the student")
    v=int(input("enter marks"))
    d[k]=v
s=input("enter student name")
for i in d:
    m=d[i] if i==s else 0
print(s,"'s marks is:", m if m!=0 else "student not found")