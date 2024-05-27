#!/usr/bin/env python3

"""
    jbfekjbwkjebkcjbds
"""

# Definición de los mixins
class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Definición de la clase Dragon que hereda de ambos mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
