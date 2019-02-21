import string
import random


class ClusterConfigMap:
    __slots__ = ['fqdn', 'secrets_map', 'namespace']

    def __init__(self, fqdn, namespace="default"):
        self.fqdn = fqdn
        self.namespace = namespace
        self.secrets_map = {}

    def ensureSecret(self, secret_identifier, size=32):
        if secret_identifier not in self.secrets_map:
            alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
            generated = ''.join(random.choice(alphabet) for _ in range(size))
            self.secrets_map[secret_identifier] = generated
        return self.secrets_map[secret_identifier]

    def __str__(self):
        return self.__repr__() + " " + self.fqdn
