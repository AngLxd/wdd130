print("In order to create your story, you have to enter the following:")

adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ").capitalize()
verb2 = input("verb: ")
verb3 = input("verb: ")

story = (
    f"The other day, it all went wrong. It all started when I saw a very\n"
    f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all\n"
    f"I could think about was {verb2} over and over. Thankfully,\n"
    f"that caused it to stop, but not before it tried to {verb3}\n"
    f"right in front of my family.")

print("\nYour beautiful story is:\n")
print(story)
