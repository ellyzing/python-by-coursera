class Value():
    def __get__(self, obj, obj_type):
        return self.value

    @staticmethod
    def amount_with_commision(obj, value):
        return int(value-value*obj.commission)

    def __set__(self, obj, value):
        self.value = self.amount_with_commision(obj, value)

    def __delete__(self, obj):
        print('delete')


class Account:
    amount = Value()
    def __init__(self, commission):
        self.commission = commission

# new_account = Account(0.1)
# new_account.amount = 100
# print(new_account.amount)
