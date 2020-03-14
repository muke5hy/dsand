class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []      # list of class Groups
        self.users = []       # list of string user

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self,user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    
def is_user_in_group(user, group, grp_queue = None):

    group_queue = []
    
    if not user:
        print(f"No user to look for! {user}")
        return False
    
    if not isinstance(group, Group):
        return False
    
    # Match user to group's name
    if user == group.get_name():
        return True
    elif user in group.get_users():
        return True
    if len(group.get_groups()) == 0:
        return False
    
    else:
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
    
    print(is_user_in_group("sub_child_user", parent))
    print(is_user_in_group("sub_child_user2", parent))
    print(is_user_in_group("", child))