import requests

API_VERSION = "5.131"
URL_VK = "https://vk.com/"
URL = "https://api.vk.com/method/"


class VkUser2():

    def __init__(self, user_id, screen_name=None, token_file=None):

        self.user_id = user_id

        if token_file:
            with open(token_file, encoding="UTF-8") as f:
                self.token = f.read().strip()
                self.parameters = {
                    "access_token": self.token,
                    "v": API_VERSION,
                }

    def __and__(self, other):
        params = {
            "source_uid": self.user_id,
            "target_uid": other.user_id,
            "count": 5,
        }
        parameters = self.parameters | params

        response = requests.get(URL + "friends.getMutual", params=parameters)
        response.raise_for_status()
        data = response.json()

        result = []
        if data["response"]:
            for friend_id in data["response"]:
                result.append(VkUser2(friend_id))

        return result

    def __str__(self):
        return URL_VK + "id" + str(self.user_id)


class VkParser:

    def __init__(self, token_file):
        with open(token_file, encoding="UTF-8") as f:
            self.token = f.read().strip()
            self.parameters = {
                "access_token": self.token,
                "v": API_VERSION,
            }

    def get_user_by_id(self, user_id, add_params={}):
        parameters = self.parameters | {"user_id": user_id} | add_params
        # parameters1 = {**self.parameters, **{"user_id": user_id}}

        response = requests.get(URL + "users.get", params=parameters)
        response.raise_for_status()
        data = response.json()

        return data["response"]

    def get_user_by_search(self, name, add_params={}):
        parameters = self.parameters | {"q": name, "sort": 0} | add_params

        response = requests.get(URL + "users.search", params=parameters)
        response.raise_for_status()
        data = response.json()

        return data["response"]

    def get_groups(self, query, sort=0):
        params = {
            "q": query,
            "sort": sort,
            "count": 1000,
        }
        parameters = self.parameters | params

        response = requests.get(URL + "groups.search", params=parameters)
        response.raise_for_status()
        data = response.json()

        return data["response"]

    def get_mutual_friends_ids_multiple(self, friend1_id, friends_ids):
        params = {
            "source_uid": friend1_id,
            "target_uid": friends_ids,
            "count": 5,
        }
        # "target_uids": friends_ids,
        parameters = self.parameters | params

        response = requests.get(URL + "friends.getMutual", params=parameters)
        response.raise_for_status()
        data = response.json()

        return data


class VkUser(VkParser):

    def __init__(self, token_file):
        super().__init__(token_file)
        self.user_id = requests.get(URL + "users.get", params=self.parameters).json()["response"][0]["id"]

    def __str__(self):
        result = self.get_user_by_id(self.user_id, {"fields": "screen_name"})
        return URL_VK + result[0]["screen_name"]

    # @property
    # def user_id(self):
    #     """Property of User ID."""
    #     return self.user_id
    #
    # @user_id.setter
    # def user_id(self, value):
    #     self.user_id = value
    #
    # @user_id.deleter
    # def user_id(self):
    #     del self.user_id

    def get_user_groups(self):
        params = {
            "user_id": self.user_id,
            "extended": 1,
        }
        parameters = self.parameters | params

        response = requests.get(URL + "groups.get", params=parameters)
        response.raise_for_status()
        data = response.json()

        return data["response"]

    def get_followers_ids(self):
        params = {
            "user_id": self.user_id,
        }
        parameters = self.parameters | params

        response = requests.get(URL + "users.getFollowers", params=parameters)
        response.raise_for_status()
        data = response.json()

        return data

    def get_followers(self):
        result = {"items": [], "count": 0}

        followers_ids = self.get_followers_ids()["response"]["items"]
        for follower_id in followers_ids:
            user_details = self.get_user_by_id(follower_id)
            result["items"].append(user_details)
            result["count"] += 1

        return result

    def get_friends_online(self):
        # User id is not necessary - by default current user is used!
        params = {
            "user_id": self.user_id,
        }
        parameters = self.parameters | params

        response = requests.get(URL + "friends.getOnline", params=parameters)
        response.raise_for_status()
        data = response.json()

        return data["response"]

    def get_friends_ids(self):
        # User id is not necessary - by default current user is used!
        params = {
            "user_id": self.user_id,
        }
        parameters = self.parameters | params

        response = requests.get(URL + "friends.get", params=parameters)
        response.raise_for_status()
        data = response.json()

        return data

    def get_friends(self):

        result = {"items": [], "count": 0}

        friends_ids = self.get_friends_ids()["response"]["items"]
        for friend_id in friends_ids:
            user_details = self.get_user_by_id(friend_id)
            result["items"].append(user_details)
            result["count"] += 1

        return result

    def get_user_mutual_friends_ids(self, friend):
        # User id is not necessary - by default current user is used!
        params = {
            "source_uid": self.user_id,
            "target_uid": friend,
        }
        parameters = self.parameters | params

        response = requests.get(URL + "friends.getMutual", params=parameters)
        response.raise_for_status()
        data = response.json()

        return data


if __name__ == '__main__':
    # Print mutual friends list:
    # 6492, 2745 are suggested by VK on page https://dev.vk.com/method/friends.getMutual!
    vk_user = VkUser("token.txt")
    result = vk_user.get_mutual_friends_ids_multiple(6492, 2745)
    for friend_id in result["response"]:
        user_info = vk_user.get_user_by_id(friend_id, {"fields": "nickname,city,domain"})
        print(user_info)

    # Print mutual friends list (using class instances):
    vk_user1 = VkUser2(6492, token_file="token.txt")
    vk_user2 = VkUser2(2745, token_file="token.txt")
    mutual_friends_list = vk_user1 & vk_user2
    for user_info in mutual_friends_list:
        # Homepage links printed.
        print(user_info)
