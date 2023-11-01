import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 14, 8, 16, 12]

# Line Graph
plt.subplot(221)  # 2x2 grid, 1st subplot
plt.plot(x, y)
plt.title('Line Graph')

# Bar Graph
plt.subplot(222)  # 2x2 grid, 2nd subplot
plt.bar(x, y)
plt.title('Bar Graph')

# Scatter Plot
plt.subplot(223)  # 2x2 grid, 3rd subplot
plt.scatter(x, y)
plt.title('Scatter Plot')

# Pie Chart
plt.subplot(224)  # 2x2 grid, 4th subplot
labels = ['A', 'B', 'C', 'D', 'E']
plt.pie(y, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

plt.tight_layout()  # Ensure proper spacing between subplots
plt.show()
