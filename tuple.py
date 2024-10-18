#def count_vowels(s):
s=input()
flag=0
for a in s:
    if('a' in a or 'e' in a or 'i' in a or 'o' in a or 'u' in a or 'A' in a or 'E' in a
    or 'I' in a or 'O' in a or 'U' in a):
        flag+=1
        if(flag==0):
            print('0')
        else:
            print(flag)
