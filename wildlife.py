# wildlife will help generate the Eco and wildlife of a given planet
#
# it will NOT generate the images of the wildlife but helps give a baseline of what the 
# Eco will look like.
#
#

#imports
import random
import array

#Start of creating Eco system

#Rolls the floral Profile of the plant
def floralProfile():
    baseProfileRoll = random.randint(1,10)
    switch = {
        1: "Diffuse Flora",
        2: "Small Flora",
        3: "Small Flora",
        4: "Small Flora",
        5: "Large Flora",
        6: "Large Flora",
        7: "Large Flora",
        8: "Large Flora",
        9: "Massive Flora",
        10: "Massive Flora",
    }
    return switch.get(baseProfileRoll)

#Gets the type the plant
def floraType():
    baseFTypeRoll = random.randint(1,10)
    switch = {
        1: "Passive Trap",
        2: "Passive Trap",
        3: "Passive Trap",
        4: "Active Trap",
        5: "Active Trap",
        6: "Active Trap",
        7: "Combatant",
        8: "Combatant",
        9: "Combatant",
        10: "Combatant",
    }
    return switch.get(baseFTypeRoll)

#The GM makes two rolls
#on the appropriate section for the Flora Type (Passive, Active, or
#Combatant), and one roll on the section that matches the type of
#world the flora exists on (Death, Jungle, Ocean, or Temperate). If
#the world or environment to which the flora strain is native does
#not correspond to any of the tables, roll on the Temperate World
#Species Traits section. Species from Death Worlds roll twice on the
#Death World Traits section and apply the results of both rolls.
#At the GM discretion, a highly evolved or unusual specimen
#may be granted a free roll on the Exotic Species section.
#aits
#Dice Roll (1d10) Species Trait
#1 Armoured
#2 Deterrent
#3 Frictionless
#4 Sticky
#5-6 Foul Aura (Soporific)
#7-8 Foul Aura (Toxic)
#9 Resilient
#10 Roll on the Exotic Species Traits
#section of this table. 

def TempWorldTrait():
    TempTraitRoll = random.randint(1,10)
    switch = {
        1: "Armoured",
        2: "Venomous",
        3: "Stealthy",
        4: "Deterrent",
        5: "Deterrent",
        6: "Foul Aura (Soporific)",
        7: "Foul Aura (Toxic)",
        8: "Projectile Attack",
        9: "Resilient",
        10: "Resilient",
    }
    return switch.get(TempTraitRoll)

def JungleWorldSpeciesTrait(Type):
    while True:
        JungleTraitRoll = random.randint(1, 10)

        match JungleTraitRoll:
            case 1:  # Deterrent
                return "Deterrent"
            case 2:  # Stealthy
                return "Stealthy"
            case 3 | 4:  # Flexible
                return "Flexible"
            case 5 | 6:  # Foul Aura (Soporific)
                return "Foul Aura (Soporific)"
            case 7 | 8:  # Foul Aura (Toxic)
                return "Foul Aura (Toxic)"
            case 9:  # Paralytic
                if Type == "Passive Trap":
                    continue  # Re-roll if it's a PassiveTrap
                return "Paralytic"
            case 10:  # Venomous
                if Type == "Passive Trap":
                    continue  # Re-roll if it's a PassiveTrap
                return "Venomous"

#Find what re-roll means
def OceanWorldTrait(Type):
    while True:
        OceanTraitRoll = random.randint(1, 10)

        match OceanTraitRoll:
            case 1 | 2:  # Deterrent
                return "Deterrent"
            case 3:  # Disturbing
                return "Disturbing"
            case 4:  # Paralytic
                if Type == "Passive Trap":
                    continue  # Re-roll if it's a PassiveTrap
                return "Paralytic"
            case 5 | 6:  # Projectile Attack
                return "Projectile Attack"
            case 7 | 8 | 9:  # Uprooted Movement
                if "trap" in Type.lower():
                    continue  # Re-roll if Type contains "Trap"
                return "Uprooted Movement"
            case 10:  # Venomous
                if Type == "Passive Trap":
                    continue  # Re-roll if it's a PassiveTrap
                return "Venomous"

def ExoticSpeciesTrait():
    ExoticTraitRoll = random.randint(1,10)
    switch = {
        1: "Disturbing",
        2: "Disturbing",
        3: "Lethal Defenses",
        4: "Silicate",
        5: "Silicate",
        6: "Fade-kind",
        7: "Fade-kind",
        8: "Unkillable",
        9: "Unkillable",
        10: "Warped",
    }
    return switch.get(ExoticTraitRoll)

