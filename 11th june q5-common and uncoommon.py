s1=[7,8,1,2,5,3]
s2=[8,6,4,7,0,2]
s_new=list(set(s1) & set(s2))
print(s_new)
unc=list(set(s1) ^ set(s2))
print(unc)