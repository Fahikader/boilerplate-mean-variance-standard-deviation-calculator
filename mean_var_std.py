import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Conversion of list into 3D numpy array 

    matrix = np.array(list).reshape(3,3)

    # MEAN,VARIANCE,STANDARD DEVIATION,MAXIMUM,MINIMUM,SUM for each column
    mean_column = np.mean(matrix, axis = 0)
    variance_column = np.var(matrix, axis=0)
    std_column = np.std(matrix, axis = 0)
    max_column = np.max(matrix, axis = 0)
    min_column = np.min(matrix, axis = 0)
    sum_column = np.sum(matrix , axis=0)

    # MEAN,VARIANCE,STANDARD DEVIATION,MAXIMUM,MINIMUM,SUM for each row
    mean_row = np.mean(matrix, axis = 1)
    variance_row = np.var(matrix, axis=1)
    std_row = np.std(matrix, axis = 1)
    max_row = np.max(matrix, axis = 1)
    min_row = np.min(matrix, axis = 1)
    sum_row = np.sum(matrix , axis=1)

    # MEAN,VARIANCE,STANDARD DEVIATION,MAXIMUM,MINIMUM,SUM flattened 
    mean_flattened = np.mean(matrix)
    variance_flattened = np.var(matrix)
    std_flattened = np.std(matrix)
    max_flattened = np.max(matrix)
    min_flattened = np.min(matrix)
    sum_flattened = np.sum(matrix)

    # Converting list into dictionary

    calculations = {
    'mean': [mean_column.tolist(), mean_row.tolist(), mean_flattened],
    'variance': [variance_column.tolist(), variance_row.tolist(), variance_flattened],
    'standard deviation': [std_column.tolist(), std_row.tolist(), std_flattened],
    'max': [max_column.tolist(), max_row.tolist(), max_flattened],
    'min': [min_column.tolist(), min_row.tolist(), min_flattened],
    'sum': [sum_column.tolist(), sum_row.tolist(), sum_flattened]
    }





    return calculations