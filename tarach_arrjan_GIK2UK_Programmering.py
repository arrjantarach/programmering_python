# ***************************************************************** #
#                                                                   #
#   PROGRAMMERING:  INTRODUKTION TILL PYTHON                        #
#                                                                   #
#   Mitt program, av Arrjan Tarach                              #
#                                                                   #
# ***************************************************************** #

# Definerar dictonaries
Earth = {
    "Name" : "Earth",
    "Celestial_Type" : "Planet",
    "Radius" : 6371,
    "Avg_Temp" : 13.8,
}

Mars = {
    "Name" : "Mars",
    "Celestial_Type" : "Planet",
    "Radius" : 4242,
    "Avg_Temp" : 34,
}

Uranus = {
    "Name" : "Uranus",
    "Celestial_Type" : "Planet",
    "Radius" : 2426,
    "Avg_Temp" : 15,
}

Sun = {
    "Name" : "Sun",
    "Celestial_Type" : "Star",
    "Radius" : 141414,
    "Avg_Temp" : 9999,
}

Pluto = {
    "Name" : "Pluto",
    "Celestial_Type" : "Former Planet",
    "Radius" : 17,
    "Avg_Temp" : -5,
}

# Definerar array med alla dictionaries.
planets = [
    Earth,
    Mars,
    Uranus,
    Sun,
    Pluto,
]

# Välkomna Användaren.
print("Welcome to the celestial body index!")
print("Type the name of the planet too see more info about the planet.")
print("Celesital Body List:")

# For loop för att visa användaren vilka himlakroppar som finns
for i in planets:
    print(i["Name"])

# Ta användarens input
data = input();

found_data = False;

# Skriv ut fakta baserat på input i en for loop
for i in planets:
    words = data.lower().split()
    if i["Name"].lower() in words:
        print("\n" + i["Name"] + " Facts:")
        print("Celestial Type: " + i["Celestial_Type"])
        print("Radius: " + str(i["Radius"]) + "Km")
        print("Avergage Temprature: " + str(i["Avg_Temp"]) + "°C")
        found_data = True
        break   

if not found_data:
    print("\nThis index does not contain that celestial body.")


#Iteration 1 data == i["Name"] fungerar men simpelt
#Iteration 2 if i["Name"] in data: för att man ska kunna skriva vad som helst, fungerar men plutonium hade funkat som pluto.
#Iteration 3 if i["Name"].lower() in data.lower(): La till case sensetive fix
#Iteration 4 added words = data.lower().split() so you can type "Tell me about Earth" 