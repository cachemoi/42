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
times = []

def sentiment(csvFileName):
  with open(csvFileName, newline='') as csvfile:
    r = csv.DictReader(csvfile)
    i = 0
    for row in r:
      documents.append({ 'id': i, 'text': row['content'] })
      times.append(row['time'])
      i += 1

  js = []
  n = 0
  while n < len(documents):
    print(n)
    body = json.dumps({'documents': documents[n:n+1000]})
    n += 1000
    j = None
    try:
      conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
      conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, body, headers)
      response = conn.getresponse()
      data = response.read()
      conn.close()
      j = json.loads(data.decode("utf-8"))
      js.extend(j['documents'])
    except Exception as e:
      print("[Errno {0}] {1}".format(e.errno, e.strerror))

  with open('output.csv', 'w') as csvfile:
    fieldnames = ['id', 'timestamp', 'score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in js:
      i = int(row['id'])
      writer.writerow({ 'id': i, 'timestamp': times[i], 'score': row['score'] })
