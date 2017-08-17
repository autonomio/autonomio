import numpy as np
import pandas as pd


def check(Y, rounded, scores):

    df1 = pd.DataFrame(rounded)
    df2 = pd.DataFrame(Y)

    # 0 or 1 if prediction mathes the output
    f = df1 == df2
    f.astype(int)
    f = np.array(f)

    x = 0
    a = len(f)

    for i in range(a):
        if f[i] == 1:
            x += 1.0

    p = x / a

    print ("keras accuracy: %.2f%%" % (scores[1]*100))
    print ("double check: %.2f%%" % (p*100))

    return
