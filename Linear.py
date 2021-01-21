# Final Library of all functions created for the project
import pandas as pd


def add(matrixa, matrixb):
    a = matrixa.shape
    b = matrixb.shape
    if a[0] == b[0] and a[1] == b[1] : #Ensures that matrics are of the same dimensions
        
        add = pd.DataFrame() # creates the matrix that will be the sum of the two given
        for column in matrixa: # goes through each column to add the values into the new matrix
            col = matrixa[column] + matrixb[column]
            add[column] = col
        return add
    else:
        print('These matrices are not the same size. You cannot add them.')

def multiply(a, b):
    if a.shape[1] != b.shape[0]: # makes sure that the matrices can be multiplied
        # for matrix multiplication, the number of columns in the first must equal the number of rows in the second
        print('These matrices cannot be multiplied because the number of columns of the first matrix is not equal to the number of rows of the second matrix.')
        return None
    count = 0
    alll = [] # this will become a list of the columns of the resulting multiplied matrix
    while count < b.shape[1]: # runs through each column of the second matrix
        col = list(b.iloc[:,count]) 
        dots = [] # creates a list of the values in a single column of the resulting marix
        count2 = 0
        while count2 < a.shape[0]: # runs through each row of the first matrix
            row = list(a.loc[count2])
            dot = 0
            count3 = 0
            while count3 < len(row):
                # multiplies each element of the row of the first matrix by the element in the column of the second with the same index and adds all the results
                dot += row[count3]*col[count3] # this is the dot product as described above 
                count3 += 1
            dots.append(dot) # appends each dot product to a list, which will become the columns of the result
            count2 += 1
        alll.append(dots) # appends a new list that is going to be a column
        count += 1
    ab = pd.DataFrame() # creates the resulting matrix
    i = 0
    col_count = list(b.columns) 
    while i < len(col_count):
        ab['Col ' + str(i+1)] = alll[i] # creates the correct number of columns and assigns each column the corresponding list of values from the list of lists
        i += 1
    return ab 

def determinant(mat):
    if mat.shape[0] != mat.shape[1]:
        print("Error: This is not a square matrix.")
        return None

    # calculation for 2x2 matrix
    if mat.shape == (2,2):
        r = mat.shape[0]
        a = mat.loc[r-2][r-2]
        b = mat.loc[r-2][r-1]
        c = mat.loc[r-1][r-2]
        d = mat.loc[r-1][r-1]
        return a*d - b*c
    
    cos = list(mat.loc[0]) # creates a list that is the first row of the given matrix
    cofs = []
    inc = 0
    for item in cos: # replicates cos to cofs with every other sign being opposite
        if inc % 2 == 0:
            cofs.append(item)
        if inc % 2 == 1:
            cofs.append(-item)
        inc += 1
        
    d = []
    count2 = 0
    for a in cofs:
        dets = []
        count = 0
        while count < mat.shape[0]: # gets the corresponding matrix to the element in cofs
            if count != count2:
                dets.append(list(mat.iloc[1:,count]))
            count += 1
        d.append(dets)
        count2 += 1
    d2 = []
    for item in d:
        m2 = pd.DataFrame()
        num = 0
        for col in item:
            name = 'Col' + str(num)
            m2[name] = item[num]
            num += 1
        if m2.shape[0] >= 2: # gets the determinant of each matrix corresponding to each cofactor
            d2.append(determinant(m2))
        else:
            print("Error.")
    final_det = 0
    count3 = 0
    for item in cofs: # multiplies each cofactor in cofs by the coressponding determinant and adds them all
        final_det += item*d2[count3]
        count3 += 1
    return final_det