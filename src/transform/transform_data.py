import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class NumericalSex(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.variable = "sex"
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X.copy()
        X[self.variable] = np.where(X[self.variable]=="female", 0, 1)
        return X

class NumericalFloat(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for var in self.variables:
            X[var] = X[var].astype("float")
        return X

class NumericalImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
    
    def fit(self, X, y=None):
        self.median_dict = {}
        for var in self.variables:
            self.median_dict[var] = X[var].median()
        return self
        

    def transform(self, X, y=None):
        X = X.copy()
        for var in self.variables:
            X[var] = X[var].fillna(self.median_dict[var])
        return X

class CategoricalImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X.copy()
        for var in self.variables:
            X[var] = X[var].fillna(method='ffill').fillna(method='bfill')
        return X

class NumericalEmbarked(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.variable = "embarked"
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X[self.variable] = X[self.variable].replace("S", 1)
        X[self.variable] = X[self.variable].replace("C", 2)
        X[self.variable] = X[self.variable].replace("Q", 3)
        return X

class NumericalRound(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for var in self.variables:
            X[var] = round(X[var],0)
        return X

class NumericalInt(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for var in self.variables:
            X[var] = X[var].astype("int64")
        return X
