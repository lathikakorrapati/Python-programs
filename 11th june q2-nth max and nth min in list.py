s=[1,4,7,2,3,9,10,34,15,15]
s_new=list(sorted(set(s)))
print("the sorted list is:",s_new)
n=3
n_max=s_new[-n]
n_min=s_new[n-1]
print("the nth max in the sorted list is:",n_max)
print("the nth min in the sorted list is:",n_min)
