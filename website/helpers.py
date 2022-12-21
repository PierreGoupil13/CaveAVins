def check_type(vin):

    match vin.lower():
        case 'rouge':
            return 1
        case 'rose':
            # Verifier que tout ce passe bien avec les accents
            return 1
        case 'blanc':
            return 1
        case 'mousseux':
            return 1
        case 'champagne':
            return 1
        case 'autres':
            return 1
        case _:
            return False
