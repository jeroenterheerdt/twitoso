# Twitoso
Get twitter friends using the API so you can easily find them on Counter.social, assuming they have the same username.

# Instructions
1. Get access to the Twitter API here: https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api. Follow the instructions and collect the following info for your app: API Key and Secret, Access Token and Secret.
2. Enter the values collected in step 1 in the python file.
3. Run the python script passing in your username or a list of usernames. Note that Tweepy is a required module (`pip install requirements.txt`).
4. Go to https://counter.social/settings/import and make the following selections:
    - Import type: Following list
    - Select 'Merge'
    - Pick the friends.csv that was created after you ran the script.
    - Click upload.
5. Be patient. You will automatically follow any user on CoSo with the same username as they had on Twitter.