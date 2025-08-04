"""
    Shayane Katchera
    Ce fichier contiens les constantes, fonctions et les classes utiles 
"""

# ============================
# ======== CONSTANTES ========
# ============================

# les couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

# fonctions

# classes
class EnumMeta(type):
    def __iter__(cls):
        """ retourne un generateur pour faire `for item in Enum`"""
        return ((k, v) for k, v in cls.__dict__.items() if not k.startswith("__") and not callable(v))

    def __contains__(cls, item):
        """ vérifie si un élément est dans l'énumération """
        return item in (v for _, v in cls) or item in cls.__dict__

    def __str__(cls):
        """ Affiche les valeurs de l'énumération via print(Enum) """
        items = [f"{k}: {v}" for k, v in cls]
        return "\n".join(items)
