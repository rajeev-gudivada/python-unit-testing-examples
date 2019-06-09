import abc

ACCOUNT_ID = '123456789'


class AbstractResource(abc.ABC):
    @abc.abstractproperty
    def resource_type(self):
        pass


class IamResourceMixin:
    service = 'iam'


class AbstractIamResource(IamResourceMixin, AbstractResource):
    pass


class Role(AbstractIamResource):
    def __init__(self, name):
        self.name = name

    @property
    def resource_type(self):
        return 'role'

    @property
    def arn(self):
        return f'arn:aws:{self.service}::{ACCOUNT_ID}:{self.resource_type}/{self.name}'
