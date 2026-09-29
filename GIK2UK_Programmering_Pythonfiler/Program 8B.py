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
#   Nu närmar vi oss slutet! Jämfört med förra programmet lägger    #
#   vi in en if-sats. Lös några "HÄR_SAKNAS_NÅGOT" med hjälp av     #
#   tidigare filer.                                                 #
#                                                                   #
# ***************************************************************** #


# Vi skapar en array med namnen på söta havsdjur.
HÄR_SAKNAS_NÅGOT

# Vi definierar tre Dictionary:s.
HÄR_SAKNAS_NÅGOT

# Vi ställer en ja-/nej-fråga till användaren, och läser in svaret:
print()
print("Vill du lära dig om havets djur? Svara J eller N.")
userResponse = input()
print()

# Med hjälp av en if-/else-sats väljer vi väg beroende på användarens svar:
if userResponse == "J":
    for cuteAnimal in cuteAnimals:
        # Vi hämtar ut fakta, färg, m.m. ur våra Dictionary:s, och skriver ut detta:
        HÄR_SAKNAS_NÅGOT
else:
    print("Då ska jag inte tråka ut dig med fakta!")

# Avslutande utskrift.
print()
print("Hej då, simma lugnt!")
print()
