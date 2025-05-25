# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.

 

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.


# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

 
# Constraints:
#     1 <= numCourses <= 2000
#     0 <= prerequisites.length <= 5000
#     prerequisites[i].length == 2
#     0 <= ai, bi < numCourses
#     All the pairs prerequisites[i] are unique.

# essentially it is graph specified by segments and I need to find loops

class Solution(object):


    def traverse_graph(self, current_node):
        if current_node in self.recursion_stack:
            # Cycle detected
            return False
        
        if current_node in self.visited_nodes:
            # Already processed, no cycle from this node
            return True
        
        # Mark the node as visited and add to the recursion stack
        self.visited_nodes.add(current_node)
        self.recursion_stack.add(current_node)
        
        self.visited_nodes.add(current_node)

        # empty list needed for leafs
        neighbours = self.graph.get(current_node, [])
        for node in neighbours:

            if not self.traverse_graph(node):
                return False
            
        # Remove the node from the recursion stack after processing
        self.recursion_stack.remove(current_node)
        return True
        
    def canFinish(self, number_of_courses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Validate prerequisites
        for edge in prerequisites:
            if edge[0] >= number_of_courses or edge[1] >= number_of_courses:
                return False

        # convert graph to neigbours list
        # Convert graph to adjacency list
        # Convert graph to adjacency list
        self.graph = dict()
        
        for edge in prerequisites:
            if edge:
                # Self loop, returning
                if edge[0] == edge[1]:
                    return False
                current_neighbours = self.graph.get(edge[0], [])
                current_neighbours.append(edge[1])
                self.graph[edge[0]] = current_neighbours

        # Ensure all courses are included in the graph, even if they have no prerequisites
        for course in range(number_of_courses):
            if course not in self.graph:
                self.graph[course] = []

        # Check for loop from each node
        self.visited_nodes = set()
        self.recursion_stack = set()
        for node in self.graph.keys():  # Iterate over all nodes in the graph
            if not self.traverse_graph(node):
                return False
            
        return True