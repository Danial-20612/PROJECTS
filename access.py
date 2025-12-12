# step 1 create users
roles_permissions = {
    "admin": ["create" , "read","update", "delete"],
    "editor": ["create", "read", "update"],
    "viewer": ["read"],
    "auditor":["read" , "log"]
}

# step 2
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def has_permission(self, action):
        return action in roles_permissions.get(self.role, [])

# step 3 create users
users = [
    User("Alice", "admin"),
    User("Bob", "editor"),
    User("Carol", "viewer"),
    User("Danial", "auditor")
]

# step 4: simulate access control
def access_resource(users, action): #
    if user.has_permission(action):
        print(f"{user.username} ({user.role}) is allowed to {action}.")
    else:
        print(f"{user.username} ({user.role}) is NOT allowed to {action}.")
    
# step 5: test the system
for user in users:
    for action in ["create" , "read", "update" ,"delete", "auditor" , "log"]:
        access_resource(user , action)
    print("-" * 40)

# tasks
print("Welcome to the RBAC Simulation CLI: ")
response = input("Enter your username: ")
if response == "Alice":
    print("Good morning:", response ,"Your responsibilities are" ,roles_permissions["admin"])
elif response == "Danial":
    print("Good morning Danial:"  ,"Your responsibilities are" ,roles_permissions["auditor"])
    



