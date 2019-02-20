class ClusterConfigMap:
    __slots__ = ['fqdn']

    def __init__(self, fqdn, **kwargs):
        self.fqdn = fqdn

    def __str__(self):
        return self.__repr__() + " " + self.fqdn
