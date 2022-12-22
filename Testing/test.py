# Test 1

def check_num(quantite):
    # Check if isNumeric
    if quantite.isnumeric():
        if int(quantite) > 0:
        # If it is a number convert it to an int
            return True#int(quantite)
    return False

""" print(check_num('6'))
print(check_num('Ok'))
print(check_num("45"))
print(check_num(""))
print(check_num("4 ok 5"))
print(check_num("0")) """


# Test 2
def check_type(vin):
    match vin.lower():
        case 'rouge':
            return True
        case 'rose':
            # Verifier que tout ce passe bien avec les accents
            return True
        case 'blanc':
            return True
        case 'mousseux':
            return True
        case 'champagne':
            return True
        case 'autres':
            return True
        case _:
            return False

""" print(check_type('Rouge'))
print(check_type('Blanc'))
print(check_type('autres'))
print(check_type('zebi')) """

# Test 3
def nom_not_null(vin):
    if(vin == None or vin == ""):
        return False
    return True

print(nom_not_null(""))
print(nom_not_null(None))

