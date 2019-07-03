/*
    Adapted from demo/cvode/serial/cdenx.c
    by Scott Cohen, Alan Hindmarsh, and Radu Serban.    

***********************************************************************/


#include <stdlib.h>
#include <math.h>
#include <cvode/cvode.h>
#include <nvector/nvector_serial.h>
#include <sundials/sundials_dense.h>
#include <sundials/sundials_types.h>
#include <sunmatrix/sunmatrix_dense.h> 
#include <sunlinsol/sunlinsol_dense.h> 


static int f(realtype t, N_Vector y, N_Vector ydot, void *f_data) 
{
    // NV_Ith_S is a macro that allows us to access the components of 
    // data using standard indexing (starting from 0).
    float *param_data = f_data;
    NV_Ith_S(ydot,0) = NV_Ith_S(y,0) * param_data[1];
    NV_Ith_S(ydot,1) = NV_Ith_S(y,1) * param_data[2];
    return 0;
}


int main(int argc, char **argv) 
{
    // 1. Initialize environment
    // 2. Set problems dimensions
    int N = 2;
    realtype T0 = 0;
    realtype Tfinal = 1;
    realtype theta0 = 1;
    realtype reltol = 1e-6;
    realtype atol = 1e-6;
    realtype t;
    int flag, k;

    N_Vector y = NULL;
    N_Vector yout = NULL;
    void *cvode_mem = NULL;
    SUNMatrix J;
    SUNLinearSolver LS;
    
    // 3. Set vector of initial values
    y = N_VNew_Serial(2);
    yout = N_VNew_Serial(2);
    NV_Ith_S(y, 0) = theta0;
    NV_Ith_S(y, 1) = 1;
    float *my_data;
    my_data = malloc (3 * sizeof (float));
    my_data[0] = 2;
    my_data[1] = 1.0;
    my_data[2] = 2.0;


    // 4. Create CVODE object
    cvode_mem = CVodeCreate(CV_BDF);
    if (cvode_mem == 0)
    {
        fprintf (stderr, "Error in CVodeMalloc: could not allocate\n");
        return -1;
    }
    

    // 5. Initialize CVODE solver
    flag = CVodeInit(cvode_mem, f, T0, y);
    if (flag < 0) 
    {
        fprintf(stderr, "Error in CVodeInit: %d\n", flag);
        return -1;
    }


    // 6. Specify integration tolerances
    flag = CVodeSStolerances(cvode_mem, reltol, atol);
    if (flag < 0)
    {
        fprintf(stderr, "Error in CVodeSStolerances: %d\n", flag);
    }


    // 7. Create matrix object
    J = SUNDenseMatrix(N, N);
    if (J == NULL)
    {
        fprintf(stderr, "Error in SUNDenseMatrix.\n");
        return -1;
    }
    
    // 8. Create linear solver object
    LS = SUNLinSol_Dense(y, J);
    if (LS == NULL)
    {
        fprintf(stderr, "Error in SUNLinSol_Dense.\n");
        return -1;
    }
    
    
    // 9. Set linear solver optioinal inputs
    
    // 10. Attach linear solver module
    flag = CVodeSetLinearSolver(cvode_mem, LS, J);
    if (flag < 0)
    {
        fprintf(stderr, "Error in SUNLinSol_Dense.\n");
        return -1;
    }
    
    // 11. Set optional inputs
    flag = CVodeSetUserData(cvode_mem, my_data);
    if (flag < 0)
    {
        fprintf(stderr, "Error in CVodeSetUserData.\n");
        return -1;
    }

    // In loop, call CVode, print results and test for error.
    for (k = 1; k < 10; ++k) {
        realtype tout = k * Tfinal / N;
        flag = CVode (cvode_mem, tout, yout, &t, CV_NORMAL);
        if (flag) {
            fprintf (stderr, "Error in CVode: %d\n", flag);
            return -1;
        }
        printf("%g %.16e %.16e\n", t, NV_Ith_S(yout, 0), 
                NV_Ith_S(yout, 1));
        printf("exp(%.3f) = %.3f\n", t, exp (t));
        printf("exp(%.3f) = %.3f\n\n", 2 * t, exp (2 * t));
    }

    // Free all memory used
    N_VDestroy_Serial(y);
    N_VDestroy_Serial(yout);
    CVodeFree(&cvode_mem);
    SUNLinSolFree(LS);
    SUNMatDestroy(J);
    return 0;
}
