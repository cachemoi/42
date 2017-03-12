from fake_useragent import UserAgent

ua = UserAgent()
HEADERS_LIST = [ua.chrome, ua.google, ua['google chrome'], ua.firefox, ua.ff]

print(type(HEADERS_LIST[0]))
print(HEADERS_LIST)