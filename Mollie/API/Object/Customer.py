from .Base import *


class Customer(Base):

    @property
    def id(self):
        return self.get('id')
