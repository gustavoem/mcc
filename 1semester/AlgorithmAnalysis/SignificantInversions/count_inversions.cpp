#include <iostream>
#include <stdio.h>

using namespace std;

void sort_combine (int * list, unsigned int p, unsigned int q, 
        unsigned int r)
{
    unsigned int i, j, k;
    unsigned int n = r - p;
    int * list_cpy = new int[n];

    for (i = p; i < r; i++)
        list_cpy[i - p] = list[i];

    i = p;
    j = q;
    k = p;
    while (k < r)
    {
        if (list_cpy[i - p] <= list_cpy[j - p])
            list[k++] = list_cpy[i++ - p];
        else
            list[k++] = list_cpy[j++ - p];
    }

    //while (i < q) 
        //list[k++] = list_cpy[i++ - p];
    //while (j < r)
        //list[k++] = list_cpy[j++ - p];

    delete[] list_cpy;
}

unsigned int count_combine (int * list, unsigned int p, unsigned int q,
        unsigned int r)
{
    unsigned int count, i, j;

    count = 0;
    i = p;
    j = q;
    while (i < q && j < r)
    {
        if (list[i] > 2 * list[j])
        {
            count += (q - i);
            j++;
        }
        else
            i++;
    }

    return count;
}

unsigned int count_n_sort (int * list, unsigned int p, unsigned int r) 
{
    unsigned int q, count;
    q = (p + r) / 2;

    if (p + 1 >= r)
        return 0;

    count = count_n_sort (list, p, q) + count_n_sort (list, q, r) + 
        count_combine (list, p, q, r);
    sort_combine (list, p, q, r);
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
