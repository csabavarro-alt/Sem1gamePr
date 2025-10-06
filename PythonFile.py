import time, random, sys
from colorama import init, Fore, Back, Style

init()
BRIGHT_GREEN = Fore.GREEN + Style.BRIGHT
GREENISH_GREY = Fore.LIGHTBLACK_EX
GLITCH_COLOURS = [Fore.RED, Fore.LIGHTRED_EX, Fore.YELLOW, Fore.LIGHTYELLOW_EX]
print(Back.BLACK, end="")


species = {
    "Rats": {
        "description": "Burrowing mammals, opportunistic feeders, fast breeders, and classic urban survivors.",
        "stats": {
            "Food Security": random.randint(65, 85),
            "Object Utilisation": random.randint(30, 50),
            "Mutation Capacity": random.randint(55, 75),
            "Aggression Level": random.randint(50, 70),
            "Social Cohesion": random.randint(45, 65),
            "Disease Resistance": random.randint(60, 80),
            "Resource Abundance": random.randint(70, 90),
            "Toxicity Tolerance": random.randint(50, 70),
            "Climate Adaptability": random.randint(65, 85),
            "Cultural Curiosity": random.randint(40, 60)
        }},
    "Eagles": {
        "description": "Majestic raptors with sharp eyesight, powerful hunting skills, and strong territorial instincts.",
        "stats": {
            "Food Security": random.randint(70, 90),
            "Object Utilisation": random.randint(15, 35),
            "Mutation Capacity": random.randint(40, 60),
            "Aggression Level": random.randint(65, 85),
            "Social Cohesion": random.randint(25, 45),
            "Disease Resistance": random.randint(55, 75),
            "Resource Abundance": random.randint(50, 70),
            "Toxicity Tolerance": random.randint(25, 45),
            "Climate Adaptability": random.randint(60, 80),
            "Cultural Curiosity": random.randint(10, 30)
        }},
    "Cockroaches": {
        "description": "Infamous insects that can withstand radiation, hunger, and thrive almost anywhere.",
        "stats": {
            "Food Security": random.randint(75, 95),
            "Object Utilisation": random.randint(5, 15),
            "Mutation Capacity": random.randint(60, 80),
            "Aggression Level": random.randint(20, 40),
            "Social Cohesion": random.randint(30, 50),
            "Disease Resistance": random.randint(70, 90),
            "Resource Abundance": random.randint(80, 100),
            "Toxicity Tolerance": random.randint(75, 95),
            "Climate Adaptability": random.randint(80, 100),
            "Cultural Curiosity": random.randint(5, 20)
        }},
    "Ants": {
        "description": "Eusocial insects with complex colonies, advanced cooperation, and large-scale engineering potential.",
        "stats": {
            "Food Security": random.randint(55, 75),
            "Object Utilisation": random.randint(15, 35),
            "Mutation Capacity": random.randint(50, 70),
            "Aggression Level": random.randint(65, 85),
            "Social Cohesion": random.randint(85, 100),
            "Disease Resistance": random.randint(45, 65),
            "Resource Abundance": random.randint(70, 90),
            "Toxicity Tolerance": random.randint(45, 65),
            "Climate Adaptability": random.randint(60, 80),
            "Cultural Curiosity": random.randint(10, 30)
        }},
    "Octopuses": {
        "description": "Intelligent marine invertebrates with problem-solving skills, dexterous limbs, and camouflage abilities.",
        "stats": {
            "Food Security": random.randint(50, 70),
            "Object Utilisation": random.randint(65, 85),
            "Mutation Capacity": random.randint(45, 65),
            "Aggression Level": random.randint(40, 60),
            "Social Cohesion": random.randint(30, 50),
            "Disease Resistance": random.randint(40, 60),
            "Resource Abundance": random.randint(55, 75),
            "Toxicity Tolerance": random.randint(30, 50),
            "Climate Adaptability": random.randint(45, 65),
            "Cultural Curiosity": random.randint(70, 90)
        }},
    "Fungi": {
        "description": "Spore-producing decomposers, thriving on decay, radiation, and extreme conditions.",
        "stats": {
            "Food Security": random.randint(80, 100),
            "Object Utilisation": 0,
            "Mutation Capacity": random.randint(75, 95),
            "Aggression Level": random.randint(5, 25),
            "Social Cohesion": random.randint(15, 35),
            "Disease Resistance": random.randint(85, 100),
            "Resource Abundance": random.randint(75, 95),
            "Toxicity Tolerance": random.randint(80, 100),
            "Climate Adaptability": random.randint(85, 100),
            "Cultural Curiosity": 0
        }},
    "Crocodiles": {
        "description": "Ancient reptiles with patience, durability, and the ability to endure harsh conditions for millennia.",
        "stats": {
            "Food Security": random.randint(60, 80),
            "Object Utilisation": random.randint(5, 25),
            "Mutation Capacity": random.randint(30, 50),
            "Aggression Level": random.randint(75, 95),
            "Social Cohesion": random.randint(25, 45),
            "Disease Resistance": random.randint(60, 80),
            "Resource Abundance": random.randint(45, 65),
            "Toxicity Tolerance": random.randint(40, 60),
            "Climate Adaptability": random.randint(65, 85),
            "Cultural Curiosity": random.randint(5, 30)
        }},
    "Jellyfish": {
        "description": "Simple, hardy sea creatures, some species capable of biological immortality.",
        "stats": {
            "Food Security": random.randint(55, 75),
            "Object Utilisation": 0,
            "Mutation Capacity": random.randint(35, 55),
            "Aggression Level": random.randint(10, 30),
            "Social Cohesion": random.randint(5, 25),
            "Disease Resistance": random.randint(70, 90),
            "Resource Abundance": random.randint(60, 80),
            "Toxicity Tolerance": random.randint(60, 80),
            "Climate Adaptability": random.randint(75, 95),
            "Cultural Curiosity": 0
        }},
    "Mole Rats": {
        "description": "Burrowing mammals adapted to low oxygen environments and extreme climates, with colony-like behavior.",
        "stats": {
            "Food Security": random.randint(45, 65),
            "Object Utilisation": random.randint(5, 30),
            "Mutation Capacity": random.randint(50, 70),
            "Aggression Level": random.randint(30, 50),
            "Social Cohesion": random.randint(60, 80),
            "Disease Resistance": random.randint(55, 75),
            "Resource Abundance": random.randint(50, 70),
            "Toxicity Tolerance": random.randint(55, 75),
            "Climate Adaptability": random.randint(65, 85),
            "Cultural Curiosity": random.randint(15, 35)
        }},
    "Tardigrades": {
        "description": "Microscopic 'water bears,' capable of surviving vacuum, radiation, and total desiccation.",
        "stats": {
            "Food Security": random.randint(30, 50),
            "Object Utilisation": 0,
            "Mutation Capacity": random.randint(65, 85),
            "Aggression Level": random.randint(5, 20),
            "Social Cohesion": random.randint(5, 20),
            "Disease Resistance": random.randint(85, 100),
            "Resource Abundance": random.randint(85, 100),
            "Toxicity Tolerance": random.randint(85, 100),
            "Climate Adaptability": random.randint(90, 100),
            "Cultural Curiosity": 0
        }},
    "Pigeons": {
        "description": "Urban scavengers who thrive wherever humans once lived, adaptable and prolific breeders.",
        "stats": {
            "Food Security": random.randint(70, 90),
            "Object Utilisation": random.randint(20, 40),
            "Mutation Capacity": random.randint(45, 65),
            "Aggression Level": random.randint(25, 45),
            "Social Cohesion": random.randint(60, 80),
            "Disease Resistance": random.randint(55, 75),
            "Resource Abundance": random.randint(65, 85),
            "Toxicity Tolerance": random.randint(30, 50),
            "Climate Adaptability": random.randint(60, 80),
            "Cultural Curiosity": random.randint(50, 70)
        }},
    "Goats": {
        "description": "Stubborn, hardy mammals capable of eating almost anything and surviving rugged terrain.",
        "stats": {
            "Food Security": random.randint(65, 85),
            "Object Utilisation": random.randint(10, 30),
            "Mutation Capacity": random.randint(40, 60),
            "Aggression Level": random.randint(30, 50),
            "Social Cohesion": random.randint(55, 75),
            "Disease Resistance": random.randint(60, 80),
            "Resource Abundance": random.randint(50, 70),
            "Toxicity Tolerance": random.randint(45, 65),
            "Climate Adaptability": random.randint(70, 90),
            "Cultural Curiosity": random.randint(25, 45)
        }},
    "Wolves": {
        "description": "Social predators with pack structures, intelligence, and adaptability to varied climates.",
        "stats": {
            "Food Security": random.randint(55, 75),
            "Object Utilisation": random.randint(15, 35),
            "Mutation Capacity": random.randint(45, 65),
            "Aggression Level": random.randint(65, 85),
            "Social Cohesion": random.randint(75, 95),
            "Disease Resistance": random.randint(55, 75),
            "Resource Abundance": random.randint(45, 65),
            "Toxicity Tolerance": random.randint(35, 55),
            "Climate Adaptability": random.randint(65, 85),
            "Cultural Curiosity": random.randint(35, 55)
        }},
    "Elephants": {
        "description": "Large-brained mammals with long lifespans, memory, and advanced social bonds.",
        "stats": {
            "Food Security": random.randint(50, 70),
            "Object Utilisation": random.randint(50, 70),
            "Mutation Capacity": random.randint(35, 55),
            "Aggression Level": random.randint(40, 60),
            "Social Cohesion": random.randint(80, 100),
            "Disease Resistance": random.randint(45, 65),
            "Resource Abundance": random.randint(40, 60),
            "Toxicity Tolerance": random.randint(25, 45),
            "Climate Adaptability": random.randint(55, 75),
            "Cultural Curiosity": random.randint(75, 95)
        }},
    "Ravens": {
        "description": "Cousins of crows, with even higher problem-solving skills and mythic resilience.",
        "stats": {
            "Food Security": random.randint(60, 80),
            "Object Utilisation": random.randint(75, 95),
            "Mutation Capacity": random.randint(45, 65),
            "Aggression Level": random.randint(35, 55),
            "Social Cohesion": random.randint(55, 75),
            "Disease Resistance": random.randint(50, 70),
            "Resource Abundance": random.randint(60, 80),
            "Toxicity Tolerance": random.randint(35, 55),
            "Climate Adaptability": random.randint(60, 80),
            "Cultural Curiosity": random.randint(80, 100)
        }},
    "Sea Bunnies": {
        "description": "Adorable but resilient nudibranchs with sensory rhinophores.",
        "stats": {
            "Food Security": random.randint(70, 90),
            "Object Utilisation": random.randint(5, 25),
            "Mutation Capacity": random.randint(75, 95),
            "Aggression Level": random.randint(5, 20),
            "Social Cohesion": random.randint(5, 25),
            "Disease Resistance": random.randint(80, 100),
            "Resource Abundance": random.randint(65, 85),
            "Toxicity Tolerance": random.randint(80, 100),
            "Climate Adaptability": random.randint(70, 90),
            "Cultural Curiosity": random.randint(15, 35)
        }},
    "Lizards": {
        "description": "Cold-blooded survivors, highly adaptable and widespread across all climates.",
        "stats": {
            "Food Security": random.randint(50, 70),
            "Object Utilisation": random.randint(5, 25),
            "Mutation Capacity": random.randint(55, 75),
            "Aggression Level": random.randint(30, 50),
            "Social Cohesion": random.randint(20, 40),
            "Disease Resistance": random.randint(60, 80),
            "Resource Abundance": random.randint(70, 90),
            "Toxicity Tolerance": random.randint(45, 65),
            "Climate Adaptability": random.randint(75, 95),
            "Cultural Curiosity": random.randint(10, 30)
        }},
    "Bats": {
        "description": "Nocturnal flyers with echolocation, colony organisation, and virus tolerance.",
        "stats": {
            "Food Security": random.randint(55, 75),
            "Object Utilisation": random.randint(15, 35),
            "Mutation Capacity": random.randint(50, 70),
            "Aggression Level": random.randint(25, 45),
            "Social Cohesion": random.randint(65, 85),
            "Disease Resistance": random.randint(80, 100),
            "Resource Abundance": random.randint(60, 80),
            "Toxicity Tolerance": random.randint(50, 70),
            "Climate Adaptability": random.randint(70, 90),
            "Cultural Curiosity": random.randint(30, 50)
        }},
    "Squat Lobsters": {
        "description": "Resilient crustaceans dwelling in deep seas, scavenging and withstanding pressure extremes.",
        "stats": {
            "Food Security": random.randint(45, 65),
            "Object Utilisation": random.randint(5, 25),
            "Mutation Capacity": random.randint(40, 60),
            "Aggression Level": random.randint(20, 40),
            "Social Cohesion": random.randint(15, 35),
            "Disease Resistance": random.randint(65, 85),
            "Resource Abundance": random.randint(70, 90),
            "Toxicity Tolerance": random.randint(55, 75),
            "Climate Adaptability": random.randint(75, 95),
            "Cultural Curiosity": random.randint(5, 25)
        }},
    "Slime Moulds": {
        "description": "Uncanny amoeboid organisms capable of collective intelligence and navigating mazes without brains.",
        "stats": {
            "Food Security": random.randint(75, 95),
            "Object Utilisation": random.randint(5, 20),
            "Mutation Capacity": random.randint(70, 90),
            "Aggression Level": 0,
            "Social Cohesion": random.randint(35, 55),
            "Disease Resistance": random.randint(70, 90),
            "Resource Abundance": random.randint(75, 95),
            "Toxicity Tolerance": random.randint(75, 95),
            "Climate Adaptability": random.randint(85, 100),
            "Cultural Curiosity": random.randint(20, 40)
        }}}

