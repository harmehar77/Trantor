import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Title and text
st.title('Simple Streamlit App')
st.write('This is a basic example of a Streamlit app.')

# Creating a DataFrame
data = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df = pd.read_csv('datasets/advertising.csv')

# Displaying the DataFrame
st.write('Here is a sample DataFrame:', df)

# Line chart
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# chart = sns.pairplot(df,hue='Clicked on Ad',palette='bwr')
sns.set_theme(style="darkgrid")
plt.figure(figsize=(10, 6))
sns.jointplot(x='Daily Time Spent on Site',y='Daily Internet Usage',data=df,color='red')

st.pyplot(plt)

# Slider widget
x = st.slider('Select a value for x', min_value=0, max_value=100, value=50)
st.write('The selected value is', x)

# Button widget
if st.button('Click me'):
    st.write('Button clicked!')
