# a = p(1+r/100)pwr*t
# cp = a-p
def compound_interest(p, r, t):
    amount = p*(pow((1+r/100), t))
    ci = amount - p
    print("ci is ", ci)


compound_interest(10000, 10.25, 5)
