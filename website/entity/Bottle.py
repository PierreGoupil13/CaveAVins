class Bottle():
    def __init__(self, name, num_caisse, quantity, comment, year, type_vin, producer, note):
        self.name = name
        self.num_caisse = num_caisse
        self.quantity = quantity
        self.comment = comment
        self.year = year
        self.type = type_vin
        self.producer = producer
        self.note = note
    
    def ajouter_bouteille_bdd(self):
        # Ajouter la bouteille à la bdd
        pass
    

