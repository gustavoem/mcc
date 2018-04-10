# Nome: Gustavo Estrela de Matos
# NUSP: 8536051
# Q2 da prova 1

def coef (r):
    return r[0]


def intersec (r1, r2):
    return (r2[1] - r1[1]) / (r1[0] - r2[0])


def merge (V1, V2):
    n1 = len (V1)
    n2 = len (V2)
    
    i = 0
    j = 0
    v = []
    if (coef (V1[i]) < coef (V2[j])):
        v.append (V1[i])
        i += 1
    else:
        v.append (V2[j])
        j += 2

    while (i < n1 and j < n2):
        x1 = intersec (v[-1], V1[i])
        x2 = intersec (v[-1], V2[j])

        if (x1 <= x2):
            v.append (V1[i])
            i += 1
            if (coef (V1[i - 1]) >= coef (V2[j])):
                j += 1
        else:
            v.append (V2[j])
            j += 1
            if (coef (V2[j - 1]) >= coef (V1[i])):
                i += 1

    while (i < n1):
        v.append (V1[i])
        i += 1
    while (j < n2):
        v.append (V2[j])
        j += 1

    return v


def visibleR (L, p, r):
    if (p + 2 >= r):
        if r == p + 2 and coef (L[p]) == coef (L[p + 1]):
            if (L[p][1] > L[p + 1][1]):
                return L[p:p + 1]
            else:
                return L[p + 1:p + 2]
        else:
            return L[p:r]
    
    q = (p + r) // 2
    V1 = visibleR (L, p, q + 1)
    V2 = visibleR (L, q + 1, r)
    return merge (V1, V2)


def visible (L):
    L.sort (key=lambda x: x[0])
    return visibleR (L, 0, len (L))


# An example instance
# A line is represented by a tuple of size 2, where the first and second
# entry represent slope and y-intercept, respectivelly.
L = [(0, 54), (-1, 27), (-1, 42), (1, 95), (-2, 9), (2, 96)]
print (visible (L))
