#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>



using namespace std;

float median_base (float * A, float * B, unsigned int pa, unsigned int qa,
        unsigned int pb, unsigned int qb)
{
    float median;
    if (qa - pa == 2)
    {
        float * sorted = new float[4];
        unsigned int t = 0;

        while (pa < qa && pb < qb)
        {
            if (A[pa] < B[pb])
                sorted[t++] = A[pa++];
            else
                sorted[t++] = B[pb++];
        }
        while (pa < qa)
            sorted[t++] = A[pa++];
        while (pb < qb)
            sorted[t++] = A[pb++];
        median = (sorted[2] + sorted[1]) / 2.0;
        delete[] sorted;
    }
    else 
        median = (A[pa] + B[pb]) / 2.0;

    return median;
}

float median (float * A, float * B, unsigned int pa, unsigned int qa, 
        unsigned int pb, unsigned int qb)
{
    float mA, mB;
    unsigned int mA_idx, mB_idx;

    
    if (pa + 2 >= qa)
        return median_base (A, B, pa, qa, pb, qb);
    
    mA_idx = (pa + qa) / 2;
    mB_idx = (pb + qb) / 2;

    // Median for even sized A and B
    if ((qa - pa) % 2 == 0) 
    {
        mA = (A[mA_idx] + A[mA_idx - 1]) / 2;
        mB = (B[mB_idx] + A[mB_idx - 1]) / 2;
    }
    // Median for odd sized A and B
    else
    {
        mA = A[mA_idx];
        mB = B[mA_idx];
    }

    if (mA == mB)
        return mA;
    if (mA < mB)
    {
        if ((qa - pa) % 2 == 0)
            return median (A, B, mA_idx - 1, qa, pb, mB_idx + 1);
        else
            return median (A, B, mA_idx, qa, pb, mB_idx + 1);
    }
    else
    {
        if ((qa - pa) % 2 == 0)
            return median (A, B, pa, mA_idx + 1, mB_idx - 1, qb);
        else
            return median (A, B, pa, mA_idx + 1, mB_idx, qb);
    }
}


int main ()
{
    unsigned int n;
    float * A, * B;

    cin >> n;
    A = new float[n];
    B = new float[n];

    for (unsigned int i = 0; i < n; i++)
        cin >> A[i];
    for (unsigned int i = 0; i < n; i++)
        cin >> B[i];
    cout << median (A, B, 0, n, 0, n) << endl;

    delete[] A;
    delete[] B;
    return 0;
}
