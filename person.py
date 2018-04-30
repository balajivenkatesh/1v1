from collections import Counter

class Person:
  def __init__(self, name):
    self.name = name
    self.scheduled = []

  def __str__(self):
    return self.name

  def __hash__(self):
    return hash(self.name)

  def __eq__(self, other):
    return other.name == self.name

  def add_scheduled(self, person):
    self.scheduled.append(person)

  def empty_scheduled(self):
    self.scheduled = []

  def has_scheduled(self, person):
    for p in self.scheduled:
      if p.name == person.name:
        return True

    return False

  def has_everybody_scheduled(self, pool):
    return Counter(pool) == Counter(self.scheduled)