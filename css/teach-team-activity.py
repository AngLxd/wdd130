print('What is the age of the first rider?')
print('What is the height of the first rider?')
choice = input("Is there a second rider? 'yes' or 'no': ").lower()
if choice == "yes":
        second_person()
elif choice == "no":
        result()
else:
    print("Invalid choice. Please type 'yes' or 'no'.")
    def second_person():
            print('What is the age of the second rider?')
            print('What is the height of the second rider?')