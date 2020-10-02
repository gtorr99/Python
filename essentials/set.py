# An ordered list. Doesn't accept a value twice

s = {1, 3, 4, 'Hello'}

s1 = {1, 3, 1, 7, 9}

print(s)
print(s1)

print(sum(s1))
print(sorted(s1))
print(any(s1)) # is there values whithin set s1? true : false
print(all(s1)) # is there any 0 or false in this set? false : true

s1.remove(1)
print(s1)

s1.add(1)
print(s1)

# Frozenset: read-only set
fs = frozenset({1, 3, 5})
print(fs)