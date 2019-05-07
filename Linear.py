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

def det2(matrix):
    if matrix.shape == (2,2): # ensures that this is a 2x2 square matrix
        # assigns each position in the matrix to a variable
        a = matrix.loc[0][0] 
        b = matrix.loc[0][1]
        c = matrix.loc[1][0]
        d = matrix.loc[1][1]
        return a*d - b*c # calculates the determinant based on the formula for the determinant of a 2x2 matrix
    else:
        print('Not a 2x2 matrix.')

def det3(mat):
    if mat.shape != (3,3): # ensures that the matrix given is a 3x3
        print('Not a 3x3 matrix.')
        return None
    cos = list(mat.loc[0]) # creates a list that is the first row of the given matrix
    cofs = []
    inc = 0
    for item in cos: # creates a list that is cos but with every other term being the opposite sign of the original
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
        m2['Col1'] = item[0]
        m2['Col2'] = item[1]
        d2.append(det2(m2)) # gets the determinant of each matrix corresponding to each cofactor
    final_det = 0
    count3 = 0
    for item in cofs: # multiplies each cofactor in cofs by the coressponding determinant and adds them all
        final_det += item*d2[count3]
        count3 += 1
    return final_det 

# Note: The logic for the determinant of a 3x3 is the same as 4x4, 5x5, etc.
# When calculating a 3x3, the determinants of three 2x2s must be calculated using the det2 function
# When calculating a 4x4, the determinants of four 3x3s must be calculated using the det3 function
# And so on
# Thus, the det6 function uses the det5 function 5 times, which uses the det4 function 4 times, which uses the det3 program 3 times, which uses the det2 program 2 times
# After a 3x3, the code needs only minor additons to get to det4, so all of the logic is the same and the code is scalable


def det4(mat):
    if mat.shape != (4, 4):
        print('Not a 4x4 matrix.')
        return None
    cos = list(mat.loc[0])
    cofs = []
    inc = 0
    for item in cos:
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
        while count < mat.shape[0]:
            if count != count2:
                dets.append(list(mat.iloc[1:,count]))
            count += 1
        d.append(dets)
        count2 += 1
    d3 = []
    for item in d:
        m2 = pd.DataFrame()
        m2['Col1'] = item[0]
        m2['Col2'] = item[1]
        m2['Col3'] = item[2]
        d3.append(det3(m2))
    final_det = 0
    count3 = 0
    for item in cofs:
        final_det += item*d3[count3]
        count3 += 1
    return final_det


def det5(mat):
    if mat.shape != (5, 5):
        print('Not a 5x5 matrix.')
        return None
    cos = list(mat.loc[0])
    cofs = []
    inc = 0
    for item in cos:
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
        while count < mat.shape[0]:
            if count != count2:
                dets.append(list(mat.iloc[1:,count]))
            count += 1
        d.append(dets)
        count2 += 1
    d4 = []
    for item in d:
        m2 = pd.DataFrame()
        m2['Col1'] = item[0]
        m2['Col2'] = item[1]
        m2['Col3'] = item[2]
        m2['Col4'] = item[3]
        d4.append(det4(m2))
    final_det = 0
    count3 = 0
    for item in cofs:
        final_det += item*d4[count3]
        count3 += 1
    return final_det

def det6(mat):
    if mat.shape != (6, 6):
        print('Not a 6x6 matrix.')
        return None
    cos = list(mat.loc[0])
    cofs = []
    inc = 0
    for item in cos:
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
        while count < mat.shape[0]:
            if count != count2:
                dets.append(list(mat.iloc[1:,count]))
            count += 1
        d.append(dets)
        count2 += 1
    d5 = []
    for item in d:
        m2 = pd.DataFrame()
        m2['Col1'] = item[0]
        m2['Col2'] = item[1]
        m2['Col3'] = item[2]
        m2['Col4'] = item[3]
        m2['Col5'] = item[4]
        d5.append(det5(m2))
    final_det = 0
    count3 = 0
    for item in cofs:
        final_det += item*d5[count3]
        count3 += 1
    return final_det