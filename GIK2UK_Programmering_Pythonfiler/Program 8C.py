# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Steg 8.  Vi knyter ihop alltsammans:                            #
#            * Variabler, strängar, exekvering                      #
#            * Input och output från/till användaren,               #
#               funktionsanrop                                      #
#            * Datastrukturerna Array och Dictionary,               #
#            * Iteration med for-loop                               #
#            * Selektion med if                                     #
#                                                                   #
#   Jämfört med förra programmet lägger vi en if-sats               #
#   inuti en for-loop, som i Steg 6. Programmet fungerar bra så     #
#   när som på några "HÄR_SAKNAS_NÅGOT" som du behöver lösa.        #
#                                                                   #
# ***************************************************************** #


# Vi skapar en array med namnen på söta havsdjur.
HÄR_SAKNAS_NÅGOT

# Vi definierar tre Dictionary:s.
HÄR_SAKNAS_NÅGOT

# Vi ställer en fråga till användaren, om vilket djur hen vill lära sig
# mer om, och läser in svaret.
print()
print("Vilket havsdjur vill du lära dig mer om?")
selectedAnimalName = input()

# Med en for-loop stegar vi igenom varje havsdjur i arrayen.
for cuteAnimal in HÄR_SAKNAS_NÅGOT:
    # Med hjälp av en if-/else-sats väljer vi väg beroende på
    # användarens svar:
    if selectedAnimal == cuteAnimal:
        # Vi hämtar ut fakta, färg, m.m. ur våra Dictionary:s som i
        # Steg 7, och skriver ut dessa:
        HÄR_SAKNAS_NÅGOT
    else:
        print("Då ska jag inte tråka ut dig med fakta om" + cuteAnimal)

# Avslutande utskrift.
print()
print("Hej då, simma lugnt!")
print()
