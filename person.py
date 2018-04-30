from collections import Counter

class Person:
  def __init__(self, name):
    self.name = name
    self.scheduled = []

  def __str__(self):
    return self.name
