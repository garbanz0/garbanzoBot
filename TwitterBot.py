import tweepy 

auth = tweepy.OAuthHandler("aJvgfhDY0Tug8fDibXUL4p0Ef", "D3REz4pXA3W01MX84cFve4xyTHFZzCp7G6VwUsKPZbEKOYEzAC")

auth.set_access_token("1503320325236350981-V5yCqvBoOhJLLBvBtsB0L64NnS0JsO", "yYRXmJqLJsNNhZFpu4VsoWwNKLREM3fG6mvHFVXAgnmNV")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
