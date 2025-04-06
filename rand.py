#to execute testing/temporary code
import pandas as pd
import pyperclip
# Load the CSV file
df = pd.read_csv(r"C:\Users\samiksha\Desktop\accenture_hackathon\job_description.csv", encoding='ISO-8859-1')

second_column = df.iloc[:, 1]

# Convert the column to a string (separated by newline)
column_str = '\n'.join(second_column.astype(str))

# Copy to clipboard
pyperclip.copy(column_str)
