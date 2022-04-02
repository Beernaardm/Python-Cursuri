t = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(t)
print(" ") #introduce un spatiu gol intre afisari

p = t #p reprezinta variabila pentru elementele pare din lista
for a in p:
    if a % 2 == 0:
        print(a)


print(" ") #introduce un spatiu gol intre afisari
imp = t #imp  reprezinta variabila pentru elementele impare din lista
for a in imp:
    if a % 2 == 1:
        print(a)


print(" ") #introduce un spatiu gol intre afisari
d = t
for a in  d:
    if a % 3 == 0:
     print(a)


print(" ")#introduce un spatiu gol intre afisari
c = t #c reprezinta variabila pentru lista ordonata ascendenst
c.sort()
print(c)

print(" ")#introduce un spatiu gol intre afisari
i = t  #i reprezinta variabila pentru lista ordonata descendent
i.sort(reverse=True)
print(i)

