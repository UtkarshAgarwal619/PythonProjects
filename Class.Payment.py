class Payment:
    Razorpay = None
    Stipe = None
    Instamojo = None

    def Razorpay(self):
        print("Credit card")

    def Stipe(self):
        print("Debit card")
    def Instamojo(self):
        print("Gpay")

Fees=Payment()
Fees.Razorpay()
Fees.Instamojo()