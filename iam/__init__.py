import abc

ACCOUNT_ID = '123456789'


class AbstractResource(abc.ABC):
    @abc.abstractproperty
    def service(self):
        pass

    @abc.abstractproperty
    def resource_type(self):
        pass

    @property
    def arn(self):
        return f'arn:aws:{self.service}::{ACCOUNT_ID}:{self.resource_type}/{self.name}'


class AbstractIamResource(AbstractResource):
    def __init__(self, name):
        self.name = name

    @property
    def service(self):
        return 'iam'


class Role(AbstractIamResource):
    @property
    def resource_type(self):
        return 'role'


class Policy(AbstractIamResource):
    @property
    def resource_type(self):
        return 'policy'
