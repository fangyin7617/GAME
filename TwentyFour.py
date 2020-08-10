def is_possible(cards):
  for i,card in enumerate(cards):
    if helper(cards[:i]+cards[i+1:], card):
      return True
  return False
  
def helper(candidates, cur):
  # Check the result when cards are all used
  if not candidates and cur == 24:
    return True
  elif not candidates:
    return False
    
# Recursively check every card in the cards
for i, candidate in enumerate(candidates):
  if helper(candidates[:i] + candidates[i + 1:], cur + candidate):
    return True
  if helper(candidates[:i] + candidates[i + 1:], cur - candidate):
    return True
  if helper(candidates[:i] + candidates[i + 1:], cur * candidate):
    return True

return False
