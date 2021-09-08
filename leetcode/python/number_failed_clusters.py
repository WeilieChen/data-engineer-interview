"""
You are charge of a dataset that contains the operational state of your company's servers clusters. The Clusters dictionary contains information about which servers belong each cluster.  Below, cluster "A" includes servers 1, 2, and 3.  The Servers dictionary contains information about the operational state of each server.  The state will be 0 if the server is in a failed state and 1 if the server is in a successful state. Some of the servers are shared among multiple clusters. Below, server 4 is state 0, meaning it is in a failed state.

Write code to return the number of clusters that have at least 1 server in a failed state. Your code should accept a list of clusters as input.

Clusters {
    "A": [1, 2, 3],
    "B": [3, 4, 5],
    "C": [2, 4, 6]
}

Servers {
    1: 1,
    2: 1,
    3: 1,
    4: 0,
    5: 0,
    6: 1,
}

Example 1:
Input: ["A", "B", "C"]
Output: 2

Cluster A contains servers 1, 2, and 3.  Servers 1, 2, and 3 all have a state of 1, meaning none of them are failed. Cluster A should not be included in our count.
Cluster B contains servers 3, 4, and 5.  Servers 4, and 5 are in a failed state. Cluster B should be included in our count. Even though there are 2 failed servers in Cluster B, we should only increase our count by 1.
Cluster C contains servers 2, 4, and 6. Server 4 is in a failed state. Cluster C should be included our count.

Example 2:
Input: ["A"]
Output: 0

Cluster A contains servers 1, 2, and 3.  Servers 1, 2, and 3 all have a state of 1, meaning none of them are failed. Cluster A should not be included in our count.
"""

clusters = {
    "A": [1, 2, 3],
    "B": [3, 4, 5],
    "C": [2, 4, 6]
}
servers = {
    1: 1,
    2: 1,
    3: 1,
    4: 0,
    5: 0,
    6: 1,
}

def number_failed_clusters(cluster_list):
    count = 0
    for cluster in cluster_list:
        servers_list = clusters[cluster]

        for server in servers_list:
            status = servers[server]

            if status == 0:
                count += 1
                break

    return count
    
assert number_failed_clusters(["A", "B", "C"]) == 2
assert number_failed_clusters(["A"]) == 0
print("passed")