def partition(n,m): 
  # form n with integers in [|1,m|] (no gap)
  #ex: 4 = 4x1,3x1+1x1,2x2,2x1+1x2,1x4 -> 5 possibilities
  count = 0 # Number of possible arrangements
  if n==2 and m>=2:
    return 2
  elif n==2 and m==1:
    return 1
  if n==1 and m>0:
    return 1
  if m==0:
    return 0
  # Loop through "coins" (integers...) of decreasing value
  for coin in range(m,0,-1):
    amount = n
    #r = n%coin
    #q = (n-r)/coin #(=n//coin dans certains cas)
    # Check how many times the current coin can be used to reach the desired amount n
    q = n//coin
    r = n-q*coin
    # Use combinations of fewer and fewer high-value coins
    for k in range(q,0,-1):
      r = n-k*coin
      if r == 0:
        count+=1
      else:
        if (coin>1):
          count += partition(r,coin-1)
  return count

number = 20
print("Les {0:2d} premières partitions d'entiers:".format(number))
for k in range(1,number+1,1):
  print(partition(k,k),end=', ')

print("")
print("Les {0:2d} premières partitions d'entiers sans l'unité 1:".format(number))
for k in range(1,20,1):
  print(partition(k+1,k+1)-partition(k,k),end=', ')