def DeathSpeciesTrait(Type):
    while True:
        DeathTraitRoll = random.randint(1, 10)

        match DeathTraitRoll:
            case 1 | 2:  # Armoured
                return "Armoured"
            case 3:  # Deadly
                if Type == "Passive Trap":
                    continue  # Re-roll if it's a PassiveTrap
                return "Deadly"
            case 4:  # Deterrent
                return "Deterrent"
            case 5:  # Disturbing
                return "Disturbing"
            case 6:  # Mighty
                if Type == "Passive Trap":
                    continue  # Re-roll if it's a PassiveTrap
                return "Mighty"
            case 7:  # Resilient
                return "Resilient"
            case 8:  # Unkillable
                return "Unkillable"
            case 9:  # Lethal Defenses
                return "Lethal Defenses"
            case 10:  # Uprooted Movement
                if Type == "Passive Trap":
                    continue  # Re-roll if it's a PassiveTrap
                return "Uprooted Movement"

def CombatantSpeciesTrait():
    CombatantTraitRoll = random.randint(1,10)
    switch = {
        1: "Armoured",
        2: "Deadly",
        3: "Venomous",
        4: "Deterrent",
        5: "Mighty",
        6: "Projectile Attack",
        7: "Resilient",
        8: "Resilient",
        9: "Uprooted Movement",
        10: ExoticSpeciesTrait(),
    }
    return switch.get(CombatantTraitRoll)

def PassiveTrapTrait():
    PassiveTraitRoll = random.randint(1,10)
    switch = {
        1: "Armoured",
        2: "Deterrent",
        3: "Frictionless",
        4: "Sticky",
        5: "Foul Aura (Soporific)",
        6: "Foul Aura (Soporific)",
        7: "Foul Aura (Toxic)",
        8: "Foul Aura (Toxic)",
        9: "Resilient",
        10: ExoticSpeciesTrait(),
    }
    return switch.get(PassiveTraitRoll)

def ActiveTrapTrait():
    ActiveTrapRoll = random.randint (1,10)
    switch = {
        1: "Armoured",
        2: "Deadly",
        3: "Flexible",
        4: "Mighty",
        5: "Sticky",
        6: "Paralytic",
        7: "Resilient",
        8: "Resilient",
        9: "Venomous",
        10: ExoticSpeciesTrait(), 
    }
    return switch.get(ActiveTrapRoll)

def floraSpeciesTraits(Type, worldType): 
    WorldTrait = []
    SpeciesTrait = []
    #Collects World species traits
    if (worldType == "Death World"):
        WorldTrait.append(DeathSpeciesTrait(Type))
        WorldTrait.append(DeathSpeciesTrait(Type))
    elif (worldType == "Jungle World"):
        WorldTrait.append(JungleWorldSpeciesTrait(Type))
    elif (worldType == "Ocean World"):
        WorldTrait.append(OceanWorldTrait(Type)) 
    else:
        WorldTrait.append(TempWorldTrait())
    #Collects Species traits
    if (Type == "Passive Trap"):
        SpeciesTrait.append(PassiveTrapTrait()) 
        SpeciesTrait.append(PassiveTrapTrait())
    elif (Type == "Active Trap"):
        SpeciesTrait.append(ActiveTrapTrait()) 
        SpeciesTrait.append(ActiveTrapTrait()) 
    else:
        SpeciesTrait.append(CombatantSpeciesTrait())
        SpeciesTrait.append(CombatantSpeciesTrait()) 
    return print("World Traits: ", ", ".join(WorldTrait), "\nSpecies Traits: ", ", ".join(SpeciesTrait))
    
def faunaBase():
    faunaBaseRoll = random.randint(1,10)
    switch = {
        1: "Avian Beast"
        ,2: "Avian Beast",
        3: "Herd Beast",
        4: "Herd Beast",
        5: "Herd Beast",
        6: "Predator",
        7: "Predator",
        8: "Scavenger",
        9: "Scavenger",
        10: "Verminous Swarm",
    }
    return switch.get(faunaBaseRoll)

