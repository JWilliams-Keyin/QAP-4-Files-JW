# Description: This program is used to enter new insurance claims for customers
#              of the One Stop Insurance Company
# Dates:       July 16th -
# Author:      Jack Williams

# Libraries #

import datetime
import time
import sys

# Functions #
# (Commented ones were validation functions that I gave up on) #

# def blankValidation(string):
#    if string == '':
#       validation = True
#    else:
#       validation = False
   
#    if validation == True:
#       print ('ERROR: This field must be entered')
#       print()
#       valid == False
#    else:
#       valid = True
#    return valid


# def yesNoValidation(variable):
#    while True:
#       variable = input('Does the customer want extra liability up to $1,000,000? (Y/N): ')
#       print()
#       if variable not in YES_NO_LST:
#          print('ERROR: Please enter either Y or N')
#          print()
#       else:
#          variable.upper
#          break


def dollarFormat(dollarValue):
   dollarValueDsp = '${:,.2f}'.format(dollarValue)
   return dollarValueDsp


def dateFormat(dateValue):
   dateValueDsp = dateValue.strftime("%Y-%m-%d")
   return dateValueDsp


def progressBar(iteration, total, prefix = '', suffix = '', length = 30, fill = '█'):

   percent = ("{0:.1f}").format(100 * (iteration / float(total)))
   filled_length = int(length * iteration // total)
   bar = fill * filled_length + '-' * (length - filled_length)
   sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
   sys.stdout.flush()


# Constants #

CUR_DATE = datetime.datetime.now()
PROV_LST = ['AB', 'ab', 'BC', 'bc', 'MB', 'mb', 'NB', 'nb', 'NL', 'nl', 
'NT', 'nt', 'NS', 'ns', 'NU', 'nu', 'ON', 'on', 'PE', 'pe', 'QC', 'qc',
'SK', 'sk', 'YT', 'yt']
PAY_OP_LST = ['Full', 'full', 'Monthly', 'monthly', 'Down Pay', 'down pay']
YES_NO_LST = ['Y', 'N', 'y', 'n']
PREV_CLAIM1 = ['01927', '2020-06-21', '$19,140.00']
PREV_CLAIM2 = ['01934', '2020-07-15', '$20,355.25']
PREV_CLAIM3 = ['02342', '2021-10-19', '$10,990.50']

# Constants From Data Files #

f1 = open('Const.dat', 'r')

for constants in f1:
   constantsLST = constants.split(',')

   POLICYNUM = int(constantsLST[0].strip())
   CAR_RATE = float(constantsLST[1].strip())
   DISCOUNT_RATE = float(constantsLST[2].strip())
   EX_LIABILITY_RATE = float(constantsLST[3].strip())
   GLASS_COV_RATE = float(constantsLST[4].strip())
   LOAN_CAR_RATE = float(constantsLST[5].strip())
   HST_RATE = float(constantsLST[6].strip())
   PROC_RATE = float(constantsLST[7].strip())

f1.close()

# Main Program Loop #

while True:
   # Input Statements #

   print()
   print('One Stop Insurance')
   print()
   print('Please fill out all fields')
   print()
   custName = input("Enter the customer's first and last name: ")
   custName = str(custName).title()
   print()
   custAdd = input("Enter the customer's street address: ")
   custAdd = str(custAdd).title()
   print()
   custCity = input("Enter the city the customer lives in: ")
   custCity = str(custCity).title()
   print()

   while True:
      custProv = input("Enter the province the customer lives in (XX): ")
      print()
      if custProv == '':
         print('ERROR: Province must be entered')
         print()
      elif custProv not in PROV_LST:
         print('ERROR: The province you entered is invalid')
         print('NOTE: Province must be abbreviated to two characters')
         print()
      else:
         custProv = str(custProv).upper()
         break

   custPostCode = input("Enter the customer's postal code: ")
   custPostCode = str(custPostCode).upper()
   print()

   while True:
      custPhoneNum = input("Enter the customer's phone number (XXXXXXXXXX): ")
      print()
      if custPhoneNum == '':
         print('ERROR: The phone number must not be blank')
         print()
      elif custPhoneNum.isnumeric() == False:
         print('ERROR: The phone number must be numerical only')
         print('NOTE: Enter just the numbers, no extra characters or spaces')
         print()
      elif len(custPhoneNum) != 10:
         print('ERROR: The phone number must be ten digits long')
         print()
      else:
         break

   while True: 
      carNum = input('Enter the amount of cars being insured: ')
      print()
      if carNum == '':
         print('ERROR: The amount of cars being insured must be entered')
         print()
      elif carNum.isnumeric == False:
         print('ERROR: The value entered is invalid')
         print('NOTE: Enter the numeric value, do not spell out the number')
         print()
      else:
         carNumCalc = float(carNum)
         break
   
   while True:
      exLiability = input('Does the customer want extra liability up to $1,000,000? (Y/N): ')
      print()
      if exLiability not in YES_NO_LST:
         print('ERROR: Please enter either Y or N')
         print()
      else:
         exLiability = str(exLiability).upper()
         break
   
   while True:
      glassCov = input('Does the customer want glass coverage? (Y/N): ')
      print()
      if glassCov not in YES_NO_LST:
         print('ERROR: Please enter either Y or N')
         print()
      else:
         glassCov = str(glassCov).upper()
         break

   while True:
      loanCar = input('Does the customer want a loaner car? (Y/N): ')
      print()
      if loanCar not in YES_NO_LST:
         print('ERROR: Please enter either Y or N')
         print()
      else:
         loanCar = str(loanCar).upper()
         break
   
   while True:
      payMethod = input("Enter Does the customer's desired payment method (Full, Monthly, Down Pay): ")
      print()
      if payMethod == '':
         print('ERROR: Payment method must be entered')
         print()
      elif payMethod not in PAY_OP_LST:
         print('ERROR: Payment method must be entered as "Full", "Monthly", or "Down Pay"')
         print()
      else:
         payMethod = str(payMethod).title()
         break

   if payMethod == PAY_OP_LST[4]:
      while True:
         downPay = input("Enter the customer's down payment: ")
         print()
         if downPay == '':
            print('ERROR: This field must be entered')
            print()
         elif downPay.isalpha() == True:
            print('ERROR: The down payment must be numeric only')
            print()
         else:
            downPay = float(downPay)
            break
   else:
      downPay = 0

   claimNum = input('Enter the claim number: ')
   print()
   claimDate = input('Enter the claim date (YYYY-MM-DD): ')
   claimDate = datetime.datetime.strptime(claimDate, '%Y-%m-%d')
   print()
   claimAmt = input('Enter the amount of previous claims from the customer: ')
   print()

  # Calculations #
   
   if carNumCalc >= 1:
      addCar = (CAR_RATE - (CAR_RATE * DISCOUNT_RATE)) * (float(carNum) - 1)
   else:
      addCar = 0

   insurPrem = CAR_RATE + addCar
   totExCosts = float(0)

   if exLiability == YES_NO_LST[0]:
      totExCosts += (EX_LIABILITY_RATE * carNumCalc)
      exLiabilityCalc = EX_LIABILITY_RATE * carNumCalc
   elif exLiability == YES_NO_LST[1]:
      exLiabilityCalc = 0
      
   if glassCov == YES_NO_LST[0]:
      totExCosts += (GLASS_COV_RATE * carNumCalc)
      glassCovCalc = GLASS_COV_RATE * carNumCalc
   elif glassCov == YES_NO_LST[1]:
      glassCovCalc = 0

   if loanCar == YES_NO_LST[0]:
      totExCosts += (LOAN_CAR_RATE * carNumCalc)
      loanCarCalc = LOAN_CAR_RATE * carNumCalc
   elif loanCar == YES_NO_LST[1]:
      loanCarCalc = 0

   totInsurPrem = insurPrem + totExCosts
   HST = totInsurPrem * HST_RATE
   totCost = totInsurPrem + HST

   monPayment = ((totCost - downPay) + PROC_RATE) / 8

   invoiceDate = dateFormat(CUR_DATE)
   firstPayDay = 1
   firstPayMonth = CUR_DATE.month + 1
   firstPayYear = CUR_DATE.year 

   if firstPayMonth >= 13:
      firstPayMonth -= 12
      firstPayYear += 1

   firstPayDate = datetime.datetime(firstPayYear, firstPayMonth, firstPayDay)
   firstPayDateDsp = dateFormat(firstPayDate)

   # Write Inputs #

   f2 = open('Claims.dat', 'w')

   f2.write(f'{custName}, {custAdd}, {custCity}, {custProv}, {custPostCode}, {custPhoneNum}, {carNum}, {exLiability}, {glassCov}, {loanCar}, {payMethod}, {downPay}, {claimNum}, {claimDate}, {claimAmt}, {totInsurPrem}')

   f2.close()

   # Progress Bar and Blinking Message #

   barIterations = 50
   savingMessage = 'Saving Claim Data...'
   savedMessage = 'Claim Data Saved'
   printingMessage = 'Printing Invoice...'
 
   for i in range(barIterations + 1):
      time.sleep(0.1)
      progressBar(i, barIterations, prefix = savingMessage, suffix = savedMessage, length = 50)
 
   time.sleep(1)
   print()

   for _ in range(6):
      print(printingMessage, end = '\r')
      time.sleep(0.4)
      sys.stdout.write('\033[2K\r')
      time.sleep(0.4)

   print()

   # Output #

   custPhoneNumDsp = '(' + custPhoneNum[0:3] + ') ' + custPhoneNum[3:6] + '-' + custPhoneNum[6:10]

   insurPremDsp = dollarFormat(insurPrem)
   
   exLiabilityDsp = dollarFormat(exLiabilityCalc)
   glassCovDsp = dollarFormat(glassCovCalc)
   loanCarDsp = dollarFormat(loanCarCalc)

   downPayDsp = dollarFormat(downPay)

   totExCostsDsp = dollarFormat(totExCosts)
   totInsurPremDsp = dollarFormat(totInsurPrem)
   HSTDsp = dollarFormat(HST)
   totCostDsp = dollarFormat(totCost)

   monPayDsp = dollarFormat(monPayment)

   claimDateDsp = claimDate.strftime('%Y-%m-%d')

   #                1         2         3         4         5         6         6    
   #       12345678901234567890123456789012345678901234567890123456789012345678901234

   print(f'+------------------------------------------------------------------------+')
   print(f'|                       One Stop Insurance Company                       |')
   print(f'+------------------------------------------------------------------------+')
   print(f'                          Customer Claim Invoice                          ')
   print(f'  Customer Info                                                           ')
   print(f'                                                                          ')
   print(f'  {custName}                                                              ')
   print(f'  {custPhoneNumDsp}                                                       ')
   print(f'  {custAdd},                                                              ')
   print(f'  {custCity}, {custPostCode}, {custProv}                                  ')
   print(f'                                                                          ')
   print(f'  Previous Claims: {claimAmt}                                             ')
   print(f'+------------------------------------------------------------------------+')
   print(f'  Claim Date: {claimDateDsp}           Invoice Date: {invoiceDate}')
   print(f'  Claim Number: {claimNum:<5s}                                            ')
   print(f'                                                                  ')
   print(f'  Insurance Premium: {insurPremDsp:<10s}    Total Extra Costs: {totExCostsDsp:<10s}')
   print(f'                                                             ')
   print(f'  Extra Liability:   {exLiabilityDsp:<7s}       Total Premium:     {totInsurPremDsp:<11s}')
   print(f'  Glass Coverage:    {glassCovDsp:<7s}       HST:               {HSTDsp:<7s}')
   print(f'  Loaner Cars:       {loanCarDsp:<7s}       Total Cost:        {totCostDsp:<11s}')
   print(f'+------------------------------------------------------------------------+')

   if payMethod == PAY_OP_LST[0]:
      print(f'  Amount Due: {totCostDsp:<11s}')
   elif payMethod == PAY_OP_LST[2]:
      print(f'  Monthly Payment (8 months): {monPayDsp}')
   elif payMethod == PAY_OP_LST[4]:
      print(f'  Down Payment: {downPayDsp:<10s} Monthly Payment (8 months): {monPayDsp}')

   print(f'+------------------------------------------------------------------------+')
   print(f'                     Claim #  Claim Date        Amount')
   print(f'                     ---------------------------------')
   print(f'                     {PREV_CLAIM1[0]}    {PREV_CLAIM1[1]}    {PREV_CLAIM1[2]}')
   print(f'                     {PREV_CLAIM2[0]}    {PREV_CLAIM2[1]}    {PREV_CLAIM2[2]}')
   print(f'                     {PREV_CLAIM3[0]}    {PREV_CLAIM3[1]}    {PREV_CLAIM3[2]}')
   print()


   # End Statement #

   while True:
      endStatement = input('Do you want to enter another claim? (Y/N): ')
      endStatement = endStatement.upper()
      print()
      if endStatement == YES_NO_LST[1]:
         exit()
      elif endStatement not in YES_NO_LST:
         print('ERROR: Please enter either Y or N')
         print()
      elif endStatement == YES_NO_LST[0]:
         break