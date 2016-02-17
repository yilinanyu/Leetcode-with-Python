import collections

d = collections.defaultdict(int)
for c in thestring:
    d[c] += 1
# A collections.defaultdict is like a dict (subclasses it, actually), but when an entry is sought and not found, instead of reporting it doesn't have it, it makes it and inserts it by calling the supplied 0-argument callable. Most popular are defaultdict(int), for counting (or, equivalently, to make a multiset AKA bag data structure), and defaultdict(list), which does away forever with the need to use .setdefault(akey, []).append(avalue) and similar awkward idioms.

# So once you've done this d is a dict-like container mapping every character to the number of times it appears, and you can emit it any way you like, of course. For example, most-popular character first:

for c in sorted(d, key=d.get, reverse=True):
  print '%s %6d' % (c, d[c])
