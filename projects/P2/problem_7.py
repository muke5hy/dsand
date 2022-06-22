import collections

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = collections.defaultdict(RouteTrieNode)
        self.handler = handler
        
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()
        
    def insert(self, handler, paths):
        current_node = self.root

        for path in paths:
            current_node = current_node.children[path]            
        current_node.handler = handler
        
    def find(self, paths):
        current_node = self.root

        for path in paths:
            if path not in current_node.children:
                return False

            current_node = current_node.children[path]
        return current_node.handler

class Router:
    def __init__(self, found_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        self.routes = RouteTrie()
        self.routes.insert(found_handler, "/")
        self.not_found = not_found_handler
        
    def add_handler(self, path, handler):
        self.routes.insert(handler, self.split_path(path))
        
    def lookup(self, path):
        return self.routes.find(self.split_path(path)) or self.not_found
    
    def split_path(self, path):
        stripped_path = path.strip("/")
        if stripped_path == "":
            return "/"
        else:
            return stripped_path


# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print ("Pass" if  ("root handler" == router.lookup("/")) else "Fail")
print ("Pass" if  ("not found handler" == router.lookup("/home")) else "Fail")
print ("Pass" if  ("about handler" == router.lookup("/home/about")) else "Fail")
print ("Pass" if  ("about handler" == router.lookup("/home/about/")) else "Fail")
print ("Pass" if  ("not found handler" == router.lookup("/home/about/me")) else "Fail")
print ("Pass" if  ("not found handler" == router.lookup(".")) else "Fail")