import urllib2

print 'fetching google ...'
fh = urllib2.urlopen('https://www.google.com/')
data = fh.read()
print data[:100]
