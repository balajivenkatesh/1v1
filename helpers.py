from person import Person
import sys

def read_people():
  try:
    with open("people.csv") as f:
      for line in f:
        names = line.rstrip().split(",")
        names.sort()
        people = [Person(name) for name in names]
  except Exception as e:
    print(type(e), e)
    sys.exit(0)

  return people

def print_pairs(i, pool, remove_person):
  while len(pool) > 0:
    g = pool[:2]
    g[0].add_scheduled(g[1])
    g[1].add_scheduled(g[0])
    print(str(i) + ", " + g[0].name + ", " + g[1].name + ", " + remove_person.name)
    pool = pool[2:]