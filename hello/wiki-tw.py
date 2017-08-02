import json, urllib.request, tweepy

# 各種キーをセット
#os.environ.get('TIMES',3)

CONSUMER_KEY = os.environ.get('CONSUMER_KEY',3)
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET',3)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN',3)
ACCESS_SECRET = os.environ.get('ACCESS_SECRET',3)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

# これだけで、Twitter APIをPythonから操作するための準備は完了。

url ='https://ja.wikipedia.org/w/api.php?format=json&utf8&action=query&list=random&rnnamespace=0&rnlimit=1'

r=urllib.request.urlopen(url)
root=json.loads(r.read())

st = 'title:' + root['query']['random'][0]['title']

print(st)

print("\n")

api.update_status(status=st)