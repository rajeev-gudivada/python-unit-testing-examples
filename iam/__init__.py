class Role:
    def __init__(self, name):
        self.name = name

    @property
    def arn(self):
        return f'arn:aws:iam::123456789:role/{self.name}'
