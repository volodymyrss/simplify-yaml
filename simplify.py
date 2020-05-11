import numpy as np

def simplify(x):
    if isinstance(x, np.ndarray):
        return simplify(list(x))
    
    #if isinstance(x, np.core.multiarray.scalar):
    #    return float(x)
    
    if isinstance(x, list):
        return [simplify(a) for a in x]
    
    if isinstance(x, tuple):
        return tuple([simplify(a) for a in x])


    if isinstance(x, dict):
        return {simplify(a):simplify(b) for a,b in x.items()}

    try:
        return float(x)
    except:
        return x
