import pathlib
import csv

# Identify file location
csv_path = pathlib.Path('Resources','budget_data.csv')

# Create my variables
Date = []
Profit_Loss = []
Average_Change = []

# Open the csv in read mode
with open(file=csv_path, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header labels
    csv_header = next(csvreader)
    # Loop through the rows
    for row in csvreader:
        # Append my variables to their lists
        Date.append(row[0])
        Profit_Loss.append(int(row[1]))
    # Loop through the profits to calculate the Average Change
    for i in range(len(Profit_Loss)-1):
        Average_Change.append(Profit_Loss[i+1]-Profit_Loss[i])

# Calculate the Total Months in dataset
Month_Count = len(Date)
# Calculate the Total Profits or Losses
Total = sum(Profit_Loss)
# Calculate the largest increase in profits
Increase_Profit = max(Average_Change)
# Calculate the largest decrease in profits
Decrease_Profit = min(Average_Change)
# Find the Month with the largest increase in profit
Increase_Month = Average_Change.index(max(Average_Change)) + 1
# Find the Month with the largest decrease in profit
Decrease_Month = Average_Change.index(min(Average_Change)) + 1

# Print the calculated values in the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Month_Count}")
print(f"Total: ${Total}")
print(f"Average Change: ${round(sum(Average_Change)/len(Average_Change),2)}")
print(f"Greatest Increase in Profits: {Date[Increase_Month]} (${(str(Increase_Profit))})")
print(f"Greatest Decrease in Profits: {Date[Decrease_Month]} (${(str(Decrease_Profit))})")

# Output a txt file to the Analysis folder
output_file = pathlib.Path("Analysis","Financial_Analysis_Summary.txt")

# Write the txt file
with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {Month_Count}")
    file.write("\n")
    file.write(f"Total: ${Total}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(Average_Change)/len(Average_Change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {Date[Increase_Month]} (${(str(Increase_Profit))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {Date[Decrease_Month]} (${(str(Decrease_Profit))})")