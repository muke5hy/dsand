class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []      # list of class Groups
        self.users = []       # list of string user

    def add_group(self, group):
        if debug: print("[[add_group]]: {}".format(group))
        self.groups.append(group)

    def add_user(self,user):
        if debug: print("[[add_user]]: {}".format(user))
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    
def is_user_in_group(user, group, grp_queue = None):

    group_queue = []

    # Match user to group's name
    if user == group.get_name():
        # print("user matches group name")
        return True
    
    # Match user to get_users
    elif user in group.get_users():
        # print("user is in group's user list")
        return True
    
    # if Group's group list not empty, recurse 
    if len(group.get_groups()) == 0:
        # print("group's group list is empty, return False")
        return False
    
    else:
        
        # print("group.name = {}".format(group.get_name()))
        # print("Descend into Group's group at a time, group_list: {}".format(group.get_groups()))
        if grp_queue is None:
            grp_queue = group.get_groups()
            return is_user_in_group(user, group, grp_queue)

        else:
            grp_queue += group.get_groups()  
            return is_user_in_group(user, grp_queue.pop(0), grp_queue)

if __name__ == "__main__":                  
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)