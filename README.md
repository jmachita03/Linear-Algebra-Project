# Linear Algebra Library

## Supreme - Gina Bernardini, Kei Reily, Jordan Machita


## Introduction:

<p>We created a library called Linear based on simple computations required for Linear Algebra. We have created functions to add any two matrices, multiply any two matrices, or find the determinants of square matrices sizes 2X2 - 6X6. </p>
    


## Motivation:
    
    As the three of our group members are Mathematical Programming Majors, Linear Algebra is a course that we have to take for our degree. Each of the functions that we created are basic steps of larger scale problems included in the course. Having a program like this to quickly calculate some of the more time-consuming, tedious, and error producing aspects of our coursework, can help us as students to focus on the more conceptual side of the subject. 



## How to Use the Program:

    We created a library of functions, so in order to use them, our library would need to be imported (by typing: import Linear). In our test file, we imported the library we created and subsequently tested these functions with various matrices. A user would need to call the desired functions and enter their input. For our addition and multiplication functions, the user would input two matrices of any size that they would like to be added or multiplied. Our addition function will add the two given matrices and will return a matrix with equal dimensions to the matrices provided by the user. Our functions protect from the user trying to add two matrices of different sizes or multiply two matrices where the number of columns in the first matrix are not equal to the number of rows in the second. Multiplication of two matrices is not commutative, therefore, Matrix A X Matrix B is not equal to Matrix B X Matrix A. Because of this, when defining our multiplication function it is important to note that the order in which the user enters the matrices is critical. Our multiplication function will return a matrix with the dimensions equivalent to the number of rows of the first give matrix by the number of columns of the second given matrix. Our determinant functions are size specific, so in order for the user to utilize the function, they would need to specifically pick a function for their matrix. In these cases, the user will only enter one square matrix. Our functions protect the user from entering a matrix that is not square or does not have the dimensions specific to that function. The result of any determinant function will return an integer or float value.
    
    
    
    ### Our Library
    
    #### add()
        Adds any two matrices.
        
    #### multiply()
        Multiplies any two matrices.
    
    #### det2()
        Finds the determinant of a 2X2 matrix.
    
    #### det3()
        Finds the determinant of a 3X3 matrix.
        
    #### det4()
        Finds the determinant of a 4X4 matrix.
        
    #### det5()
        Finds the determinant of a 5X5 matrix.
    
    #### det6()
        Finds the determinant of a 6X6 matrix.
