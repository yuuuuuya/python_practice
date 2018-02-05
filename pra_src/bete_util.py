import numpy as np 
from scipy.stats import beta
from matplotlib.pyplot import hist, plot, show

'''
コメント！！
何をしている書く。英語で、（笑）
'''

def betaVar(alpha,Beta):
    denom=(alpha+Beta)**2*(alpha+Beta+1)
    numer=(alpha*Beta)
    value=numer/denom
    return value#outputしてください。

def betaM(alpha,Beta):
    value=alpha/(alpha+Beta)
    return value#outputしてください。



