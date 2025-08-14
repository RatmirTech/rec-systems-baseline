"""
cb_baseline.py — content-based recommendations baseline
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity
