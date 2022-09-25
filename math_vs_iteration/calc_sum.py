n,p = 11,5

#\sum_i^n\sum_j^p(i+j)
sumij = 0
for i in range(1,n+1,1):
    for j in range(1,p+1,1):
        sumij += i+j
math_formula = n*p*(n+p+2)//2
print("La somme itérée (O(n^2)) est ",sumij)
print("La formule mathématique (O(1)) donne ",math_formula)

#\sum_{i<j<=n} (ij)
sum0 = 0
for i in range(1,n,1):
    for j in range(i+1,n+1,1):
        sum0 += i*j

math_formula0 = n*(n-1)*(3*n**2+5*n+2)//24
print("La somme itérée (O(n^2)) est ",sum0)
print("La formule mathématique (O(1)) donne ",math_formula0)
