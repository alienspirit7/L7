# @title
import numpy as np
import matplotlib.pyplot as plt

# Define the sample size parameter
sample_size_n = 1000

# Create n two-dimensional points
# Generate x-coordinates randomly between 0 and 1
x_coords = np.random.rand(sample_size_n)
# Generate y-coordinates based on the formula y = 0.2x + 0.3 + random number between -0.2 and 0.2
random_noise = -0.2 + (0.2+0.2) * np.random.rand(sample_size_n)
y_coords = 0.2 * x_coords + 0.3 + random_noise

points = np.column_stack((x_coords, y_coords))


# Plot the points
plt.figure(figsize=(6, 6))
plt.scatter(points[:, 0], points[:, 1], s=5)
plt.title(f'Scatter Plot of {sample_size_n} Random Points')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.xlim(0, 1)
plt.ylim(0, 1) # Adjust the y-limit back to 0-1
plt.grid(True)
plt.show()

# @title
# Generate n pairs of points (a, b)
n_pairs = 10000
ab_pairs = np.random.rand(n_pairs, 2)

# Calculate and store average errors for each pair
avg_errors = []
for a, b in ab_pairs:
    # Calculate errors for each of the 1000 points
    errors = (points[:, 1] - a * points[:, 0] - b)**2
    # Calculate the average error for the current pair (a, b)
    avg_error = np.mean(errors)
    avg_errors.append(avg_error)

# Convert avg_errors to a NumPy array
avg_errors = np.array(avg_errors)

# Print the average errors
# print("Average errors for each of the 100 pairs (a, b):")
# for i, avg_err in enumerate(avg_errors):
#     print(f"Pair {i+1}: {avg_err:.4f}")

# Find the index of the minimum average error
min_error_index = np.argmin(avg_errors)

# Get the pair (a, b) with the minimum average error
best_ab_pair = ab_pairs[min_error_index]
best_a, best_b = best_ab_pair

print(f"\nPair (a, b) with minimum average error: a = {best_a:.4f}, b = {best_b:.4f}")
print(f"Minimum average error: {avg_errors[min_error_index]:.4f}")

# Plot the points and the line y = ax + b
plt.figure(figsize=(6, 6))
plt.scatter(points[:, 0], points[:, 1], s=5, label='Random Points')

# Generate x values for the line
x_values = np.linspace(0, 1, 100)
# Calculate corresponding y values using the best (a, b) pair
y_values = best_a * x_values + best_b
plt.plot(x_values, y_values, color='red', label=f'y = {best_a:.4f}x + {best_b:.4f}')

plt.title('Scatter Plot of Points and Best Fit Line')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True)
plt.legend()
plt.show()

# @title
# Get the indices of the 10 lowest average errors
min_error_indices = np.argsort(avg_errors)[:10]

# Get the 10 pairs (a, b) with the lowest average errors
best_10_ab_pairs = ab_pairs[min_error_indices]

# Find the index of the minimum error within the top 10 average errors
index_of_min_error_in_top_10 = np.argmin(avg_errors[min_error_indices])


# Plot the points and the lines for the best 10 pairs
plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1], s=5, label='Random Points')

x_values = np.linspace(0, 1, 100)

for i, (a, b) in enumerate(best_10_ab_pairs):
    y_values = a * x_values + b
    # Check if the current line is the one with the overall minimal error
    if i == index_of_min_error_in_top_10:
        plt.plot(x_values, y_values, color='red', linewidth=2, label=f'Best Fit Line (Error: {avg_errors[min_error_indices[i]]:.4f})') # Make the minimal error line red and bolder
    else:
        plt.plot(x_values, y_values, linestyle='--', label=f'Line {i+1} (Error: {avg_errors[min_error_indices[i]]:.4f})')


plt.title('Scatter Plot of Points and 10 Best Fit Lines')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
