n=list(input())

for i in range(len(n)):
    if n[i]=="\\":
        n[i]="/"
n="".join(n)
print(n)