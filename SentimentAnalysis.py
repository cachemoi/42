import http.client, urllib.request, urllib.parse, urllib.error, base64
import json, csv

headers = {
  # Request headers
  'Content-Type': 'application/json',
  'Ocp-Apim-Subscription-Key': 'f6e3b66e22214112ace5bff3b6a22ad2'
}

params = urllib.parse.urlencode({
})

documents = []
tts = []

with open('realDonaldTrump_tweets.csv', newline='') as csvfile:
  r = csv.DictReader(csvfile)
  i = 0
  for row in r:
    documents.append({ 'id': i, 'text': row['content'] })
    tts.append({ 'tweetID': row['tweetID'], 'timestamp': row['date'] })
    i += 1

body = json.dumps({'documents': documents})


j = None

try:
  conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
  conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, body, headers)
  response = conn.getresponse()
  data = response.read()
  conn.close()
  print(body)
  print(data)
  j = json.loads(data.decode("utf-8"))
except Exception as e:
  print("[Errno {0}] {1}".format(e.errno, e.strerror))



with open('sentiment.csv', 'w') as csvfile:
  fieldnames = ['tweetID', 'timestamp', 'score']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  for row in j['documents']:
    i = int(row['id'])
    writer.writerow({ 'tweetID': tts[i]['tweetID'], 'timestamp': tts[i]['timestamp'], 'score': row['score'] })
