import xlsxwriter
from requests import Session

start = 1
f = 1

crypto_workbook = xlsxwriter.Workbook('cryptocurrencies.xlsx')
crypto_sheet = crypto_workbook.add_worksheet()

crypto_sheet.write('A1', 'Name')
crypto_sheet.write('B1', 'Symbol')
crypto_sheet.write('C1', 'Market cap')
crypto_sheet.write('D1', 'Price')
crypto_sheet.write('E1', '24H Volume')
crypto_sheet.write('F1', 'Hour Change')
crypto_sheet.write('G1', 'Day Change')
crypto_sheet.write('H1', 'Week Change')

