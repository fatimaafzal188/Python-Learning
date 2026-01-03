
# Plotting multiples of 2 up to 20

import matplotlib.pyplot as plt

# Sample data: multiples of 2 up to 20
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Create a line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Multiples of 2')
plt.title('Line Plot of Multiples of 2 up to 20')

# Display the plot
plt.show()

