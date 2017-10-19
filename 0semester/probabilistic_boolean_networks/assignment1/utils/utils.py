import numpy as np

# Reads input and buffers it into a list
def buffered_input (my_buffer):
    if (len (my_buffer) == 0):
        line_str = input ()
        line_arr = line_str.split ()
        my_buffer.extend (line_arr)
    res = my_buffer.pop (0)
    return res


# Returns an array of the binary representation (with n or more digits)
# of an integer
def int_to_binary_array (n, x):
    b = np.zeros (n)
    i = n - 1
    while x > 0:
        digit = x % 2
        x = x // 2
        b[i] = digit
        i -= 1
    return b.astype (int)


# Returns a string representing the integer x with n or more characters
def int_to_binary_string (n, x):
    return "".join (int_to_binary_array (n, x).astype (str).tolist ())


# Prints a transition probability matrix in a latex array representation
def print_latex_representation (P, n):
    # Prints in latex table format
    for j in range (2 ** n):
        print ("& " + int_to_binary_string (n, j), end=" ")
    print ("\\\ ", end="")
    for i in range (2 ** n):
        print ("\n" + int_to_binary_string (n, i), end=" ")
        for j in range (2 ** n):
            if (P[i][j] < 1e-2):
                p_str = "{:.2e}".format (P[i][j])
            else:
                p_str = "{:.2}".format (P[i][j])
            print ("& " + p_str, end=" ")
        print ("\\\\", end="")
