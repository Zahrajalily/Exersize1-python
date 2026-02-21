
names=[ "zahra" ,"maryam" ,"nazanin" ,"shiva ","maral" ,"faranak" ,"sodabe" ,"baran" ]

x=[]

for name in names:
    if name[1] == "a" :
        x.append(name)

    
print("اسم هایی که حرف دومشان a : "x)

a=[]
for word in names:
    if word[-1] == "n" :
        a.append(word)

print("اسم هایی که حرف اخرشان n : "a)
