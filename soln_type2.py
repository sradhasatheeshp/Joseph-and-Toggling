import math
n=int(input())
bin_dig_cnt=int(math.log2(n))+1  #binary digit count
k=(1<<bin_dig_cnt)-1 #left shift 1.bin_dig_cnt-1 times
print(n^k) #XOR n with k
