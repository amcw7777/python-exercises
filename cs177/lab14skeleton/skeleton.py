#=======================================
#Task-1

class Pet:
    #Implement the constructor Function
    #The constructor function takes 3 arguments.
    #argument-1: self-> refers to the object
    #argument-2: name-> String value which will be assigned to the instance variable "name"
    #argument-3: species-> String value which will be assigned to the instance variable "species"
    def __init__(self, name, species):
        #======Your code goes here======
        #initialise the instance variables "name" and "species".
        self.name = name
        self.species = species


        #======Your code ends here======

    #Implement the getName() function
    #It takes 1 argument.
    #argument-1: self-> refers to the object    
    def getName(self):
        return self.name
        #======Your code goes here======
        #return the instance variable "name"


        #=======Your code ends here======


    #Implement the getSpecies() function
    #It takes 1 argument
    #argument-1: self-> refers to the object
    def getSpecies(self):
        return self.species
        #======Your code goes here======
        #return the instance variable "species"

        #======Your code ends here======

    def sound(self):
        print("I make generic sound")

#=============================================
#Task-2

class Dog(Pet):
    #Implement the constructor function.
    #It takes 3 arguments.
    #argument-1: self->refers to the object
    #argument-2: name->String value which will be used to initialise the inherited instance variable "name"
    #argument-3: breed->String value which will be used to initialise the instance variable "breed"
    def __init__(self, name, breed):
        Pet.__init__(self,name,'Dog')
        self.breed = breed
        #=====Your code starts here=======
        #call the contructor function of the base class and initialise the instance variable "name" with the argument passed.
        #initialise the inherited instance variable "species" as "Dog."
        #initialise the instance variable "breed"
        

        #======Your code ends here========

    #Implement the getBreed() function
    #It takes 1 argument
    #argument-1 : self-> refers to the object
    def getBreed(self):
        return self.breed
        #return the instance variable "breed"


    #Implement the sound function
    #It takes 1 argument.
    #argument-1: self->refers to the object 
    def sound(self):
        #Override the sound() function by printing-> "I make Bark sound"
        print ("I make Bark sound")
    
        
#===============================================
#Task-3
        

class Cat(Pet):
    #Implement the constructor function.
    #It takes 3 arguments.
    #argument-1: self->refers to the object
    #argument-2: name->String value which will be used to initialise the inherited instance variable "name"
    #argument-3: hasWhiskers->Boolean value which will be used to initialise the instance variable "hasWhiskers"
    def __init__(self, name, hasWhiskers):
        #=====Your code starts here=======
        #call the contructor function of the base class and initialise the instance variable "name" with the argument passed.
        #initialise the inherited instance variable "species" as "Cat"
        #initialise the instance variable "hasWhiskers"
        Pet.__init__(self,name,"Cat")
        self.hasWhiskers = hasWhiskers
        

        #======Your code ends here========
    
    #Implement the gethasWhiskers() function
    #It takes 1 argument
    #argument-1 : self-> refers to the object
    def gethasWhiskers(self):
        #return the instance variable "hasWhiskers"
        return self.hasWhiskers

    #Implement the sound function
    #It takes 1 argument.
    #argument-1: self->refers to the object 
    def sound(self):
        #Override the sound() function by printing-> "I make Meow sound"
        print ("I make Meow sound")
        


#=============================================================




