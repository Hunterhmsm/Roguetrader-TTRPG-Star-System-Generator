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


#Chooses the traits for temperate world flora
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

#Chooses the traits for Jungle floura
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

#Chooses the traits for Ocean floura
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

#Chooses the traits for Exotic Flora
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

#Chooses the traits for Death World Flora
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

#Chooses the traits for Combatent Species flora
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

#Chooses the traits for passive trap flora
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

#Chooses the traits for Active Trap flora
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

#Chooses the traits for Flora
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
    
##Chooses the Base for Beasts
def faunaBase():
    faunaBaseRoll = random.randint(1,10)
    switch = {
        1: "Avian Beast",
        2: "Avian Beast",
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

#Chooses the Size for Beasts
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
        
              
#Chooses the traits for Exotic Beasts           
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

##Chooses the traits for Avian Beasts
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

#Chooses the traits for Herd Beasts
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

#Chooses the traits for Predator Beasts
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

#Chooses the traits for Scavenger Beasts
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

#Chooses the traits for Vermin Swarm beasts 
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

#Chooses the traits for Death world Beasts
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

#Chooses the traits for Desert Beasts
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

#Chooses the traits for Ice Beasts
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

#Chooses the traits for Jungle Beasts
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

#Chooses the traits for Ocean Beasts
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

#Chooses the traits for temperate Beasts
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

##Chooses the traits for Volcanic Beasts
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

#Generates the Traits for the Beasts
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

#Chooses a trait for the Xenos
def PrimitiveXenosDesc():
    PrimitiveXenosRoll = random.randint(1,5)
    switch = {
        1: "Deadly",
        2: "Mighty",
        3: "Resilient",
        4: "Stealthy",
        5: "Swift",
    }
    return switch.get(PrimitiveXenosRoll)

#Chooses what the xenos look like
def XenosMorphology():
    XenosMorphologyRoll = random.randint(1,10)
    switch = {
        1: "Crawler",
        2: "Flyer (6)",
        3: "Hoverer (4)",
        4: "Multiple Arms",
        5: "Quadruped",
        6: "Size (Hulking)",
        7: "Size (Scrawny)",
        8: "Humanoid, Size (Average)",
        9: "Humanoid, Size (Average)",
        10: "Humanoid, Size (Average)",
    }
    return switch.get(XenosMorphologyRoll)

#Chooses the traits for the Xenos
#This is a 1/4 chance to happen on top of Xenos Morphology
def ExoticXenosPhysiology():
    ExoticXeonosRoll = random.randint(1,10)
    switch = {
        1: "Armoured",
        2: "Disturbing",
        3: "Deathdweller",
        4: "Lethal Defences",
        5: "Disturbing",
        6: "Warped",
        7: "Darkling",
        8: "Unkillable",
        9: "Projectile Attack",
        10: "Deterrent",
    }
    return switch.get(ExoticXeonosRoll)

#Chooses the traits for the Xenos
#this is also a 1/4 chance to happen 
def UnusualXenosCom():
    UnusualXenosComRoll = random.randint(1,5)
    switch = {
        1: "Intuitive Communicators", # The xenos race possesses the ability to understand and communicate with the Explorers without prior contact, whether through low-level telepathy, an uncanny ability to intuit body language, or other unusual means. Interaction Skills suffer no penalty, unless the Explorers take issue with this clearly unnatural power.
        2: "Previous Contact", #Certain members of the xenos culture have adequate fluency in Low Gothic to allow use of Interaction Skills without penalties. The question of where they learned the language is likely to be an issue—the only Imperial contact such beings are likely to have had would be a rival Rogue Trader dynasty.
        3: "Relic Civilisation", #The entire race speaks a debased form of Low Gothic, not unlike what a long-separated fragment of pre-Imperial civilisation might use. Mastering the idiosyncrasies of their variant might take a week or two, but unravelling the mystery of their language’s origin could be much more challenging...
        4: "Simplistic", #The language of the xenos is simplicity itself—largely because their civilisation has little use for advanced concepts, and their communication has barely progressed beyond grunting. The language is learned for free after a week of interaction. Communication without fluency in the language treats Interaction Skills as Basic, but does not penalise them. However, even a trained speaker must pass a Speak Language test to get across advanced concepts and metaphors.
        5: "Exotic", #The xenos communicate via elaborate mechanisms impossible to fully duplicate without their unique biology. Pheromones, pigmentation shifts, or body language beyond human physiology to replicate may play a part. Interaction Skills suffer an additional –10 penalty, whether the user trained in the language or not. Characters with the Polyglot Talent also suffer from this penalty, despite their unique abilities.
    }
    return switch.get(UnusualXenosComRoll)

##Chooses the primitive Xenos social sturcture
def PrimitiveXenosSocialStructures():
    PrimitiveXenosSocialRoll = random.randint(1,10)
    switch = {
        1:"Agriculturalist", #The xenos have based their lifestyle around farming crops and herding local fauna. Such societies tend to be stable, if not outright peaceful. While many primitive xenos cultures have the tools to farm, this represents a culture where the herd or crop is the central cultural value. In some xenos cultures, the herd may even be a related species, or degenerate members of their own race.
        2: "Agriculturalist", #The xenos have based their lifestyle around farming crops and herding local fauna. Such societies tend to be stable, if not outright peaceful. While many primitive xenos cultures have the tools to farm, this represents a culture where the herd or crop is the central cultural value. In some xenos cultures, the herd may even be a related species, or degenerate members of their own race.
        3: "Hunter", #This race lives by their prowess in the hunt, supplementing lean seasons with foraging. They may know of agriculture and scorn it as weakness, or even have a physiology not far divorced from the predators they compete with for food. Explorers must take care not to present themselves as potential prey animals when dealing with such a culture.
        4: "Feudal", #The xenos live in a society rigidly defined by oaths of loyalty. This could as easily refer to blood-bonds between feral chieftains as the vows made by vassals of an alien lord aping true Imperial nobility. Such societies are tight-knit, but often divided along multiple lines that can be exploited to gain influence over one lord or another.
        5: "Raiders", #While some section of the xenos culture is devoted to the production or acquisition of food and other necessities, true status in this society belongs to the warriors. Crops grown are valued less than those seized from others, and only strength is respected. A Rogue Trader can easily impress such aliens with his military might, but must be careful not to let himself seem too dependent on his tools or servants.
        6: "Nomadic", #The race is constantly on the move, travelling along with migratory herds, moving from area to area as they exhaust local food supplies or deplete the land, driven to keep roaming perhaps due to local weather conditions. Explorers may find it impossible to deal with them unless they are willing to also move with the tribes.
        7: "Hivemind", #Linked together in a network of pheromones, neurological energies, or some other mechanism, the xenos think and speak with one mind. There are no actual individuals in the race, and their “representative” might change daily as a new member is chosen to interact with the Explorers. This race views the death of a member as nothing more than a mild nuisance, but will also view a slight against one as a slight against them all.
        8: "Scavengers", #The xenos make their living by picking through the ruins of an older civilisation. Whether they dwell amidst a fallen human colony, archeotech ruins, or the remains of a xenos race such as the Egarian Dominion, the end result is that these supposed primitives have access to advanced tools, although they may understand little to nothing about these items. They may trade priceless relics for new kinds of “magic,” for example, or view the intrusion of other advanced races as a sign of an impending apocalypse.
        9: "Xenophobic", #It is possible this race was previously exploited by less benign Explorers, or they may have simply evolved to treat anything but themselves as a deadly threat. They will aggressively attack anyone outside their race or tribe, and it will take extensive patience and peace offerings to even begin attempts at communication.
        10: "Tradition-bound", #Unlike most primitive xenos, the lack of advancement for this culture is not based on youth, but an ancient and established tradition. The hallowed ancestors or ancient edicts of this race forbid diverging from their long-held path. Anything new—like the Explorers—is to be mistrusted.
    }
    return switch.get(PrimitiveXenosSocialRoll)

#Generates a Primitive xenos civilization using the Kornonus Bestairy
def PrimitiveXenosGeneration():
    gamble = random.randint (1,4)
    unusualGamble = random.randint(1,4)
    if (gamble == 4 and unusualGamble == 4):
        return print("Primitive Xenos Desc: ", PrimitiveXenosDesc(), "\nPrimitive Xenos Morphology: ", XenosMorphology(),"\nExotic Xenos Physiology: ", ExoticXenosPhysiology(),"\nUnusual Xenos Communication: ", UnusualXenosCom(),"\nPrimitive Xenos Social Structure: ", PrimitiveXenosSocialStructures())
    elif (gamble == 4):
        return print("Primitive Xenos Desc: ", PrimitiveXenosDesc(), "\nPrimitive Xenos Morphology: ", XenosMorphology(),"\nExotic Xenos Physiology: ", ExoticXenosPhysiology(),"\nPrimitive Xenos Social Structure: ", PrimitiveXenosSocialStructures())
    elif (unusualGamble ==4):
        return print("Primitive Xenos Desc: ", PrimitiveXenosDesc(), "\nPrimitive Xenos Morphology: ", XenosMorphology(),"\nUnusual Xenos Communication: ", UnusualXenosCom(), "\nPrimitive Xenos Social Structure: ", PrimitiveXenosSocialStructures())
    else:
        return print("Primitive Xenos Desc: ", PrimitiveXenosDesc(), "\nPrimitive Xenos Morphology: ", XenosMorphology(),"\nPrimitive Xenos Social Structure: ", PrimitiveXenosSocialStructures())

#Picks which beast type it should be
def BestialArchetypes():
    ArchetypeRoll = random.randint(1,5)
    switch = {
        1: "Apex Predator",
        2: "Behemoth",
        3: "Ptera-Beast",
        4: "Shadowed Stalker",
        5: "Venomous Terror",
    }
    return switch.get(ArchetypeRoll)

#Chooses the traits for Apex Predators
def ApexPredator():
    ApexRoll = random.randint(1,10)
    switch = {
        1: "Adapted",
        2: "Adapted",
        3: "Brute",
        4: "Brute",
        5:"Cunning Stalker",
        6: "Cunning Stalker",
        7: "Killing Machine",
        8: "Living Arsenal",
        9: "Natural Prowess",
        10: "Natural Prowess",
    }
    return switch.get(ApexRoll)

#Chooses the traits for Behemoths
def Behemoths():
    BehemothRoll = random.randint(1,10)
    switch = {
        1: "Beyond Challenge",
        2: "Beyond Challenge",
        3: "Impossible Grace",
        4: "Leviathan",
        5: "Leviathan",
        6: "Megapredator",
        7: "Megapredator",
        8: "Titanborn",
        9: "Unstoppable",
        10: "Unstoppable",
    }
    return switch.get(BehemothRoll)

#Chooses the traits for PteraBeasts
def PteraBeasts():
    PteraRoll = random.randint(1,10)
    switch = {
        1: "Aerial Impossibility",
        2: "Aerial Impossibility",
        3: "Doom Diver",
        4: "Earth-Scorning",
        5: "Earth-Scorning",
        6: "Skyless Flight",
        7: "Swift Flyer",
        8: "Swift Flyer",
        9: "Swift Flyer",
        10: "Wyrdwing",
    }
    return switch.get(PteraRoll)

#Chooses the traits for Shadowed Stalkers
def ShadowedStalkers():
    StalkerRoll = random.randint(1,10)
    switch = {
        1: "Adapted",
        2: "Adapted",
        3: "Chameleonic",
        4: "Chameleonic",
        5: "Deadly Ambusher",
        6: "Deadly Ambusher",
        7: "Lure",
        8: "Shadow-walking",
        9: "Vanisher", 
        10: "Vanisher", 
    }
    return switch.get(StalkerRoll)

#Chooses the traits for Venomous Terrors
def VenomousTerrors():
    TerrorsRoll = random.randint(1,10)
    switch = {
        1: "Deadly Touch",
        2: "Delirium Bringer",
        3: "Toxic Hunter",
        4: "Toxic Hunter",
        5: "Hidden Death",
        6: "Hidden Death",
        7: "Poisonous Presence",
        8: "Poisonous Presence",
        9: "Potent Toxins",
        10: "Potent Toxins",
    }
    return switch.get(TerrorsRoll)

#Creates a Beast using stars of enequity
def BeastGeneration():
    Nature = BestialArchetypes()
    Traits = []
    TraitRoll = random.randint(1,3) #This may not make since it says at least one roll
    while TraitRoll >= 1:
        
        if (Nature == "Apex Predator"):
            Traits.append(ApexPredator())
        elif (Nature == "Behemoth"):
            Traits.append(Behemoths())
        elif (Nature == "Ptera-Beast"):
            Traits.append(PteraBeasts())
        elif (Nature == "Venomous Terror"):
            Traits.append(VenomousTerrors())
        else: #Shadowed Stalkers
            Traits.append(ShadowedStalkers())
        TraitRoll -= 1
    return print("Bestial Archetype: ", Nature, "\nBestial Traits: ", ", ".join(Traits))
    
#Decides which inhabitant civ to create
#possible understanding in place    
#change latter do not understand uninhabitable for orks and kroots
def inhabitants(habit):
    if habit != "Verdant": #Verdant = Habitable planet
        inhabitantRoll = random.randint(1,10)
        while (inhabitantRoll >= 5 and inhabitantRoll <= 7):
            inhabitantRoll = random.randint(1,10)
    else:
        inhabitantRoll = random.randint(1,10)
    
    switch = {
        1: "Eldar",
        2: "Humans",
        3: "Humans",
        4: "Humans",
        5: "Kroot",
        6: "Orks",
        7: "Orks",
        8: "Rak’Gol",
        9: "Xenos (Other)",
        10: "Xenos (Other)",
    }
    return switch.get(inhabitantRoll)

#generates knife eared civ
def Eldar(habit):
    if habit != "Verdant": #Verdant = Habitable plane
        EldarRoll = random.randint(4,10)
    else: 
        EldarRoll = random.randint(1,10)
    switch = {
        1: "Primitive Clans (Exodites)††",
        2: "Primitive Clans (Exodites)††",
        3: "Primitive Clans (Exodites)††",
        4: "Orbital Habitation",
        5: "Orbital Habitation",
        6: "Orbital Habitation",
        7: "Orbital Habitation",
        8: "Orbital Habitation",
        9: "Voidfarers",
        10: "Voidfarers",
    }
    return switch.get(EldarRoll)

#generates hummies civ
def Humans(habit):
    if habit != "Verdant":
        HumanRoll = random.randint(1,10)
        while(HumanRoll >= 4 and HumanRoll <= 9):
            HumanRoll = random.randint(1,10)
    else:
        HumanRoll = random.randint(1,10)
    switch = {
        1: "Advanced Industry",
        2: "Advanced Industry",
        3: "Colony",
        4: "Orbital Habitation",
        5: "Basic Industry††",
        6: "Basic Industry††",
        7: "Pre-Industrial††",
        8: "Pre-Industrial††",
        9: "Primitive Clans††",
        10: "Voidfarers",
    }
    return switch.get(HumanRoll)

#generates Kroot civ
def Kroot():
    KrootRoll = random.randint(1,10)
    switch = {
        1: "Primitive Clans",
        2: "Primitive Clans",
        3: "Primitive Clans",
        4: "Primitive Clans",
        5: "Primitive Clans",
        6: "Primitive Clans",
        7: "Primitive Clans",
        8: "Colony",
        9: "Colony",
        10: "Colony",
    }
    return switch.get(KrootRoll)

#generates ork civ
def Orks():
    OrkRoll = random.randint(1,10)
    switch = {
        1: "Advanced Industry",
        2: "Advanced Industry",
        3: "Advanced Industry",
        4: "Advanced Industry",
        5: "Colony",
        6: "Primitive Clans",
        7: "Primitive Clans",
        8: "Primitive Clans",
        9: "Voidfarers",
        10: "Voidfarers",
    }
    return switch.get(OrkRoll)

#Generates RokGol civ            
def RakGol():
    RakGolRoll = random.randint(1,10)
    switch = {
        1: "Colony",
        2: "Colony",
        3: "Orbital",
        4: "Orbital",
        5: "Voidfarers",
        6: "Voidfarers",
        7: "Voidfarers",
        8: "Voidfarers",
        9: "Voidfarers",
        10: "Voidfarers",
    }    
    return switch.get(RakGolRoll)

#Generates other xenos civ
def XenosCiv(habit):
    if habit != "Verdant":
        XenosCivRoll = random.randint(1,10)
        while(XenosCivRoll >= 4 and XenosCivRoll <= 9):
            XenosCivRoll = random.randint(1,10)
    else:
        XenosCivRoll = random.randint(1,10)
    switch = {
        1: "Advanced Industry",
        2: "Advanced Industry",
        3: "Colony",
        4: "Orbital Habitation",
        5: "Basic Industry††",
        6: "Basic Industry††",
        7: "Pre-Industrial††",
        8: "Pre-Industrial††",
        9: "Primitive Clans††",
        10: "Voidfarers",
    }
    return switch.get(XenosCivRoll)

#Generates an inhabitant civilization uses rouge trader book
def generateInhabitantCiv(habit):
    Inhabitant = inhabitants(habit)
    if (Inhabitant == "Eldar"):
        Civilization = Eldar(habit)
    elif (Inhabitant == "Humans"):
        Civilization = Humans(habit)
    elif (Inhabitant == "Kroot"):
        Civilization = Kroot()
    elif (Inhabitant == "Orks"):
        Civilization = Orks()
    elif (Inhabitant == "Rak’Gol"):
        Civilization = RakGol()
    else:
        Civilization = XenosCiv(habit)
    return print("Inhabitants: ", Inhabitant,"\nCivilization: ", Civilization)

#Generates a Flora life form
def floraGeneration(World):
    profile = floralProfile()
    Type = floraType()
    print("Profile: "+ profile +"\nType: " + Type)
    floraSpeciesTraits(Type, World)

#Generates a fauna life form
def faunaGeneration(World):
    Base = faunaBase()
    Size = faunaSize(Base)
    print("Fauna Base: "+ Base +"\nFauna Size: " + Size)
    faunaBeastTraits(Base, World)
    
#Creates an entire ecosstem with up to 20 unique life forms
def Ecosystem(habit, World):
    if habit == "Limited Ecosystem":
        lifeforms = random.randint(1,6)
        advancedCiv = random.randint(1,10)
        if advancedCiv == 10:
            PrimitiveOrInhabitant = random.randint(1,10)
            if PrimitiveOrInhabitant <= 1:
                PrimitiveXenosGeneration()
            else:
                generateInhabitantCiv(habit)
    elif habit == "Verdant":
        lifeforms = random.randint(6,20)
        advancedCiv = random.randint(1,10)
        if advancedCiv >= 8:
            PrimitiveOrInhabitant = random.randint(1,10)
            if PrimitiveOrInhabitant <= 5:
                PrimitiveXenosGeneration()
            else:
                generateInhabitantCiv(habit)
    else:
        return "NO ECOSYSTEM"
    i = 1
   
    while i <= lifeforms: 
        #May change latter testing to see if generation looks like first
        #Should change to look better
        lifetype = random.randint(1,10)    
        switch = {
            1: lambda: floraGeneration(World),
            2: lambda: floraGeneration(World),
            3: lambda:  floraGeneration(World),
            4: lambda:  floraGeneration(World),
            5: lambda:  faunaGeneration(World),
            6: lambda:  faunaGeneration(World),
            7: lambda:  faunaGeneration(World),
            8: lambda:  faunaGeneration(World),
            9: lambda:  BeastGeneration(),
            10: lambda:  BeastGeneration(), 
        }
        # Call the function associated with the generated lifetype
        #next two lines are generated by Chat don't know how but they work
        print(f"\nLifeform {i} ")
        switch.get(lifetype, lambda: "Unknown type")()  # Default to "Unknown type" if no match
        i += 1  # Increment the counter
    
    

def main():
    #print(floralProfile(), floraType(), floraSpeciesTraits(floraType(), "Ocean World"))
    
    #This looks a lot nicer than the previous showing code above
    #profile = floralProfile()
    #Type = floraType()
    #print("Profile: "+ profile +"\nType: " + Type)
    #floraSpeciesTraits(Type, "Ocean World")
    #print("\n\n\n\n")
    #Base = faunaBase()
    #Size = faunaSize(Base)
    #print("Fauna Base: "+ Base +"\nFauna Size: " + Size)
    #faunaBeastTraits(Base, "")
    #print("\n\n\n\n")
    #PrimitiveXenosGeneration()
    #print("\n\n\n\n")
    #BeastGeneration()
    #print("\n\n\n\n")
    #generateInhabitantCiv("Verdant") #Verdant = everthing if not it has restrictions

    Ecosystem("Verdant", "Death World")



if __name__ == "__main__":
    main()