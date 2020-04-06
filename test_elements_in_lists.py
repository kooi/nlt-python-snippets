
print("Raadsel 1:",
      "\n Wanneer leefde de oudste persoon ter wereld?")

guess = input() #"TUSSEN GEBOORTE en dood" # input ()
guess_words = []

for g in guess.split():
    guess_words.append(g.lower())

answer_words = ["tussen", "geboorte", "dood"]
incorrect = False

for word in answer_words:
    if word not in guess_words:
        incorrect = True

if incorrect == True:
    print ("Jammer, je hebt het fout geraden,",
           "het antwoord was \n tussen zijn geboorte en zijn dood")
else:
    print ("Goed gedaan, je hebt het geraden.")
    
    
    
