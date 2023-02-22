def sale_tax(money):
    x = input("does sales tax apply? (y-n): ")
    if x=="y":
        return money*0.08
    else:
        return 0


def VAT(money):
    x = input("does vat tax apply? (y-n): ")
    if x=="y":
        return money*0.04
    else:
        return 0

def whatToPay():
    price = float(input("what is the bill: "))
    s_tax = sale_tax(price)
    v_tax = VAT(price)
    print("Your sales tax is ", s_tax)
    print("Your V tax is ", v_tax)
    total = price + s_tax + v_tax
    print("what you need to pay is ", total)



whatToPay()
    

    
    
