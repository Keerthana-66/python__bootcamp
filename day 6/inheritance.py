class animal:
    def speak():
        return "animal is speaking"
    #single inheritance
class dog(animal):
        def bark(): 
            return "bow ......"
obj1=animal
obj2=dog
print(obj1.speak())
print(obj2.bark())
######33#multilevel inheritance.py###33333#333
class puppy(dog):
 def puppy_speak():
     return "in puppy "
 obj1=animal
obj2=dog
obj3=puppy
print(obj1.speak())
print(obj2.bark())
print(obj3.puppy_speak())
