import pandas as pd
from scipy import stats
from itertools import combinations

def testMannWhitney(data:pd.DataFrame, group:str, depvar:str, **kwargs):
    l = []
    for (g1, g2) in combinations(data[group].unique(), 2):
        d1 = data[data[group] == g1][depvar]
        d2 = data[data[group] == g2][depvar]
        _stat, _pv = stats.mannwhitneyu(d1, d2, **kwargs)
        l.append({
            f"{group}_1": g1,
            f"{group}_2": g2,
            "U-Statistic": _stat,
            "P-Value": _pv
        })
    result = pd.DataFrame(l)
    return result

def testFlignerKilleen(data:pd.DataFrame, group:str, depvar:str, **kwargs):
    l = []
    for (g1, g2) in combinations(data[group].unique(), 2):
        d1 = data[data[group] == g1][depvar]
        d2 = data[data[group] == g2][depvar]
        _stat, _pv = stats.fligner(d1, d2, **kwargs)
        l.append({
            f"{group}_1": g1,
            f"{group}_2": g2,
            "F-Statistic": _stat,
            "P-Value": _pv
        })
    result = pd.DataFrame(l)
    return result