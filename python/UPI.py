#UPI handle
#Practice - create a dictionary of upi handles
#'key' must be a phone number


def create_handle(uid, bank_id):
    return(uid, bank_id)

def read_id(uh):
    return uh[0]

def read_bank_id(uh):
    return uh[1]

def test_upi_handle():
    dh = ("9878","abc")
    assert read_id(dh) == "9878"
