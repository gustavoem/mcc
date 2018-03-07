#include <iostream>
#include <stdio.h>

using namespace std;

unsigned int merge_n_count (int * list, unsigned int p, unsigned int q,
        unsigned int r)
{
    unsigned int count, i, j, k;
    int n = r - p;
    int * list_cpy = new int[n];
    
    for (i = p; i < r; i++)
        list_cpy[i - p] = list[i];
    
    count = 0;
    i = p;
    j = q;
    k = p;
    while (i < q && j < r)
    {
        if (list_cpy[i - p] <= list_cpy[j - p])
            list[k++] = list_cpy[i++ - p];
        else
        {
            list[k++] = list_cpy[j++ - p];
            count += q - i;
        }
    }

    while (i < q) 
        list[k++] = list_cpy[i++ - p];
    while (j < r)
        list[k++] = list_cpy[j++ - p];
    
    delete[] list_cpy;
    return count;
}

unsigned int count_n_sort (int * list, unsigned int p, unsigned int r) 
{
    unsigned int q, count;
    q = (p + r) / 2;

    if (p + 1 >= r)
        return 0;

    count = count_n_sort (list, p, q) + count_n_sort (list, q, r) +
        merge_n_count (list, p, q, r);

    return count;
}


int main ()
{
    unsigned int n, inversions;
    int * list;

    cin >> n;
    list = new int[n];
    for (unsigned int i = 0; i < n; i++)
        cin >> list[i];
    
    inversions = count_n_sort (list, 0, n);
    cout << "Number of inversions: " << inversions << endl;
    
    delete[] list;
    return 0;
}
