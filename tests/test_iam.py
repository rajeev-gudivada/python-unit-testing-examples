import unittest

from iam import Role, Policy


class RoleTests(unittest.TestCase):

    def test_arn(self):
        name = 'rds-monitoring-role'
        role = Role(name=name)

        ret = role.arn

        assert ret == 'arn:aws:iam::123456789:role/rds-monitoring-role'


class PolicyTests(unittest.TestCase):

    def test_arn(self):
        name = 'DenyIAMAccess'
        role = Policy(name=name)

        ret = role.arn

        assert ret == 'arn:aws:iam::123456789:policy/DenyIAMAccess'
