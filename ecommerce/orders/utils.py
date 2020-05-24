import string, random
from .models import Order


# def id_generator(length = 10, str = string.ascii_lowercase + string.digits):
#     the_id =  "".join(random.choice(str) for i in range(length))
#     try:
#         order = Order.objects.get(order_id=the_id)
#         id_generator()
#     except Order.DoesNotExist:
#         return the_id

def create_id():
    caracteres = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789@&é!ççà*$€£ù%?+#-"
    longueur = 20
    id = ""
    compteur = 0

    while compteur < longueur:
        lettre = caracteres[random.randint(0, len(caracteres)-1)]
        id += lettre
        compteur += 1
    return id