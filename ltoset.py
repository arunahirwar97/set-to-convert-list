a = int(input("Enter any number :"))
b = int(input("Enter any number :"))
c = int(input("Enter any number :"))
d = int(input("Enter any number :"))
e = int(input("Enter any number :"))
f = int(input("Enter any number :"))
print('print all values is set')
g = {a,b,c,d,e,f}
print('Set : ',g)
print("above set convert into list")
h = [g,a,b]
print('List :',h)
h.append(a)
h.append(b)
h.append(c)
h.append(d)

print(h)

