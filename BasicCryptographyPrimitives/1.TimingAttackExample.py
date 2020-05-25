
# the function "check_pasword" works with 4-digits passwords and is susceptible to timing attacks. 
# It takes it around 0.1 seconds to check one digit.
import time
real_password="9759"
def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    test_password="0000"
    cracked=False
    current_digit=1
    value_to_change=0
    while cracked==False:
        if check_password(test_password):
            cracked =True
        else:
            start_time=time.time()
            check_password(test_password)
            gap_time=time.time()-start_time
            if ((current_digit *.1)<=gap_time) & (gap_time<= (current_digit *.1)+0.1):
                value_to_change=value_to_change+1
                if current_digit==1:
                    test_password=str(value_to_change)+test_password[current_digit:4]
                else:
                    head=test_password[0:current_digit-1]
                    tail=test_password[current_digit:4]
                    test_password=head + str(value_to_change)+ tail
            else:
                current_digit=current_digit+1
                value_to_change=1
                head=test_password[0:current_digit-1]
                tail=test_password[current_digit:4]
                test_password=head + str(value_to_change)+ tail
            if value_to_change==10:
                break
    print(test_password)
    return test_password

crack_password()