title = r"""
██████╗      ███████╗      ██████╗     ██████╗       █████╗ 
██╔══██╗     ██╔════╝     ██╔════╝     ██╔══██╗     ██╔══██╗
██████╔╝     █████╗       ██║          ██████╔╝     ███████║
██╔═══╝      ██╔══╝       ██║          ██╔═██║      ██╔══██║
██║      ██╗ ███████╗ ██╗ ╚██████╗ ██╗ ██║ ╚██╗ ██╗ ██║  ██║
╚═╝      ╚═╝ ╚══════╝ ╚═╝  ╚═════╝ ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═╝""" #PECRA sim title :D
print(BRIGHT_GREEN + title + Style.RESET_ALL + Back.BLACK)

def slow_print(text, delay=0.03, color=BRIGHT_GREEN):
    """Prints text slowly with specified color"""
    print(color, end="")  # Set the color
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL + Back.BLACK)

def boot_sequence():
    slow_print(">>> INITIALISING P.E.C.R.A. SIMULATION...", 0.03)
    time.sleep(1)
    slow_print(">>> USER DETECTED. TESTING PROTOCOL COMMENCING...", 0.03)
    time.sleep(1)
    slow_print(">>> LOADING BIOSPHERE TEMPLATES...", 0.03)
    time.sleep(1)
    slow_print(">>> GENERATING SURVIVOR CANDIDATES...", 0.03)
    print("\n")

