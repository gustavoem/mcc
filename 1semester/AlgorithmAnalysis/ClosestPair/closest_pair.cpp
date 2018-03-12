#include <iostream>
#include <stdio.h>

using namespace std;

void swap (float * Px, float * Py, unsigned int i, unsigned int j)
{
    float aux = Px[i];
    Px[i] = Px[j];
    Px[j] = aux;
}

void quick_sort_partition (float * Px, float * Py, unsigned int s, 
    unsigned int e)
{
    unsigned int i, pivot;
    pivot = e - 1;
    i = e;

    while (i != pivot)
    {
        if (Px[i] > Px[pivot])
        {
            swap (Px, Py, pivot, pivot--);
            swap (Px, Py, pivot + 1, i);
        }
        else
            i++;
    }
}

void quick_sort (float * Px, float * Py, unsigned int s, unsigned int e)
{
    quick_sort_partitoin (Px, Py, s, e);
}

int main ()
{
    unsigned int n;
    float * Px, *Py;

    cin >> n;
    Px = new float[n];
    Py = new float[n];
    for (unsigned int i = 0; i < n; i++)
        cin >> Px[i];
    for (unsigned int i = 0; i < n; i++)
        cin >> Py[i];

    delete[] Px;
    delete[] Py;
    return 0;
}
