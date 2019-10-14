import http.client
from html.parser import HTMLParser

city = input('Введите город:')

conn = http.client.HTTPSConnection("yandex.ru")
conn.request('GET','/pogoda/'+city)
res = conn.getresponse()
print(res.status, res.reason)
page = res.read().decode('utf-8')
currentTemp = 0

class MyHTMLParser(HTMLParser):
    tempvalue = False
    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            for attr in attrs:
                if (attr[0] == 'class') and (attr[1] == 'temp__value'):
                    self.tempvalue = True

    #def handle_endtag(self, tag):
    #   print("Encountered an end tag :", tag)

    def handle_data(self, data):
          if self.tempvalue:
              print(data)
              self.tempvalue = False
parser = MyHTMLParser()
parser.feed(page)