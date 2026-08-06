#class example using UPI example 

class UPI_ID:
    def __init__(self, id, bank_id):
        self.my_id = id
        self.my_bank_id = bank_id

    def __repr__(self):
        return "UPI {" + self.my_id + "@" + self.my_bank_id + "}"

    def __eq__(self, other):
        return self.my_id == other.my_id and self.my_bank_id == other.my_bank_id

ID = UPI_ID("59599595", "okabc")
print(ID)

somebody = ID
print(somebody is ID)
