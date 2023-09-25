import os 
import csv

INPUT_CSV_PATH = os.path.join("python-challenge","PyBank","Resources", "budget_data.csv")

# Declare variables
count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
profit_loss_changes = []
months = 0

# Open and read csv
with open(INPUT_CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        count_months += 1
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if count_months == 1:
            previous_month_profit_loss = current_month_profit_loss
        else:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            profit_loss_changes.append(profit_loss_change)
            previous_month_profit_loss = current_month_profit_loss

# Calculate statistics
sum_profit_loss = sum(profit_loss_changes)
average_profit_loss = round(sum_profit_loss / (count_months - 1), 2)
highest_change = max(profit_loss_changes)
lowest_change = min(profit_loss_changes)
highest_month_index = profit_loss_changes.index(highest_change)
lowest_month_index = profit_loss_changes.index(lowest_change)


# Create lists of months and assign best and worst month
months = []
with open(INPUT_CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        months.append(row[0])

best_month = months[highest_month_index +1]
worst_month = months[lowest_month_index +1] 

# Print Analysis
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {count_months}")
print(f"Total: $ {net_profit_loss}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Increase in Profits: {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses: {worst_month} (${lowest_change})")

# Export a text file with the results
output_file = os.path.join("python-challenge","PyBank","budget_data.txt")
with open(output_file, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("-------------------\n")
    outfile.write(f"Total Months: {count_months}\n")
    outfile.write(f"Total: ${net_profit_loss}\n")
    outfile.write(f"Average Change: ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits: {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses: {worst_month} (${lowest_change})\n")
