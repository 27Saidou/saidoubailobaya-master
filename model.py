
class Formation(object):
    """
    Cette classe permet de mémoriser les informations
    sur les formations proposées par  le CSEI
    """
    
    def __init__(self, designation, description=None):
        """
        Constructeur de la classe Formation
        --------------
        Paramètres:
            designation (str): Désignation de la formation
            description (str): Description de la formation
        """
        self.designation = designation
        self.description = description

    def __str__(self):
        """
        Cette méthode permet d'afficher un objet Formation
        avec méthode print().
        Exemple: print(formation1)
        """
        return "Désignation: {} \nDescription: {}"\
               .format(self.designation, self.description)
