import sys
from skeleton import Pet 
from skeleton import Dog
from skeleton import Cat
def main():
    unit_test_1();
    unit_test_2();

def unit_test_1():
    myPet = Pet("Simba", "Lion")
    print(myPet.getName())
    print(myPet.getSpecies())
    myPet.sound()

def unit_test_2():
    dog1 = Dog("Spike", "Bulldog")
    cat1 = Cat("Tom", True)
    print("The name of dog1 is",dog1.getName())
    print("The species of dog1 is" , dog1.getSpecies())
    print("The breed of", dog1.name, "is", dog1.getBreed())
    dog1.sound()
    print("The name of cat1 is", cat1.getName())
    print("The species of  cat1 is" , cat1.getSpecies())
    print(cat1.name, "has whiskers is", cat1.gethasWhiskers())
    cat1.sound()

main();