#Note VERMINOUS SWARM DOES NOT USE COMMENTED OUT STAT INCREASES
def faunaSize(Base):
    if (Base == "Verminous Swarm"):
        faunaSizeRoll = random.randint(5,10)
    else:
        faunaSizeRoll = random.randint(1,10)
    switch = {
        1: "Miniscule", #–25 to Strength and Toughness, –10 Wounds (minimum of 3) before Species Traits
        2: "Puny", #–20 to Strength and Toughness, –10 Wounds
        3: "Scrawny", # –10 to Strength and Toughness, –5 Wounds
        4: "Scrawny", # –10 to Strength and Toughness, –5 Wounds
        5: "Average", #No modifiers
        6: "Average", #No modifiers
        7: "Hulking", #+5 to Strength and Toughness, –5 to Agility, +5 Wounds
        8: "Hulking", #+5 to Strength and Toughness, –5 to Agility, +5 Wounds
        9: "Enormous", #+10 to Strength and Toughness, –10 to Agility, +10 Wounds 
        10: "Massive", #+20 to Strength and Toughness, –20 to Agility, +20 Wounds
    }
    return switch.get(faunaSizeRoll)
        
              
           
def ExoticBeastTrait():
    ExoticBeastTraitRoll = random.randint(1,10)
    switch = {
        1: "Amorphous",
        2: "Darkling",
        3: "Disturbing",
        4: "Fade-Kind",
        5: "Gestalt",
        6: "Silicate",
        7: "Sustained Life",
        8: "Lethal Defenses",
        9: "Unkillable",
        10: "Warped",
    }
    return switch.get(ExoticBeastTraitRoll)

def AvianTrait():
    AvianTraitRoll = random.randint(1,10)
    switch = {
        1: "Deadly", 
        2: "Deadly", 
        3: "Deadly", 
        4: "Flexible",
        5: "Projectile Attack", 
        6: "Projectile Attack", 
        7: "Stealthy", 
        8: "Sustained Life", 
        9: "Swift",
        10: ExoticBeastTrait(),
    }
    return switch.get(AvianTraitRoll)

def HerdBeastTrait():
    HerdBeastRoll = random.randint(1,10)
    switch = {
        1: "Armoured",
        2: "Armoured",
        3: "Deterrent", 
        4: "Lethal Defences", 
        5: "Mighty",
        6: "Resilient",
        7: "Resilient",
        8: "Swift",
        9: "Swift",
        10: ExoticBeastTrait(),
    }
    return switch.get(HerdBeastRoll)

def PredatorBeastTrait():
    PredatorBeastRoll = random.randint(1,10)
    switch = {
        1: "Apex", 
        2: "Armoured",
        3: "Deadly",
        4: "Deadly", 
        5: "Mighty", 
        6: "Paralytic OR Venomous (GM’s choice)", 
        7: "Projectile Attack", 
        8: "Stealthy", 
        9: "Swift",
        10: ExoticBeastTrait(),
    }
    return switch.get(PredatorBeastRoll)

def ScavengerBeastTrait():
    ScavengerBaestRoll = random.randint(1,10)
    switch = {
        1: "Crawler", 
        2: "Darkling",
        3: "Deadly", 
        4: "Deadly", 
        5: "Deathdweller", 
        6: "Disturbing",
        7: "Flexible", 
        8: "Stealthy", 
        9: "Swift",
        10: ExoticBeastTrait(),
    }
    return switch.get(ScavengerBaestRoll)

def VerminSwarmTrait():
    VerminSwarmRoll = random.randint(1,10)
    switch = {
        1: "Crawler", 
        2: "Darkling",
        3: "Deadly", 
        4: "Deadly", 
        5: "Deathdweller",
        6: "Deterrent",
        7: "Deterrent",
        8: "Disturbing",
        9: "Disturbing",
        10: ExoticBeastTrait(),
    }
    return switch.get(VerminSwarmRoll)

def DeathBeastTrait():
    DeathBeastRoll = random.randint(1,10)
    switch = {
        1: "Apex", 
        2: "Armoured", 
        3: "Deadly",
        4: "Deathdweller", 
        5: "Disturbing", 
        6: "Lethal Defences", 
        7: "Mighty", 
        8: "Resilient", 
        9: "Swift",
        10: "Unkillable",
    }
    return switch.get(DeathBeastRoll)

def DesertBeastTrait():
    DesertBeastRoll = random.randint(1,10)
    switch = {
        1: "Crawler", 
        2: "Thermal Adaptation (Cold)",        
        3: "Deathdweller", 
        4: "Deathdweller",
        5: "Tunneller",
        6: "Tunneller",
        7: "Thermal Adaptation (Heat)",
        8: "Thermal Adaptation (Heat)",
        9: "Thermal Adaptation (Heat)",
        10: "Thermal Adaptation (Heat)",
    }
    return switch.get(DesertBeastRoll)

