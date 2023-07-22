#create a sample of users
users = {'zebby': 'active', 'brian':'inactive', 'japheth':'active', 'mumo':'inactive'}

#Strategy: Iterate over a copy
for user, status in users.copy().items():
    if user == 'inactive':
        del users[user]

#strategy : Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(user)

#find prime and odd number using continue
for num in range(2, 10):
    if num % 2 == 0:
        print("Found a prime number",num)

        continue
    print("Found an odd number",num)
    




