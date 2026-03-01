
# Base class
class Payment:
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class WalletPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Wallet")


# User input
amount = float(input("Enter amount: "))
choice = input("Choose payment method (credit/upi/wallet): ")

if choice == "credit":
    payment = CreditCardPayment()
elif choice == "upi":
    payment = UPIPayment()
elif choice == "wallet":
    payment = WalletPayment()
else:
    print("Invalid payment method")
    exit()

payment.pay(amount)