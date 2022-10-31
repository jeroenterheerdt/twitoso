from tweepy import OAuthHandler
from tweepy import API
import sys
import io

if __name__ == "__main__": 
    account_list = [] 
    if (len(sys.argv) > 1):
        account_list = sys.argv[1:]

    if len(account_list) < 1:
        print("No parameters supplied. Exiting.")
        sys.exit(0)

    consumer_key="" #API Key
    consumer_secret="" #API Key Secret
    access_token="" #Access Token
    access_token_secret="" #Access Token secret

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = API(auth)

    for target in account_list:
        print("Processing target: " + target)

        # get friends
        friends = auth_api.get_friend_ids(screen_name=target)
        outfile = "friends.csv"
        with io.open(outfile, "w", encoding="utf-8") as file:
            for f in friends:
                u = auth_api.get_user(user_id=f).screen_name
                file.write(u+"\n")
