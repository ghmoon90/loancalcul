import numpy as np
import tkinter as *


def redemption_maturity (principal, rate_per_yr,month_duration):
    principals = np.zeros([month_duration])
    principals[month_duration-1] = principal
    rate_per_month = rate_per_yr / 12 
    print('interest rate : ' + str(rate_per_yr) + ' %')
    print('duration : ' + str(month_duration) + ' month')
    interests  =  np.ones([month_duration]) * ( rate_per_month * principal /100)
    print('month, principal, interest, monthly sum')
    for i in range(0,month_duration):
        newline = str( i+1 ) +'\t' + str( principals[i] )+'\t' + str( interests[i]  )+'\t' + str( principals[i]+interests[i]  )+'\n'
        print( newline )
    total = principals.sum() + interests.sum()
    lastline = 'total redemption : '+ str(total) + '\n' + 'total interests : '+ str(interests.sum()) 
    print(lastline)
    
#redemption_maturity (170000000, 5.73,12)



def EqualityPrincipal(principal, rate_per_yr,month_duration):
    principals = np.ones([month_duration]) * principal / month_duration
    rate_per_month = rate_per_yr / 12 
    interests  =  np.ones([month_duration]) * principal * rate_per_month / 100
    print('interest rate : ' + str(rate_per_yr) + ' %')
    print('duration : ' + str(month_duration) + ' month')
    print('month, principal, interest, montly sum')
    for i in range(0,month_duration):
        interests[i] = interests[i] * ( 1 - i / month_duration )
    for i in range(0,month_duration):
        newline = str( i+1 ) +'\t' + str( principals[i] )+'\t' + str( interests[i]  )+'\t' + str( principals[i]+interests[i]  )+'\n'
        print( newline )
    total = principals.sum() + interests.sum()
    lastline = 'total sum : '+ str(total) + '\n' + 'interest sum : '+ str(interests.sum()) 
    print(lastline)
#EqualityPrincipal (170000000, 5.73,12)

def EqualityPrincipalInterest(principal, rate_per_yr,month_duration):
    principals = np.zeros([month_duration]) 
    rate_per_month = rate_per_yr / 12 
    KK =  pow( 1 + rate_per_month / 100 , month_duration ) 
    montly_sum = np.ones([month_duration]) * principal * rate_per_month / 100 * KK / (KK - 1)
    interests  = np.zeros([month_duration])
    print('interest rate : ' + str(rate_per_yr) + ' %')
    print('duration : ' + str(month_duration) + ' month')
    print('month, principal, interest, montly sum')
    for i in range(0,month_duration):
        principals[i] = montly_sum[i] - interests[i]
    for i in range(0,month_duration):
        newline = str( i+1 ) +'\t' + str( principals[i] )+'\t' + str( interests[i]  )+ '\t' + str(montly_sum[i]) + '\n'
        print( newline )
    total = principals.sum() + interests.sum()
    lastline = 'total sum : '+ str(total) + '\n' + 'interest sum : '+ str(interests.sum()) 
    print(lastline)

#EqualityPrincipalInterest (170000000, 5.73,12)