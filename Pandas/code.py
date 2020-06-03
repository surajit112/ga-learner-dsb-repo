# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank = pd.read_csv(path)
#print (bank.dtypes)
categorical_var=bank.select_dtypes(include='object')
print (categorical_var)
numerical_var=bank.select_dtypes(include='number')
print (numerical_var)
# code starts here






# code ends here


# --------------
# code starts here
banks=bank.drop(columns = ['Loan_ID'])
#banks.head()
banks.isnull().sum()
bank_mode=banks.mode()
#print (bank_mode)
#banks.fillna(bank_mode,inplace=True)
banks.replace(np.nan,bank_mode,inplace=True)
#code ends here


# --------------
# Code starts here






#print (banks.head())
avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'], values=['LoanAmount'],aggfunc='mean')
print (avg_loan_amount)



# code ends here



# --------------
# code starts here





loan_approved_se = banks.loc[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].count(0)[0]
print(loan_approved_se)
loan_approved_nse = banks.loc[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].count()[0]

Total = banks['Loan_Status'].count()
print (Total)
percentage_se = (loan_approved_se*100)/Total
percentage_nse = (loan_approved_nse*100)/Total
# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda month:month/12)
big_loan_term = loan_term[loan_term>=25].count()
print (big_loan_term)
# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby(['Loan_Status'])
loan_groupby=loan_groupby[['ApplicantIncome','Credit_History']]
mean_values = loan_groupby.mean()


# code ends here


