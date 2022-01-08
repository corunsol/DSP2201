#!/usr/bin/env python
# coding: utf-8

# # sklearn.naive_bayes.GaussianNB

# ## Gaussian Naive Bayes (GaussianNB)
# 
# Can perform online updates to model parameters via partial_fit. For details on algorithm used to update feature means and variance online, see Stanford CS tech report STAN-CS-79-773 by Chan, Golub, and LeVeque:
# 
# http://i.stanford.edu/pub/cstr/reports/cs/tr/79/773/CS-TR-79-773.pdf
# 
# Read more in the User Guide.
# 
# ### Parameters
# ##### priorsarray-like of shape (n_classes,)
# * Prior probabilities of the classes. If specified the priors are not adjusted according to the data.
# 
# ##### var_smoothingfloat, default=1e-9
# * Portion of the largest variance of all features that is added to variances for calculation stability.
# 
# * New in version 0.20.
# 
# ### Attributes
# ##### class_count_ndarray of shape (n_classes,)
# * number of training samples observed in each class.
# 
# ##### class_prior_ndarray of shape (n_classes,)
# * probability of each class.
# 
# ##### classes_ndarray of shape (n_classes,)
# * class labels known to the classifier
# 
# ##### epsilon_float
# * absolute additive value to variances
# 
# ##### sigma_ndarray of shape (n_classes, n_features)
# * variance of each feature per class
# 
# ##### theta_ndarray of shape (n_classes, n_features)
# * mean of each feature per class


import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
# define the classifier
clf = GaussianNB()
# Fit the data into the model
clf.fit(X, Y)

# predict (classify new data point)
print("Full fit: ", clf.predict([[-0.8, -1]]))

# partial fit
clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))

# predict per partial_fit model
print("Partial fit: ", clf_pf.predict([[-0.8, -1]]))

