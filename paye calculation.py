#NUMBER 1

def paye(amount):#defining the function with amount as the parameter
    if amount<250000:#if the amount is less than 250000
        return 0#returning 0
    elif 250000<amount<350000:#if the amount is between 250000 and 350000
        return amount*0.1#returning the amount multiplied by 0.1
    elif 350000<amount<450000:#if the amount is between 350000 and 450000
        return 25000+amount*0.2#returning 25000 plus the amount multiplied by 0.2
    else:
        return 35000+amount*0.3#returning 35000 plus the amount multiplied by 0.3
def main():
    amount=eval(input("Enter the amount"))
    print("The paye is ",paye(amount))#printing the paye
main()