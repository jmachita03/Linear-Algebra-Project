# Final Library of all functions created for the project
import pandas as pd

def det2(matrix):
    if matrix.shape == (2,2):
        a = matrix.loc[0][0]
        b = matrix.loc[0][1]
        c = matrix.loc[1][0]
        d = matrix.loc[1][1]
        return a*d - b*c
    else:
        print('Not a 2x2 matrix.')

def det3(mat):
    if mat.shape != (3,3):
        print('Not a 3x3 matrix.')
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
    d2 = []
    for item in d:
        m2 = pd.DataFrame()
        m2['Col1'] = item[0]
        m2['Col2'] = item[1]
        d2.append(det2(m2))
    final_det = 0
    count3 = 0
    for item in cofs:
        final_det += item*d2[count3]
        count3 += 1
    return final_det

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