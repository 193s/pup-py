# pup-py
Python wrapper for [pup](https://github.com/ericchiang/pup)

```python
import pup
import requests

x = requests.get('http://example.com').text
print pup.raw(x, 'p') # "<p>\n  This domain is established to..."
print pup.pup(x) # [{u'tag': u''}, {u'tag': u'html'...
print pup.text(x, 'a') # "More information..."
print pup.attr(x, 'a', 'href') # "http://www.iana.org/domains/example"
```
