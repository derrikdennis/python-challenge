
import csv

csvpath = "Resources/budget_data.csv"

# Reading in the file.  I am also setting my values to start that I will use.
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter = ',')
    csv_header = next(csvreader)    

    Month = []
    profitLoss = []
    profitLossChange = []
    totalProfitLoss = 0
    maxProfitLossChange = 0
    minProfitLossChange = 0
    maxProfitLossMonth = ' '
    minProfitLossMonth = ' '

# for every row, I am appending my local list to include the Month, the Profit/loss and the Total Profit/Loss
    for row in csvreader:
        Month.append(row[0])
        profitLoss.append(float(row[1]))
        totalProfitLoss += float(row[1])

#This will give me the change month-over-month for profit/loss.
#It will also identify when I had the maximum and minimum months for profit/loss
    for x in range(1,len(profitLoss)):
        profitLossChange.append(profitLoss[x] - profitLoss[x-1])
        if (profitLoss[x] - profitLoss[x-1]) > maxProfitLossChange:
            maxProfitLossChange = (profitLoss[x] - profitLoss[x-1])
            maxProfitLossMonth = Month[x]
        if (profitLoss[x] - profitLoss[x-1]) < minProfitLossChange:
            minProfitLossChange = (profitLoss[x] - profitLoss[x-1])
            minProfitLossMonth = Month[x]

#Now I am figuring out what is the average change in profit/loss
    avg_PL_chg = round(sum(profitLossChange) / len(profitLossChange),2)


#This will print out to the terminal my findings
print("Financial Analysis")
print(" ----------------------------")
print("Total Months: " + str(len(Month)))
print("Total Revenue: " + '${:,.2f}'.format(totalProfitLoss))
print("Average Revenue Change: " + '${:,.2f}'.format(avg_PL_chg))
print("Greatest Increase in Profits: " + str(maxProfitLossMonth) + " " + '${:,.2f}'.format(maxProfitLossChange))
print("Greatest Decrease in Profits: " + str(minProfitLossMonth) + "  "+ '${:,.2f}'.format(minProfitLossChange))


#This will output to a file called py_Bank_Results my findings
output="py_Bank_Results.txt"
with open(output,"w+") as file:
    file.write("Financial Analysis\n")
    file.write(" ----------------------------\n")
    file.write("Total Months: " + str(len(Month))+"\n")
    file.write("Total Revenue: " + '${:,.2f}'.format(totalProfitLoss)+"\n")
    file.write("Average Revenue Change: " + '${:,.2f}'.format(avg_PL_chg)+"\n")
    file.write("Greatest Increase in Profits: " + str(maxProfitLossMonth) + " " + '${:,.2f}'.format(maxProfitLossChange)+"\n")
    file.write("Greatest Decrease in Profits: " + str(minProfitLossMonth) + " " + '${:,.2f}'.format(minProfitLossChange)+"\n")
