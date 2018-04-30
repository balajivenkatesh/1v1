import random

from person import Person
from helpers import print_pairs, read_people

people = read_people()

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

i = 1
while i < len(people):
  if len(remove_q) == 0 and len(remove_order) > 0:
    remove_q = list(remove_order)
    print("remove_q reset")
  if len(remove_q) > 0:
    remove_person = remove_q.pop(0)
  else:
    remove_person = Person("none")

  pool = [x for x in people if x.name != remove_person.name]
  random.shuffle(pool)

  j = 0
  break_outer = False
  while j < len(pool):
    if pool[j].has_everybody_scheduled(people):
      pool[j].empty_scheduled()
    if pool[j].has_scheduled(pool[j+1]):
      break_outer = True
      break
    j += 2

  if break_outer:
    remove_q.insert(0, remove_person)
    continue

  print_pairs(i, pool, remove_person)
  print()
  i += 1

print()
