def getTalk(kind="shout"):

    # We define functions on the fly
    def shout(word="yes"):
        return word.capitalize()+"!"

    def whisper(word="yes") :
        return word.lower()+"..."

    # Then we return one of them
    if kind == "shout":
        # We don't use "()", we are not calling the function,
        # we are returning the function object
        return shout
    else:
        return whisper

# How do you use this strange beast?

# Get the function and assign it to a variable
talk = getTalk()

# You can see that "talk" is here a function object:
print(talk)
#outputs : <function shout at 0xb7ea817c>

# The object is the one returned by the function:
print(talk())
#outputs : Yes!

# And you can even use it directly if you feel wild:
print(getTalk("whisper")())
#outputs : yes...

