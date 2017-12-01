from cassandra.cluster import Cluster, NoHostAvailable


class Connector:
    """Connect to a list of Cassandra hosts and check if they are alive"""

    def __init__(self, hosts):
        self.hosts = hosts

    def is_host_alive(self, host):
        """Check if the host is alive

        :returns bool: True if the host is alive
        """

        # This function cannot be tested
        try:
            cluster = Cluster([host])
            cluster.connect()
            cluster.shutdown()
            return True
        except NoHostAvailable:
            return False

    def get_num_of_dead_nodes(self):
        """Return number of dead nodes in the cluster

        :returns int: number of dead nodes in the cluster
        """

        dead_nodes = 0
        for host in self.hosts:
            if not self.is_host_alive(host):
                dead_nodes += 1

        return dead_nodes

    def get_num_of_alive_nodes(self):
        """Return number of alive nodes in the cluster

        :returns int: number of alive nodes
        """

        return len(self.hosts) - self.get_num_of_dead_nodes();
