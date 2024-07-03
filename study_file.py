stroka = "Hello world"
print(stroka)
spisok = stroka.split(' ')
print(spisok)
new_stroka = ' '.join(spisok)
print(new_stroka)
spisok = spisok.reverse()
sp = ''
for n in stroka:
    if n is str:
        sp += n
    else:
        sp += n

        
print(sp)
