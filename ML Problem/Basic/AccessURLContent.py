import urllib.request
class URLContent:
    def urlContent(self,url):
        return urllib.request.urlopen(url)

u = URLContent()
print(u.urlContent('https://google.co.in'))
print(u.urlContent('https://github.com/Dewanshurahul'))