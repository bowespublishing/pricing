import streamlit as st

# Streamlit app title
st.title("Price Variation Calculator")

# User input for the initial price
initial_price = st.number_input("Enter the current price:", value=5.37, format="%.2f")

# User input for the target price
target_price = st.number_input("Enter the target price:", value=5.37, format="%.2f")

# Define a fixed tolerance value of 0.005 around the target price
tolerance_value = 0.005
tolerance_range = (target_price - tolerance_value, target_price + tolerance_value)

# Display tolerance range
st.write(f"Tolerance range: {tolerance_range[0]:.4f} - {tolerance_range[1]:.4f}")

# Range of possible increases and decreases
increase_range = range(-20, 41)  # Percentage increase from -20% to 40%
decrease_range = range(1, 51)  # Percentage decrease from 1% to 50%

# List to store valid results within the acceptable tolerance range
valid_combinations = []

# Check all combinations of percentage increases and decreases
for increase in increase_range:
    for decrease in decrease_range:
        # Apply the increase first
        increased_price = initial_price * (1 + increase / 100)
        # Apply the decrease
        final_price = increased_price * (1 - decrease / 100)
        # Check if the final price falls within the tolerance range
        if tolerance_range[0] <= final_price <= tolerance_range[1]:
            valid_combinations.append((increase, decrease, final_price))

# Display results
if valid_combinations:
    st.write("Valid Combinations:")
    for combo in valid_combinations:
        increase, decrease, final_price = combo
        st.write(f"Increase by {increase}% and then decrease by {decrease}% → Final price: £{final_price:.6f}")
else:
    st.write("No valid combinations found within the tolerance range.")
