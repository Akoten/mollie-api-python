from .Base import *
from Mollie.API.Error import *
from Mollie.API.Object import Customer


class Customers(Base):
    RESOURCE_ID_PREFIX = 'tr_'


    def getResourceObject(self, result):
        return Customer(result)
