# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your CSV data
df = pd.read_csv('toy_dataset.csv')

# Group the data
gen_med = df.groupby(['City', 'Gender'])['Income'].mean().reset_index(name='count')

# Create a Streamlit app
st.title("Average Income Per City by Gender")

# Select a gender to display (using a sidebar)
selected_gender = st.sidebar.selectbox("Select Gender", gen_med['Gender'].unique())

# Filter data for the selected gender
filtered_data = gen_med[gen_med['Gender'] == selected_gender]

# Create a bar plot for the selected gender
fig, ax = plt.subplots(figsize=(10, 5))
x_pos = np.arange(len(filtered_data))
tick_labels = filtered_data['City']

# Plot the data
ax.bar(x_pos, filtered_data['count'], width=0.4, label=selected_gender)
ax.set_xticks(x_pos)
ax.set_xticklabels(tick_labels, rotation=45, horizontalalignment='right')

# Customize the plot
ax.set_xlabel("City")
ax.set_ylabel("Average Income")
ax.set_title(f"Average Income for {selected_gender} in Each City")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Filter data for the other gender
other_gender = 'Female' if selected_gender == 'Male' else 'Male'
other_data = gen_med[gen_med['Gender'] == other_gender]

# Create a separate bar plot for the other gender
fig2, ax2 = plt.subplots(figsize=(10, 5))
x_pos2 = np.arange(len(other_data))

# Plot the data
ax2.bar(x_pos2, other_data['count'], width=0.4, label=other_gender, color='orange')
ax2.set_xticks(x_pos2)
ax2.set_xticklabels(other_data['City'], rotation=45, horizontalalignment='right')

# Customize the plot
ax2.set_xlabel("City")
ax2.set_ylabel("Average Income")
ax2.set_title(f"Average Income for {other_gender} in Each City")
ax2.legend()

fig = plt.figure()
plt.pie(gen_med['count'], labels = gen_med['City'])

# show plot
plt.show()

# Display the plot for the other gender in Streamlit
st.pyplot(fig2)

#comments
st.write("There are some findings and a brief analysis ")
st.write('1. The highest average income belongs to "Mountain View" and the lowest average income belongs to "Dallas"')
st.write('2.Gender does not affect the overall trend in average income ')
st.write('3.the average income of "Austin" is close to "Boston" ')



fig = plt.figure()
plt.pie(gen_med['count'], labels = gen_med['City'])

# show plot
plt.show()
