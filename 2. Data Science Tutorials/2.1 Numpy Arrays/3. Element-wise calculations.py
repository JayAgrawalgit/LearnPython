# Now we can perform element-wise calculations on height and weight. For example, you could take all 6 of the height and
# weight observations above, and calculate the BMI for each observation with a single equation. These operations are
# very fast and computationally efficient. They are particularly helpful when you have 1000s of observations in your data.

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

