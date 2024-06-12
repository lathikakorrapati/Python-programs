s=['a','a','d','b','b','a']
s_new=list(set(s))
print("list after removing duplicates:",s_new)
s_ascen=sorted(s_new)
s_descen=sorted(s_new,reverse=True)
print("the list after arranging in ascending order:",s_ascen)
print("the list after arranging in descending order:",s_descen)
