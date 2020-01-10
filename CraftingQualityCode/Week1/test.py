def count_startswith(L, ch):
    startswith = L[:]

    for item in L:
        if not item.startswith(ch):
	        startswith.remove(item)

    return len(startswith)

print(count_startswith(['rumba', 'salsa', 'samba'], 's'))

##def is_palindrome(s):
##    for i in range(len(s) // 2):
##        if s[i] != s[len(s) - i]:
##            return False
##    return True

##def is_palindrome(s):
##    for i in range(len(s) // 2 + 1):
##        if s[i] != s[len(s) - i - 1]:
##            return False
##    return True

##def is_palindrome(s):
##    for i in range(len(s) // 2):
##        if s[i] != s[len(s) - i - 1]:
##            return False
##    return True

##def is_palindrome(s):
##    j = len(s) - 1
##    for i in range(len(s) // 2):
##        if s[i] != s[j - i]:
##            return False
##    return True
##
##print(is_palindrome('racecar'))
##print(is_palindrome('nope'))

##def is_anagram(s1, s2):
##    L1 = list(s1)
##    L2 = list(s2)
##    L1.sort()
##    L2.sort()
##    return L1 == L2
##    d1 = {}
##    d2 = {}
##    for c in s1:
##        if c in d1:
##            d1[c] += 1
##        else:
##            d1[c] = 1
##    for c in s2:
##        if c in d2:
##            d2[c] += 1
##        else:
##            d2[c] = 1
##    return d1 == d2
##    for c in s1:
##        if s2.count(c) != s1.count(c):
##            return False
##    return True
    
        
##print(is_anagram('silent', 'listen'))
##print(is_anagram('breach', 'bear'))
##print(is_anagram('admirer', 'married'))