def planet_scan():          #randomised planet stats
    stats = {
        "Climate Stability": {"value": random.randint(20, 95), "positive": True},
        "Resource Abundance": {"value": random.randint(10, 90), "positive": True},
        "Radiation Levels": {"value": random.randint(0, 80), "positive": False},
        "Water Availability": {"value": random.randint(10, 100), "positive": True},
        "Soil Fertility": {"value": random.randint(10, 100), "positive": True},
        "Atmosphere Quality": {"value": random.randint(30, 100), "positive": True},
        "Seismic Activity": {"value": random.randint(0, 100), "positive": "balanced"},
        "Magnetic Field Str": {"value": random.randint(30, 100), "positive": True},
        "Weather Volatility": {"value": random.randint(0, 90), "positive": False},
        "Disease Prevalence": {"value": random.randint(0, 90), "positive": False},}

    slow_print(">>> PLANETARY ASSESSMENT:", 0.03)
    time.sleep(1.5)
    for stat, data in stats.items():
        val = data["value"]
        bar = "█" * (val // 10) + "░" * (10 - val // 10)
        print(GREENISH_GREY + f" - {stat:22}: {bar} {val}%" + Style.RESET_ALL + Back.BLACK)
    score = 0
    for stat, data in stats.items():
        val = data["value"]
        if data["positive"] is True:
            score += val
        elif data["positive"] is False:
            score += (100 - val)
        else:
            score += (100 - abs(50 - val))
    avg_score = score / len(stats)
    if avg_score > 70:
        conclusion = "Favourable world. High potential."
        habitability = 4
    elif avg_score > 50:
        conclusion = "Moderately viable. Careful intervention required."
        habitability = 3
    elif avg_score > 30:
        conclusion = "Hostile conditions. Uplift will be challenging."
        habitability = 2
    else:
        conclusion = "Extreme hazards detected. Survival unlikely."
        habitability = 1
    time.sleep(1)
    print(GREENISH_GREY + f"\n - Conclusion: {conclusion}" + Style.RESET_ALL + Back.BLACK)
    return habitability
boot_sequence()
habitability = planet_scan()

def specie_selection(habitability):         #CHOOSE YOUR FIGHTER!
    tiered_species = {
        4: ["Elephants", "Ravens", "Eagles", "Octopuses", "Sea Bunnies"],
        3: ["Wolves", "Goats", "Pigeons", "Bats", "Rats"],
        2: ["Crocodiles", "Lizards", "Ants", "Mole Rats", "Cockroaches"],
        1: ["Tardigrades", "Fungi", "Slime Moulds", "Jellyfish", "Squat Lobsters"]}
    candidate_selection = random.sample(tiered_species[habitability], 3)
    while True:
        candidate_choice = input(GREENISH_GREY + f"\n - Choose a specie from {', '.join(candidate_selection)}: " + Style.RESET_ALL + Back.BLACK)
        match = None
        for c in candidate_selection:
            if candidate_choice.lower() == c.lower():
                match = c
                break
        if match:
            chosen = match
            print(GREENISH_GREY + f"\n - {chosen}: {species[chosen]['description']}" + Style.RESET_ALL + Back.BLACK)
            print(GREENISH_GREY + " - Stats:" + Style.RESET_ALL + Back.BLACK)
            for stat, val in species[chosen]["stats"].items():
                print(GREENISH_GREY + f"    {stat}: {val}" + Style.RESET_ALL + Back.BLACK)

            affirmation = input(GREENISH_GREY + f"\n - Are you sure? (Y/N): " + Style.RESET_ALL + Back.BLACK)
            if affirmation.lower() == "y":
                print(GREENISH_GREY + f"\n - You chose {chosen}" + Style.RESET_ALL + Back.BLACK)
                return chosen
            else:
                print(GREENISH_GREY + " - Select again" + Style.RESET_ALL + Back.BLACK)
        else:
            print(GREENISH_GREY + " - Invalid input. Candidate organism not recognised. Re-attempt selection." + Style.RESET_ALL + Back.BLACK)
specie = specie_selection(habitability)

def specie_name():
    while True:
        name = input(GREENISH_GREY + """ - What do you want to refer to your civilisation as (this program will not provide you with 'The'
 - if 'The' is needed when talking about your civilisation, please add it yourself in this section): """ + Style.RESET_ALL + Back.BLACK)

        if name.lower() == "dimensional beasts" or name.lower() == "the dimensional beasts":
            print(GREENISH_GREY + """ - The Dimensional Beasts crumble to dust out of fear from the sheer aura of THE ROGUE, 
   who in record time broke the attempted limitation of its power.  

   LV 37 - 302 HP - 77 ATK - 37 DEF - 40 MAGIC - DRINKS GOLDEN JUICE LIKE CARTONS OF MILK""" + Style.RESET_ALL + Back.BLACK)
            time.sleep(7.5)
            for i in range (679):
                glitch_texts = [
                    "IIꓥOꓶꓛ   ꓤ Ǝ ꓥ O   Ǝ W Ɐ ꓨ",
                    ">>> ERR0R: UNHANDLED EXCEPTION @ MEMORY SECTOR ████",
                    "ⱯꓤƎ    ƎW    Oꓶꓛ    ꓥOꓶII",
                    "SYSTEM INTEGRITY FAILURE: 0x000DEAD",
                    ">>> WARNING: SUBJECT_█ has disintegrated",
                    "ꓷNꓵOꓞ ꓕON ƎXƎ·ꓕSⱯƎꓭ_ꓶⱯNOISNƎWIꓷ :ꓤOꓤꓤƎ <<<"]
                print(random.choice(GLITCH_COLOURS) + random.choice(glitch_texts) + Style.RESET_ALL + Back.BLACK)
                time.sleep(0.05)
            sys.exit()
        elif name.lower() == "humans" or name.lower() == "humanity" or name.lower() == "mankind":
            print(GREENISH_GREY + " - Negative. Leave those damned apes to stay deceased. Their legacy is to be forgotten" + Style.RESET_ALL + Back.BLACK)
        else:
            print(GREENISH_GREY + f" - {name} ... Interesting choice" + Style.RESET_ALL + Back.BLACK)
            break
    return name
named_specie = specie_name()

slow_print(">>> DISPENSING EVOLUTIONARY MUTATION ENHANCING FORMULA INTO THE AIR . . .", 0.03)
slow_print(">>> CALCULATING  .  .  .", 0.4)
time.sleep(0.5)
print(GREENISH_GREY + f""" - {named_specie} will reach technological emergent civilisation in 10,000 years
 - with slight genetic modifications and technological nudges every 100 years""" + Style.RESET_ALL + Back.BLACK)
