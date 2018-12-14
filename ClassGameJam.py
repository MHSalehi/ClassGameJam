print("\n****************************************************************************************************************\n****************************\tDR DO-MUCH - THE LEGEND OF THE SINISTER SASQUATCH\t****************************\n****************************************************************************************************************")

print("\nYou are Dr. DoMuch, head of the Animal Alliance and famous detective.You awake in your bed with light streaming\nthrough your bedbroom curtains and the chirping of birds outside. You look at the clock next to your bed, it \nreads, '6:58 AM'.")
while True:
    userInput = input("\nWould you like to get up?").lower()
    if userInput not in ["yes", "y"] and userInput not in ["no", "n"]:
        print("You can't do that.")
    if userInput in ["yes", "y"]:
        print("You get up do you morning routine before heading down to the kitchen")
        break
    if userInput in ["no", "n"]:
        print("You lay back to relax a little longer but it isn't long before your alarm begins to ring loudly.")
        break

while True:
    print("You are unable to sleep. What do you do?")
    userInput = input("1) Turn off the alarm\n2) Get up.")
    if userInput not in ["1", "2"]:
            print("You can't do that.")
    if userInput in ["1"]:
        print("Reaching over you to switch off the alarm and lean lie back down again. Just as you eyes begin to close, your \nbedroom door slowly creaks open and you hear the pitter-patter of paws on the floor. A black and white \nborder collie jumps on to your bed and begins nudging you incessantly. Sighing you get up do you morning \nroutine before heading down to the kitchen")
    if userInput in ["2"]:
        print("You get up do you morning routine before heading down to the kitchen")
        break


      #"You receive information that the local zoo has lost one of it's newest additions.")

