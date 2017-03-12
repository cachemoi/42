import http.client, urllib.request, urllib.parse, urllib.error, base64
import json, csv, datetime, math

headers = {
  # Request headers
  'Content-Type': 'application/json',
  'Ocp-Apim-Subscription-Key': 'f6e3b66e22214112ace5bff3b6a22ad2'
  # 'Ocp-Apim-Subscription-Key': 'ee2b64ff7dc8401c98d54b2fc90b5455'
}

params = urllib.parse.urlencode({
})

documents = []
times = []

def sentiment(inputcsvFileName, outputcsvfilename):
  with open(inputcsvFileName, newline='') as csvfile:
    r = csv.DictReader(csvfile)
    i = 0
    for row in r:
      documents.append({ 'id': i, 'text': row['content'] })
      t = datetime.datetime.strptime(row['time'], '%Y-%m-%d %H:%M:%S').timestamp()
      times.append(math.floor(t/86400)*86400)
      i += 1

  js = []
  n = 0
  while n < len(documents):
    print(n)
    body = json.dumps({'documents': documents[n:n+500]})
    n += 500
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

  with open(outputcsvfilename, 'w') as csvfile:
    fieldnames = ['id', 'timestamp', 'score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in js:
      i = int(row['id'])
      writer.writerow({ 'id': i, 'timestamp': times[i], 'score': row['score'] })
