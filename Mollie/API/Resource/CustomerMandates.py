from .Base import *
from Mollie.API.Error import *
from Mollie.API.Object import CustomerMandate


class CustomerMandates(Base):
    RESOURCE_ID_PREFIX = 'tr_'
    DEFAULT_LIMIT = 10
    parent_id = None

    def getResourceName(self):
        return 'customers'

    def rest_list(self, params=None):
        path = self.getResourceName() + '/%s/mandates' % self.parent_id
        result = self.performApiCall(self.REST_LIST, path, None, params)
        return List(result, self.getResourceObject({}).__class__)

    def withParentId(self, parent_id):
        self.parent_id = parent_id
        return self

    def getResourceObject(self, result):
        return CustomerMandate(result)
