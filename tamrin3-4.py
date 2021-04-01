a = "python is a powerful programming language"

wc = 1

for i in range(len(a)):
     if (a[i] == ' '):
        wc += 1

print(wc)