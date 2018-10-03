# 'Week 1 Assignment standard in and out.py' isn't a very standard file name
# Go for something without spaces and probably shorter and easier to remember lol
# Like 'week-1.py' would be fine

print('Lei Meis weekly assignment Standard in and out')
# already mentioned it to you, but ' or " can be used to make strings - just make sure they're used in pairs:
# 'this is a string' and "this is a string" are fine, 'like this" will throw an error
# to use apostrophes in strings, use double quotation marks outside the string, apostrophes inside:
print("This should use the ' like nothing's a problem")
print('01/10/2018')

print('Hello I am fruit shop')

customer=input("What is your name?: ") #not sure how to include ' in the I'll part as it closes my print
# for prettier looking code, please space separate variables and their assignment:
customer = input("What's your name:")

print("Hello", customer, "what fruit would you like to buy?") #how do I put a comma after the Hello Lei Mei, what etc..
# this will end up printing "Hellonamewhat fruit would you like to buy?"
# make sure you remember to add spaces yourself:
print("Hello, ", customer, ". What fruit would you like to buy?")
# you can add most if not all punctuation as you would normally, so long as it's in the string quotation marks


fruit=input() #not sure what the difference is between "" and ''
# again for prettier code, space separate.... and not really any difference "" and '':
fruit = input('this is still a string, ', "and so is this")

print ("You have bought:", fruit)
# prettier code -> no spaces between function names and brackets please! And don't forget adding spaces in strings yourself:
print("You have bought: ", fruit)

# so now you've got something that runs once, that means you can only ever buy one fruit.....
# and even then the customer could ask for whatever fruit and the shop would just be like
# cool, yep, we sell that shit, great, here have it...

# Challenges:
# -----------
# 1. Give your fruit shop a list of fruit that it stocks
#     a. If the fruit the customer asks for isn't in the list, say "Nope, we don't have that, sorry."
#     b. If the fruit the customer asks for is in the list, say "Oh, here you go."
# 2. Get your program to run til the customer stops asking for fruit
#     a. If the customer types "nothing" when they get asked for what fruit they want, say "Okay, bye." and close the program
# 3. Keep an inventory of your fruit 
#     a. Take 1 away from the inventory if you're able to sell your customer fruit
#     b. Do that til you hit zero for whatever fruit

