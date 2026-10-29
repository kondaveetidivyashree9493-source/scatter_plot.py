
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with 5 columns and 10 rows
data = {
    "Name": ["A", "B", "C", "D", "E",
             "F", "G", "H", "I", "J"],
    "Age": [18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    "Marks": [65, 70, 75, 80, 85, 60, 72, 88, 90, 78],
    "Hours": [2, 3, 4, 5, 6, 2, 4, 7, 8, 5],
    "Attendance": [80, 85, 90, 92, 95, 75, 88, 96, 98, 89]
}

df = pd.DataFrame(data)

# Create scatter plot
plt.scatter(df["Hours"], df["Marks"], label="Students")

# Add title and labels
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
