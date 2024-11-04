import streamlit as st
import numpy as np
import pandas as pd

data_points = st.slider("Select number of data points", 10, 100)
st.divider()
data = pd.DataFrame(np.random.randn(data_points, 1), columns=["Value"])
st.line_chart(data)
