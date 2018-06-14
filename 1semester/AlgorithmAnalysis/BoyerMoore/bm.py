from string import printable

def v2_calc (p):
    ''' For each i in 1..m, calculates the greatest j such that 
        P[i..m] is suffix of P[1..j] or P[1..j] is suffix of P[i..m].'''
    # We say that j is good to i if P[1..j] is suffix of P[i..m] or 
    # P[i..m] is suffix of P[1..j].
    # Before reading this function, try to prove that if k is not good
    # to h, then k is not good for any other l < h.
    m = len (p) - 1
    h = m
    k = m - 1
    v2 = [0] * (m + 1)
    while (h >= 1 and k >= 1):
        i = m
        j = k
        while (i >= h and j >= 1):
            if (p[i] == p[j]):
                i -= 1
                j -= 1
            else:
                i = m
                k -= 1
                j = k
        v2[h] = k
        h -= 1
    while (h >= 1):
        v2[h] = k
        h -= 1
    return v2

def v1_calc (p):
    ''' For each character in our alphabet, calculates the last index
        in which this character is seen on the pattern. If the character
        is not on the pattern, we consider the index as 0. '''
    v1 = [0] * 256
    i = 1
    for c in list (p[1:]):
        v1[ord (c)] = i
        i += 1
    return v1

def boyermoore (p, t):
    m = len (p) - 1
    n = len (t) - 1
    v1 = v1_calc (p)
    occurs = 0
    k = m
    while (k <= n):
        i = m
        j = k
        print ("matching " +  "".join (t[j-m + 1:j+1]) + " with " + p[1:])
        while (i >= 1 and p[i] == t[j]):
            i -= 1
            j -= 1
        print ("saiu com i = " + str (i))
        if (i < 1):
            occurs += 1
        if (k >= n):
            return occurs
        print ("Next step based on " + t[k + 1]) 
        print ("Skept " + str (m - v1[ord (t[k + 1])] + 1))
        k += m - v1[ord (t[k + 1])] + 1  
    return occurs


p = '*CAABAA'
t = '*AsscCAABACAABAACAABAAAccCaaAAsdfBAAaACCAABAACACAABAA'
print (t)
print (boyermoore(p, t))
