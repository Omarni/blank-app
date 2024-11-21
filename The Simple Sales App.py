import streamlit as st
import pandas as pd

st.title("The Sales App")
# Step 1: Define the data
data = pd.DataFrame({
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Electronics": [500, 700, 800, 900, 1000],
    "Clothing": [300, 400, 500, 600, 700],
    "Groceries": [200, 300, 400, 500, 600]
})

# Step 2: Creating User inputs
department = st.multiselect("Choose the departments you'd like to see:", ["Electronics", "Clothing", "Groceries"])
chart_type = st.selectbox("Choose your chart type:", ["Bar Chart", "Line Chart"])
pct_adjust = st.slider("Choose your sales percent adjustment:", max_value=100, min_value=0, value=0)

# Step 3: Filtering the data
if department:  # Check if at least one department is selected
    filtered_data = data[["Day"] + department].set_index("Day")  # Include only selected departments

    # Step 4: Apply percentage adjustment
    if pct_adjust > 0:
        for dept in department:
            filtered_data[dept] = filtered_data[dept] * (1 + pct_adjust / 100)

    # Step 5: Display the chart
    if chart_type == "Bar Chart":
        st.bar_chart(filtered_data)
    elif chart_type == "Line Chart":
        st.line_chart(filtered_data)
else:
    st.write("Please select at least one department to view the data.")

