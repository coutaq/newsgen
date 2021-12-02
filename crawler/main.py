import vk

session = vk.Session(
    access_token=open("token").readline().strip())
vk_api = vk.API(session)

user_id = 82770450


def user_get(uid):
    return vk_api.users.get(user_id=uid, v=5.131)[0]


def groups_get(uid):
    return vk_api.groups.get(user_id=uid, v=5.131, extended=1)


def friends_get(uid):
    return vk_api.friends.get(user_id=uid, v=5.131, fields="name")


user = user_get(user_id)
print(user['first_name'], user['last_name'], "\n")
groups = groups_get(user_id)
for group in groups['items']:
    print(group['name'])
friends = friends_get(user_id)
print(friends)
for friend in friends['items']:
    print(friend['first_name'], friend['last_name'])