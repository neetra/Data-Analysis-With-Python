import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    array = np.array(list).reshape(3,3)
    calculations = {
        'mean': [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array).item()],
        'variance': [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array).item()],
        'standard deviation': [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array).item()],
        'max': [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array).item()],
        'min': [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array).item()],
        'sum': [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array).item()]
    }

    return calculations

calculate([0,1,2,3,4,5,6,7,8])