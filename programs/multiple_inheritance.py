class Father:
    def skills(self):
        return ["gardening", "carpentry", "fishing"]
    def hobbies(self):
        return ["reading", "traveling"]
      
class Mother:
    def skills(self):
        return ["cooking", "painting", "gardening"]
      
class Child(Mother, Father):
    pass

c = Child()
print("Child's Skills:", c.skills())  # Will use Mother's skills method due to MRO
print("Child's Hobbies:", c.hobbies()) # Inherited from Father since Mother doesn't have hobbies method