import vk

session = vk.Session(
    access_token="token")
vk_api = vk.API(session)
user = vk_api.users.get(user_id=82770450, v=5.0)[0]
print(user['first_name'], user['last_name'], "\n")
groups = vk_api.groups.get(user_id=82770450, v=5.0, extended=1)
for group in groups['items']:
    print(group['name'])
