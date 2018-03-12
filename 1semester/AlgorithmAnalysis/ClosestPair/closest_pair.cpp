#include <iostream>
#include <stdio.h>

using namespace std;

void swap (float * Px, float * Py, unsigned int i, unsigned int j)
{
    float aux = Px[i];
    Px[i] = Px[j];
    Px[j] = aux;
}

unsigned int quick_sort_partition (float * Px, float * Py, unsigned int s, 
    unsigned int e)
{
    unsigned int i, pivot;
    pivot = e - 1;
    i = s;

    while (i != pivot)
    {
        if (Px[i] > Px[pivot])
        {
            swap (Px, Py, pivot, pivot - 1);
            pivot--;
            swap (Px, Py, pivot + 1, i);
        }
        else
            i++;
    }
    return pivot;
}

void quick_sort (float * Px, float * Py, unsigned int s, unsigned int e)
{
    if (e - s <= 1)
        return;

    unsigned int pivot;
    pivot = quick_sort_partition (Px, Py, s, e);
    quick_sort (Px, Py, s, pivot);
    quick_sort (Px, Py, pivot + 1, e);
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

    quick_sort (Px, Py, 0, n);

    cout << "Px = " << endl;
    for (unsigned int i = 0; i < n; i++)
        cout << Px[i] << " " << endl;
    cout << endl << "Py" << endl;
    for (unsigned int i = 0; i < n; i++)
        cout << Py[i] << " " << endl;
    

    delete[] Px;
    delete[] Py;
    return 0;
}