def IceBeastTrait():
    IceBeastRoll = random.randint(1,10)
    switch = {
        1: "Darkling",
        2: "Deathdweller",
        3: "Deathdweller",  
        4: "Silicate",
        5: "Thermal Adaptation (Cold)",
        6: "Thermal Adaptation (Cold)",
        7: "Thermal Adaptation (Cold)",
        8: "Thermal Adaptation (Cold)",
        9: "Thermal Adaptation (Cold)",
        10: "Tunneller",
    }
    return switch.get(IceBeastRoll)

def JungleBeastTrait():
    JungleBeastRoll = random.randint(1,10)
    switch = {
        1: "Amphibious",
        2: "Amphibious",
        3: "Arboreal",
        4: "Arboreal",
        5: "Arboreal",
        6: "Crawler",
        7: "Crawler", 
        8: "Paralytic", 
        9: "Stealthy",
        10: "Venomous",
    }
    return switch.get(JungleBeastRoll)

def OceanBeastTrait():
    OceanBeastRoll = random.randint(1,10)
    switch = {
        1: "Amphibious",
        2: "Amphibious",
        3: "Amphibious",
        4: "Amphibious",
        5: "Amphibious",
        6: "Aquatic",
        7: "Aquatic",
        8: "Aquatic",
        9: "Aquatic",
        10: "Aquatic",
    }
    return switch.get(OceanBeastRoll)

def TemperateBeastTrait():
    TemperateBeastRoll = random.randint(1,10)
    switch = {
        1: "Amphibious", 
        2: "Aquatic", 
        3: "Arboreal", 
        4: "Armoured", 
        5: "Crawler", 
        6: "Mighty", 
        7: "Resilient", 
        8: "Stealthy", 
        9: "Swift",        
        10: ExoticBeastTrait(),
    }
    return switch.get(TemperateBeastRoll)

def VolcanicBeastTrait():
    VolcanicBeastRoll = random.randint(1,10)
    switch = {
        1: "Armoured",
        2: "Deathdweller",
        3: "Deathdweller", 
        4: "Sustained Life",
        5: "Thermal Adaptation (Heat)",
        6: "Thermal Adaptation (Heat)",
        7: "Thermal Adaptation (Heat)",
        8: "Thermal Adaptation (Heat)",
        9: "Thermal Adaptation (Heat)",
        10: "Tunneller",
    }
    return switch.get(VolcanicBeastRoll)

def faunaBeastTraits(Base, WorldType):
    BaseTraits = []
    WorldBeastTraits = []
    #Collects the base Traits
    if (Base == "Avian Beast"):
        BaseTraits.append(AvianTrait())
        BaseTraits.append(AvianTrait())
    elif(Base == "Herd Beast"):
        BaseTraits.append(HerdBeastTrait())
        BaseTraits.append(HerdBeastTrait())
    elif(Base == "Predator"):
        BaseTraits.append(PredatorBeastTrait())
        BaseTraits.append(PredatorBeastTrait())
    elif(Base == "Scavenger"):
        BaseTraits.append(ScavengerBeastTrait())
        BaseTraits.append(ScavengerBeastTrait())
    else: #Verminous Swarm
        BaseTraits.append(VerminSwarmTrait())
        BaseTraits.append(VerminSwarmTrait())
    #Collects the World Beast Traits
    if (WorldType == "Death World"):
        WorldBeastTraits.append(DeathBeastTrait())
        WorldBeastTraits.append(DeathBeastTrait())
    elif(WorldType == "Desert World"):
        WorldBeastTraits.append(DesertBeastTrait())
    elif(WorldType == "Ice World"):
        WorldBeastTraits.append(IceBeastTrait())
    elif(WorldType == "Jungle World"):
        WorldBeastTraits.append(JungleBeastTrait())
    elif(WorldType == "Ocean World"):
        WorldBeastTraits.append(OceanBeastTrait())
    elif(WorldType == "Volcanic World"):
        WorldBeastTraits.append(VolcanicBeastTrait())
    else: #Temperate World
        WorldBeastTraits.append(TemperateBeastTrait())
    return print("World Beast Traits: ", ", ".join(WorldBeastTraits), "\nBase Beast Traits: ", ", ".join(BaseTraits))

def main():
    #print(floralProfile(), floraType(), floraSpeciesTraits(floraType(), "Ocean World"))
    
    #This looks a lot nicer than the previous showing code above
    profile = floralProfile()
    Type = floraType()
    print("Profile: "+ profile +"\nType: " + Type)
    floraSpeciesTraits(Type, "Ocean World")
    print("\n\n\n\n")
    Base = faunaBase()
    Size = faunaSize(Base)
    print("Fauna Base: "+ Base +"\nFauna Size: " + Size)
    faunaBeastTraits(Base, "")

if __name__ == "__main__":
    main()