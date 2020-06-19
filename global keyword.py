#global keyword

def spam1() :                                                            #define function
    eggs = "cheesy eggs"                                             # declare eggs local
    global meat                                                     #declare variable as global in scope
    meat = "ham"                                                 # meat locally defined  

def spam2() :                                                            #define function
    global eggs                                                          # use keyword global to change eggs in main program
    eggs = "green eggs"                                             # declare eggs
    meat = "pork patty"                                                 # meat locally defined

eggs = "eggs"                                                       # eggs declared globally in main program (main used from C++/Java)
meat = "bacon"                                                      # meat defined globally

print("global eggs & meat before any spam functions run = " + eggs + " and " + meat)               
spam1()                            
print("global eggs & meat after spam1 function run = "+ eggs + " and " + meat)       
spam2()                                                                          
print("global eggs & meat after spam2 function run = " + eggs + " and " + meat)               
