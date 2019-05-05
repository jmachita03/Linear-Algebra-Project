# Final Library of all functions created for the project
import pandas as pd

def det2(matrix):
    if matrix.shape == (2,2):
        r = matrix.shape[0]
        a = matrix.loc[r-2][r-2]
        b = matrix.loc[r-2][r-1]
        c = matrix.loc[r-1][r-2]
        d = matrix.loc[r-1][r-1]
        return a*d - b*c
    else:
        print('Not a 2x2 matrix.')

def det3(matrix):
    if matrix.shape == (3,3):
        a = matrix.loc[0][0]
        b = matrix.loc[0][1]
        c = matrix.loc[0][2]
        d = matrix.loc[1][0]
        e = matrix.loc[1][1]
        f = matrix.loc[1][2]
        g = matrix.loc[2][0]
        h = matrix.loc[2][1]
        i = matrix.loc[2][2]
        pt1 = a*(e*i-f*h)
        pt2 = b*(d*i-f*g)
        pt3 = c*(d*h-e*g)
        return pt1 - pt2 + pt3
    else:
        print('Not a 3x3 matrix.')


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
    for a in cofs:
        dets = []
        count = 0
        while count < mat.shape[0]:
            if count != cofs.index(a):
                dets.append(list(mat.iloc[1:,count]))
            count += 1
        d.append(dets)
    d3 = []
    for item in d:
        m2 = pd.DataFrame()
        m2['Col1'] = item[0]
        m2['Col2'] = item[1]
        m2['Col3'] = item[2]
        d3.append(det3(m2))
    final_det = 0
    for item in cofs:
        final_det += item*d3[cofs.index(item)]
    return final_det