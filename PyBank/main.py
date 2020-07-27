
import csv

csvpath = "Resources/budget_data.csv"

# Reading in the file.  I am also setting my values to start that I will use.
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter = ',')
    csv_header = next(csvreader)    

    Month = []
    PL = []
    PL_chg = []
    TotalPL = 0
    max_PL_chg = 0
    min_PL_chg = 0
    max_PL_Month = ' '
    min_PL_Month = ' '

# for every row, I am appending my local list to include the Month, the Profit/loss and the Total Profit/Loss
    for row in csvreader:
        Month.append(row[0])
        PL.append(float(row[1]))
        TotalPL += float(row[1])

#This will give me the change month-over-month for profit/loss.
#It will also identify when I had the maximum and minimum months for profit/loss
    for x in range(1,len(PL)):
        PL_chg.append(PL[x] - PL[x-1])
        if (PL[x] - PL[x-1]) > max_PL_chg:
            max_PL_chg = (PL[x] - PL[x-1])
            max_PL_Month = Month[x]
        if (PL[x] - PL[x-1]) < min_PL_chg:
            min_PL_chg = (PL[x] - PL[x-1])
            min_PL_Month = Month[x]

#Now I am figuring out what is the average change in profit/loss
    avg_PL_chg = round(sum(PL_chg) / len(PL_chg),2)


#This will print out to the terminal my findings
print("Financial Analysis")
print(" ----------------------------")
print("Total Months: " + str(len(Month)))
print("Total Revenue: " + '${:,.2f}'.format(TotalPL))
print("Average Revenue Change: " + '${:,.2f}'.format(avg_PL_chg))
print("Greatest Increase in Profits: " + str(max_PL_Month) + " " + '${:,.2f}'.format(max_PL_chg))
print("Greatest Decrease in Profits: " + str(min_PL_Month) + "  "+ '${:,.2f}'.format(min_PL_chg))


#This will output to a file called py_Bank_Results my findings
output="py_Bank_Results.txt"
with open(output,"w+") as file:
    file.write("Financial Analysis\n")
    file.write(" ----------------------------\n")
    file.write("Total Months: " + str(len(Month))+"\n")
    file.write("Total Revenue: " + '${:,.2f}'.format(TotalPL)+"\n")
    file.write("Average Revenue Change: " + '${:,.2f}'.format(avg_PL_chg)+"\n")
    file.write("Greatest Increase in Profits: " + str(max_PL_Month) + " " + '${:,.2f}'.format(max_PL_chg)+"\n")
    file.write("Greatest Decrease in Profits: " + str(min_PL_Month) + " " + '${:,.2f}'.format(min_PL_chg)+"\n")
