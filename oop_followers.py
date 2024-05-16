# Create user class and blueprint for class objects
class Users:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Create two objects
user1 = Users(2345, "Timmy")
print(f"{user1.username} has ", user1.followers, " number of followers")

user2 = Users(2377, "Samantha")
print(f"{user2.username} also has ", user2.followers, " number of followers")

# Have user1 follow user2
user1.follow(user2)
print(f"{user1.username} now has", user1.followers, " number of followers")
print(f"{user1.username} now follows ", user1.following, "people")
