
import sys

def pairs(s):
  for c in s:
    for d in s:
      if c<d:
        yield (c, d)

s_len = int(input().strip())
s = list(input().strip())

unique_chars = set(s)
if len(unique_chars) < 2:
  print ('0')
  sys.exit()
  
participation = {}   
pair_status = {}    
for x, y in pairs(unique_chars):
  for c in [x, y]:
    if c in participation:
      participation[c] += [(x,y)]
    else:
      participation[c] = [(x,y)]
  
  pair_status[(x,y)]={'seen':'', 'count':0}

  
for c in s:
  p_list = participation[c]
  for p in p_list:
    if p in pair_status: 
      ps = pair_status[p]
      if ps['seen'] == '' or ps['seen'] != c:
        ps['seen'] = c
        ps['count'] += 1
      else:
        del pair_status[p]

max_length = 0
if len(pair_status) > 0:
  max_length = max( p['count'] for p in pair_status.values() )
print (max_length)


