from xlsxwriter import Workbook


#make workbook

workbook = Workbook('firs_file.xlsx')

#add workbook

worksheet = workbook.add_worksheet()

#write function - parameter - (row, column, value)

#worksheet.write(0,0,'zero row and zero column')
#worksheet.write(1,1,'one row and one column')

for row in range(20):
    worksheet.write(row,0,'Row Number')
    worksheet.write(row,1,row)

#close workbook

workbook.close()