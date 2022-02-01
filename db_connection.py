from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

SECURE_CONNECT_BUNDLE = r"C:\Users\Shankar Wagh SNR\Desktop\Data_Science_Course\Internship\I-NEURON\Astra DB\secure-connect-sample.zip"
USERNAME = 'qBYUXirKQnEPmuXnraYUHHdJ'
PASSWORD = 'mMSs.wRDJW7K7fjjKLGgup2bbv5ojh-l4SivkG78H0KDJBb6ituFaHxq6ahPzwmCvAN+cUQQlrKECTpFT+qYDQX0Wijv94Z4opyy7xKZgwLyWC5ktO2-M5,j9u48cmGz'
KEYSPACE = 'sample'

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