import numpy as np
import tkinter as tk

#%% core


def redemption_maturity (principal, rate_per_yr,month_duration):
    principals = np.zeros([month_duration])
    principals[month_duration-1] = principal
    rate_per_month = rate_per_yr / 12 
    print('interest rate : ' + str(rate_per_yr) + ' %')
    print('duration : ' + str(month_duration) + ' month')
    interests  =  np.ones([month_duration]) * ( rate_per_month * principal /100)
    montly_sum =  np.zeros([month_duration])
    print('month, \t principal, \t interest, \t monthly sum\n')
    for i in range(0,month_duration):
        montly_sum[i] = principals[i]+interests[i]
        newline = str( i+1 ) +'\t' + '{0:0.1f}'.format( principals[i] )+'\t' + '{0:0.1f}'.format( interests[i]  )+'\t' + '{0:0.1f}'.format( montly_sum[i]  )+'\t'+ '\n'
        print( newline )
    total = principals.sum() + interests.sum()
    lastline = 'total redemption : '+ str(total) + '\n' + 'total interests : '+ str(interests.sum()) 
    print(lastline)
    return principals, interests, montly_sum 
    
#redemption_maturity (170000000, 5.73,12)


#원금균등상환
def EqualityPrincipal(principal, rate_per_yr,month_duration):
    principals = np.ones([month_duration]) * principal / month_duration
    rate_per_month = rate_per_yr / 12 
    interests  =  np.ones([month_duration]) * principal * rate_per_month / 100
    montly_sum =  np.zeros([month_duration])
    remaining = np.zeros([month_duration])
    print('interest rate : ' + str(rate_per_yr) + ' %')
    print('duration : ' + str(month_duration) + ' month')
    print('month, \t principal,\t interest,\t montly sum \t remaining \n')
    for i in range(0,month_duration):
        interests[i] = interests[i] * ( 1 - i / month_duration )
        remaining[i] = principal - principals[0:i+1].sum()
    for i in range(0,month_duration):
        montly_sum[i] = principals[i]+interests[i]        
        newline = str( i+1 ) +'\t' + '{0:0.1f}'.format( principals[i] )+'\t' + '{0:0.1f}'.format( interests[i]  )+'\t' + '{0:0.1f}'.format( montly_sum[i]  )+'\t' + '{0:0.1f}'.format( remaining[i]  )+'\n'
        print( newline )
    total = principals.sum() + interests.sum()
    lastline = 'total sum : '+ str(total) + '\n' + 'interest sum : '+ str(interests.sum()) 
    print(lastline)    
    return principals, interests, montly_sum, remaining
#EqualityPrincipal (170000000, 5.73,12)
#EqualityPrincipal (100000000, 5.73,12)

#원리금균등상환
def EqualityPrincipalInterest(principal, rate_per_yr,month_duration):
    principals = np.zeros([month_duration]) 
    rate_per_month = rate_per_yr / 12 
    KK =  pow( 1 + rate_per_month / 100 , month_duration ) 
    montly_sum = np.ones([month_duration]) * principal * rate_per_month / 100 * KK / (KK - 1)
    interests  = np.ones([month_duration])* principal * rate_per_month / 100
    remaining = np.zeros([month_duration])
    print('interest rate : ' + str(rate_per_yr) + ' %')
    print('duration : ' + str(month_duration) + ' month')
    print('month, \t principal,\t interest,\t montly sum \t remaining \n')
    remain = principal
    for i in range(0,month_duration):
        interests[i] = remain * rate_per_month / 100
        principals[i] = montly_sum[0] - interests[i]
        remain = remain - principals[i]
        remaining[i] = remain
    for i in range(0,month_duration):
        newline = str( i+1 ) +'\t' + '{0:0.1f}'.format( principals[i] )+'\t' + '{0:0.1f}'.format( interests[i]  )+'\t' + '{0:0.1f}'.format( montly_sum[i]  )+'\t' + '{0:0.1f}'.format( remaining[i]  )+'\n'
        print( newline )
    total = principals.sum() + interests.sum()
    lastline = 'total sum : '+ str(total) + '\n' + 'interest sum : '+ str(interests.sum()) 
    print(lastline)

#EqualityPrincipalInterest (170000000, 5.73,12)
# #EqualityPrincipalInterest (100000000, 5.73,12)

#중도상환수수료 계산
def EarlyRedemption(principal, month_duration, penalty_rate,remaining_days, exemption_period_yr):
    redemption = 0
    if (month_duration * 365/12 > exemption_period_yr * 365):
        if ((exemption_period_yr * 365)  > (month_duration * 30 - remaining_days)):
            redemption = principal * (penalty_rate /100)*  ( exemption_period_yr * 365 - (  month_duration * 365/12 - remaining_days ) ) /(exemption_period_yr * 365)
    else:
        redemption = principal * (penalty_rate /100)* remaining_days /(month_duration / 12 * 365)
    return redemption

#EarlyRedemption(100000000, 24, 1,365, 3)
#EarlyRedemption(100000000, 48, 1,730, 3)
#EarlyRedemption(100000000, 12 * 22, 1,365*2, 3)

#%% tkinter gui 
#window = tkinter.Tk()

def main ():

    sz_prompt = 'loancalcul 옵션선택 : \n 1 \t원리금 균등상환 \n 2\t원금균등상환 \n 3\t만기일시상환 \n 4\t중도상환수수료\n'

    option = int(input(sz_prompt))
    #print(option==1)
    if (option == 1 |  2| 3):
        principal = float(input('원금:' ))
        rate_per_yr = float(input('이자 %:' ))
        month_duration = int(input('대출기간 (month):' ))
        if option == 1 :
            EqualityPrincipalInterest(principal, rate_per_yr,month_duration)
        elif option == 2 :
            EqualityPrincipal(principal, rate_per_yr,month_duration)
        elif option == 3 :
            redemption_maturity (principal, rate_per_yr,month_duration)

    elif option == 4:
        principal = float(input('원금:' ))
        month_duration = int(input('대출기간 (month):' ))
        penalty_rate = float(input('중도상환 수수료 %:' ))
        remaining_days = int(input('잔여기간 (days):' ))
        exemption_period_yr = int(input('면제기간 (yr):' ))
        redemption= EarlyRedemption(principal, month_duration, penalty_rate,remaining_days, exemption_period_yr)
        print(redemption)

if __name__ =="__main__":
    main()

