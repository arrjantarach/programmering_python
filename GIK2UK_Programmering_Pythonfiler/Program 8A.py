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
#   Vi bygger ihop allt vi lärt oss i Steg 1-7. Vi skapar en array  #
#   med havsdjur, som vi loopar igenom med en for-loop.             #
#   För varje varv i loopen, d.v.s. för varje havsdjur i arrayen,   #
#   skriver vi ut fakta, färg och storlek.                          #
#                                                                   #
# ***************************************************************** #


# UPPGIFT:  Utifrån kommentarerna, lös alla "HÄR_SAKNAS_NÅGOT".

# Vi skapar en array med namnen på söta havsdjur (se programmen i Steg 4).
cuteAnimals = HÄR_SAKNAS_NÅGOT

# Vi definierar tre Dictionary:s (se programmen i Steg 7).
cuteAnimalsFacts = HÄR_SAKNAS_NÅGOT
cuteAnimalsColors = HÄR_SAKNAS_NÅGOT
cuteAnimalsSizes =HÄR_SAKNAS_NÅGOT

# Och här, för varje varv i loopen skriver vi ut fakta, färg och storlek.
# UPPGIFT:          Gör vad du kan för att snygga till utskriften.
# EXTRA UPPGIFT:    Gör utskrifter ännu snyggare genom att separera
#                   stegen då en sträng byggs ihop (inuti for-loopen) 
#                   respektive skrivs ut (efter loopen), ungefär som i
#                   Program 5E.
for cuteAnimal in cuteAnimals:
    # Vi hämtar ut fakta, färg, m.m. ur våra Dictionary:s:
    animalFact = cuteAnimalsFacts[cuteAnimal]
    animalColor = cuteAnimalsColors[HÄR_SAKNAS_NÅGOT]
    animalSize = HÄR_SAKNAS_NÅGOT
    # Och så gör vi en utskrift av detta:
    HÄR_SAKNAS_NÅGOT
