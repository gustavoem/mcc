#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>



using namespace std;


// Swaps two points of index i and j on Px and Py.
void swap (float * Px, float * Py, unsigned int i, unsigned int j)
{
    float aux = Px[i];
    Px[i] = Px[j];
    Px[j] = aux;
}


// Quicksort partition.
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


// Quicksort. 
void quick_sort (float * Px, float * Py, unsigned int s, unsigned int e)
{
    if (e - s <= 1)
        return;

    unsigned int pivot;
    pivot = quick_sort_partition (Px, Py, s, e);
    quick_sort (Px, Py, s, pivot);
    quick_sort (Px, Py, pivot + 1, e);
}


// Euclidean distance.
float pair_dist (float * Px, float * Py, unsigned int i, unsigned int j)
{
    float dx = Px[i] - Px[j];
    float dy = Py[i] - Py[j];
    return sqrt (dx * dx + dy * dy);
}


// Sorts points according to Y coordinate. This function assumes that 
// Py[p .. q] and Py[q + 1 .. r - 1] are sorted, where q = (p + r) / 2.
void intercalate_on_y (float * Px, float * Py, unsigned int p, 
        unsigned int r)
{
    unsigned int i, j, q, k;
    float * Px_aux = new float[r - p];
    float * Py_aux = new float[r - p];
    
    i = p;
    q = (p + r) / 2;
    j = q + 1;
    k = 0;

    while (i <= q && j < r)
    {
        if (Py[i] < Py[j])
        {
            Px_aux[k] = Px[i];
            Py_aux[k] = Py[i];
            k++;
            i++;
        }
        else
        {
            Px_aux[k] = Px[j];
            Py_aux[k] = Py[j];
            k++;
            j++;
        }
    }

    while (i <= q)
    {
        Px_aux[k] = Px[i];
        Py_aux[k] = Py[i];
        k++;
        i++;
    }
    while (j < r)
    {
        Px_aux[k] = Px[j];
        Py_aux[k] = Py[j];
        k++;
        j++;
    }


    for (i = p; i < r;  i++)
    {
        Px[i] = Px_aux[i - p];
        Py[i] = Py_aux[i - p];
    }

    delete[] Px_aux;
    delete[] Py_aux;
}


unsigned int get_candidates (float * Px, unsigned int * candidates,
        float L, float d, unsigned int r, unsigned int p)
{
    unsigned int t = 0;

    for (unsigned int i = p; i < r; i++)
        if (abs (Px[i] - L) < d)
            candidates[t++] = i;

    return t;
}


// The combine part of Shamos and Hoey
float combine (float * Px, float * Py, unsigned int p, unsigned int r,
        float d, float L)
{
    unsigned int i, j, k, k2, t;
    float min_d;
    unsigned int * candidates;

    min_d = d;
    intercalate_on_y (Px, Py, p, r);
    candidates = new unsigned int[r - p];
    t = get_candidates (Px, candidates, L, d, r, p);
    
    for (k = 0; k < t; k++)
    {
        i = candidates[k];
        for (k2 = k + 1; k2 < k + 7 && k2 < t; k2++)
        {
            j = candidates[k2];
            float candidate_d = pair_dist (Px, Py, i, j);
            if (candidate_d < min_d)
            {
                min_d = candidate_d;
            }
            if (Py[j] - Py[i] > min_d)
                break;
        }
    }

    return min_d;
}   


// Shamos and Hoey algorithm
float closest_pair (float * Px, float * Py, unsigned int p, 
        unsigned int r)
{
    float d_l, d_r, d, L;
    unsigned int q = (p + r) / 2;

    if (r - p <= 2)
    {
        if (r == p + 1)
            return -1;
        else
        {
            return pair_dist (Px, Py, p, p + 1);
        }

    }

    L = Px[q];
    d_l = closest_pair (Px, Py, p, q + 1);
    d_r = closest_pair (Px, Py, q + 1, r);
    if (d_l != -1)
    {
        d = d_l;
        if (d_r != -1 && d_r < d_l)
            d = d_r;
    }
    else
        d = d_r;

    d = combine (Px, Py, p, r, d, L);
    return d; 
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

    cout << closest_pair (Px, Py, 0, n) << endl;

    delete[] Px;
    delete[] Py;
    return 0;
}
