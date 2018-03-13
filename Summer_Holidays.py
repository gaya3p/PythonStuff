import datetime

#It all started on 4th May
start = datetime.date(2018, 3, 10)
start_day = start.day
today = datetime.datetime.today()#(datetime.date(2017, 6, 4))

if (today.month) ==3:# If its May, then
    days_over = ((today.day) - start_day)
else:# If its May, then
    days_over = (today.day+27)
     
print('Days over : ', days_over)# Days over
# if Days_Over > 20:
#   raise Sadness
# else:
#   raise Happiness!!!
try:
    Qs = input("Questions done : ")# 17 in total
        
    def get_it():
        
        days_reqd = int(round((17*days_over)/(int(Qs))))# as days_passed : Qs_done :: x_days : total_Qs
        print('Days reqired :', int(round(days_reqd)))
        
        DAYS_REQD = (str(int(days_reqd)+4))+ ' May, 2017' if today.month == 5 else (str(int((4+days_reqd)-31)) + ' June, 2017')
            
        return DAYS_REQD


    print('Going at this velocity, Summer Holiday Homeworks will be done on', get_it(), '.')
    
except ZeroDivisionError:
    print('You will never do it...')
    
except TypeError:
    print('You cant do, \"', Qs, '\" questions... its against maths!')
# Good Habits! -->

print('\nHappy Summer Time...!')
