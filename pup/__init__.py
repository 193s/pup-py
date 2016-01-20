import json
from subprocess import Popen, PIPE

def raw(text, selectors='', **kwargs):
  v = selectors
  if 'mode' in kwargs:
    v += ' %s{%s}' % (kwargs['mode'], kwargs['attrkey'] if 'attrkey' in kwargs else '')
  args = ['pup'] + ([v] if v != '' else [])
  p = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
  res = p.communicate(text)
  assert  res[1] == '', res[1]
  return res[0].rstrip('\n')

def pup(text, selectors=''):
  return json.loads(raw(text, selectors, mode='json'))

def text(text, selectors=''):
  return raw(text, selectors, mode='text')

def attr(text, selectors, attr):
  return raw(text, selectors, mode='attr', attrkey=attr)

