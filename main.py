# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def print_full_name(first_name, last_name):
    print(f"First Name: {first_name}, Last Name: {last_name}")

print_full_name("Adam","Joker")

## Meh so here we are encapsulating something in the functions context
## The function here knows, that the first argument is the first name, and the second one is the last name.

## why is that a problem? Problem 1
print_full_name("Liu", "Jianguo")

## Why is that a problem? Well, because Chinese actually reverse that order. The functions' output is incorret.
class Name:
    first_name: ""
    last_name: ""

def print_full_name_2(n: Name):
    print(f"First Name: {n.first_name}, Last Name: {n.last_name}")


n = Name()
n.first_name = "Jianguo"
n.last_name = "Liu"
print_full_name_2(n)

## Benefit 2: We also reduce tests to being in isolation, but this doesnt work well for that does it?
## Benefit 3: We get less dependencies. eeeh. I like that, but this example isn't good.


## A purely functional example like this one only works, if we push context into the lexial scope.
## Otherwise we need an OOP example to make this really work nicely :-D


## ---------------------------------------------------------------------------------------------------------------------
# Principle 2: The class we used above is fine for principle 1, but has drawbacks, so let's look at them...
#
print(n)
# that's not pretty is it? Because we wrote class ourselves we cannot leverage other functions...
# let's try something different

def create_name(first_name, last_name):
    return {"first_name": first_name, "last_name": last_name}
n = create_name(first_name="Jianguo", last_name="Liu")

print(n)

## that's benefit 1, nice... can you add a field to n? Sure!
n["full_name"] = "Jianguo Liu"
print(n)

# that's even cooler right?

## ---------------------------------------------------------------------------------------------------------------------
# Principle 3: https://docs.python.org/3/library/dataclasses.html nice... concurency & predictable behavior
#

## ---------------------------------------------------------------------------------------------------------------------
# Principle 4: Principle #4: Separate data schema from data representation <= he changed apparently to 4 principles..


# IN my own words I'd say, data-oriented programming makes data a first class citizen. that means..
# 1. separates the data itself from computations on data.
# 2. makes data immutables
# 3. don't look data into objects
# 4. don't look code into objects
# This leads to radically simpler systems, easier to test, easier to understand, easier to develop.
# We have four principles that help us to do this separation completely.

# Maybe rewrite this one? https://github.com/Poseyy/Articles/blob/master/5SkLearnModels/svm.py


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_full_name("Adam","Joker")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
