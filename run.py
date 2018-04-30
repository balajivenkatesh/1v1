import random
import sys

from person import Person

try:
  with open("people.csv") as f:
    for line in f:
      names = line.rstrip().split(",")
      names.sort()
      people = [Person(name) for name in names]
except Exception as e:
  print(type(e), e)
  sys.exit(0)

print()
print("people = ", [p.name for p in people])

remove_order = []
if len(people) % 2 == 1:
  remove_order = list(people)
  random.shuffle(remove_order)

print("remove order = ", [p.name for p in remove_order])

print()

print("Week, P1, P2, out")

remove_q = []
for i in range(0, 4):
  if len(remove_q) == 0 and len(remove_order) > 0:
    remove_q = list(remove_order)
  remove_person = remove_q.pop(0)

  pool = [x for x in people if x.name != remove_person.name]
  random.shuffle(pool)

  while len(pool) > 0:
    g = pool[:2]
    print(str(i) + ", " + g[0].name + ", " + g[1].name + ", " + remove_person.name)
    pool = pool[2:]

print()
