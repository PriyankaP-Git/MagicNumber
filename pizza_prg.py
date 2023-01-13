
def display(collection):
    nb_pizza=len(collection)
    if nb_pizza == 0:
        print ("No Pizza")
        return

    print(f"-----------PIZZA({nb_pizza})------------")
    for i in collection:
            print(i)
    print()
    print ("First Pizza: " + collection[0])
    print ("Last Pizza: " + collection[-1])

def add_user_pizza(collection):
    p = input("Add Your Pizza: ")
    if pizza_exists(p.lower(), collection):
        print ("ERROR: This Pizza already exists")
    else:
        collection.append(p)

def pizza_exists(e, collection):
    for i in collection:
        if e == i:
            return True
    return False

pizza = ["cheese", "chicken", "pepproni", "veggie", "meat"]

add_user_pizza(pizza)

display(pizza)