def incomeTax(amount):
    if amount<=10000:
        tax=0
        print("no tax to pay")
    elif amount>=10000 and amount<=20000:
        tax = amount-10000
        total_tax = tax*(10/100)
        print("taxt to pay",total_tax)
    else:
        
        partial_tax= (10000)*(10/100)
        print(partial_tax)
        taxTOPAY = (amount-20000)*(20/100)
        print(taxTOPAY)
        final_tax=partial_tax+taxTOPAY
        print(final_tax)



amount=45000
incomeTax(amount)