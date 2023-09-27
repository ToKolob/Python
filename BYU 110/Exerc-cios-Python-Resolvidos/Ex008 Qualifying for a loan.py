print ("First answer the following questions as 0 to 10\n")
loan_rate = int(input("How large is the loan?"))
credit_rate = int(input("How good is your credit history?"))
income_rate = int(input("How high is your income?"))
payment_rate = int(input("How large is your down payment?"))

if loan_rate >= 5:
    if credit_rate >= 7 and income_rate >=7:
        print ("\nLoan granted!!")
    elif credit_rate >= 7 or income_rate >=7:
        if payment_rate >= 5:
            print ("\nLoan granted!!")
        else:
            print ("\nGET OUT you loser!!")
    else:
        print ("\nGET OUT you loser!!")
elif loan_rate < 5:
    if credit_rate < 4:
        print ("\nGET OUT you loser!!")
    elif income_rate >= 7 or payment_rate >= 7:
        print ("\nLoan granted!!")
    elif income_rate >= 4 and payment_rate >= 4:
        print ("\nLoan granted!!")
    else :
        print ("\nGET OUT you loser!!")
else:
    print ("\nGET OUT you loser!!")



