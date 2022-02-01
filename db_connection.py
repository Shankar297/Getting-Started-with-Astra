from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

SECURE_CONNECT_BUNDLE = r""
USERNAME = ''
PASSWORD = ''
KEYSPACE = ''

class Connection:
    def __init__(self):
        self.secure_connect_bundle = SECURE_CONNECT_BUNDLE
        self.path_to_creds=''
        self.cluster = Cluster(
            cloud={'secure_connect_bundle': self.secure_connect_bundle}, auth_provider=PlainTextAuthProvider(USERNAME, PASSWORD)
        )
        self.session = self.cluster.connect(KEYSPACE)
        
    def close(self):
        self.cluster.shutdown()
        self.session.shutdown()