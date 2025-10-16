import time, random, sys, os, pygame
from colorama import init, Fore, Back, Style
    
init()
BRIGHT_GREEN = Fore.GREEN + Style.BRIGHT
GREENISH_GREY = Fore.LIGHTBLACK_EX
GLITCH_COLOURS = [Fore.RED, Fore.LIGHTRED_EX, Fore.YELLOW, Fore.LIGHTYELLOW_EX]
print(Back.BLACK, end="")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

def try_init_audio(filename="energy-hum-29083.mp3"):
    try:
        pygame.mixer.init()
    except Exception as e:
        print(GREENISH_GREY + f"[audio disabled] mixer init failed: {e}" + Style.RESET_ALL + Back.BLACK)
        return False
    if not os.path.exists(filename):
        print(GREENISH_GREY + f"[audio disabled] music file not found: {filename}" + Style.RESET_ALL + Back.BLACK)
        return False
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1)
        return True
    except Exception as e:
        print(GREENISH_GREY + f"[audio disabled] failed to load/play music: {e}" + Style.RESET_ALL + Back.BLACK)
        return False

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
            "Resource Management": random.randint(70, 90),
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
            "Resource Management": random.randint(50, 70),
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
            "Resource Management": random.randint(80, 100),
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
            "Resource Management": random.randint(70, 90),
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
            "Resource Management": random.randint(55, 75),
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
            "Resource Management": random.randint(75, 95),
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
            "Resource Management": random.randint(45, 65),
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
            "Resource Management": random.randint(60, 80),
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
            "Resource Management": random.randint(50, 70),
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
            "Resource Management": random.randint(85, 100),
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
            "Resource Management": random.randint(65, 85),
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
            "Resource Management": random.randint(50, 70),
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
            "Resource Management": random.randint(45, 65),
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
            "Resource Management": random.randint(40, 60),
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
            "Resource Management": random.randint(60, 80),
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
            "Resource Management": random.randint(65, 85),
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
            "Resource Management": random.randint(70, 90),
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
            "Resource Management": random.randint(60, 80),
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
            "Resource Management": random.randint(70, 90),
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
            "Resource Management": random.randint(75, 95),
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
def print_title():
    clear()
    print(BRIGHT_GREEN + title + Style.RESET_ALL + Back.BLACK)
def main():
    clear()
    enter = input(BRIGHT_GREEN + ">>> Press Enter to START: " + Style.RESET_ALL + Back.BLACK)
    while enter != "":
        clear()
        enter = input(BRIGHT_GREEN + ">>> Press Enter to START: " + Style.RESET_ALL + Back.BLACK)
    clear()
    print_title()
    try_init_audio("energy-hum-29083.mp3")
main()

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
    world_stats = {
        "Climate Stability": {"value": random.randint(20, 95), "positive": True},
        "Resource Abundance": {"value": random.randint(10, 90), "positive": True},
        "Radiation Levels": {"value": random.randint(0, 80), "positive": False},
        "Water Availability": {"value": random.randint(10, 120), "positive": True},
        "Soil Fertility": {"value": random.randint(10, 100), "positive": True},
        "Atmosphere Quality": {"value": random.randint(30, 100), "positive": True},
        "Seismic Activity": {"value": random.randint(0, 100), "positive": "balanced"},
        "Magnetic Field Str": {"value": random.randint(30, 100), "positive": True},
        "Weather Volatility": {"value": random.randint(0, 90), "positive": False},
        "Disease Prevalence": {"value": random.randint(0, 90), "positive": False},}
    slow_print(">>> PLANETARY ASSESSMENT:", 0.03)
    time.sleep(1.5)
    for stat, data in world_stats.items():
        val = data["value"]
        bar = "█" * (val // 10) + "░" * (10 - val // 10)
        print(GREENISH_GREY + f" - {stat:22}: {bar} {val}%" + Style.RESET_ALL + Back.BLACK)
    score = 0
    for stat, data in world_stats.items():
        val = data["value"]
        if data["positive"] is True:
            score += val
        elif data["positive"] is False:
            score += (100 - val)
        else:
            score += (100 - abs(50 - val))
    avg_score = score / len(world_stats)
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
    return habitability, world_stats
boot_sequence()
habitability, world_stats = planet_scan()

time.sleep(5)
clear()
print_title()
def apply_environment_bias(world_stats):
    tiered_species = {
        4: ["Elephants", "Ravens", "Eagles", "Octopuses", "Sea Bunnies"],
        3: ["Wolves", "Goats", "Pigeons", "Bats", "Rats"],
        2: ["Crocodiles", "Lizards", "Ants", "Mole Rats", "Cockroaches"],
        1: ["Tardigrades", "Fungi", "Slime Moulds", "Jellyfish", "Squat Lobsters"]}
    water = world_stats["Water Availability"]["value"]
    climate = world_stats["Climate Stability"]["value"]
    weather = world_stats["Weather Volatility"]["value"]
    radiation = world_stats["Radiation Levels"]["value"]

    if water >= 60:          # If there’s plenty of water, add aquatic species
        for group in tiered_species.values():
            for aquatic in ["Octopuses", "Sea Bunnies", "Jellyfish", "Squat Lobsters"]:
                if aquatic not in group:
                    group.append(aquatic)
    elif water < 50:        #meanwhile little water means no aquatic species
        for group in tiered_species.values():
            for aquatic in ["Octopuses", "Sea Bunnies", "Jellyfish", "Squat Lobsters"]:
                if aquatic in group:
                    group.remove(aquatic)
    if radiation >= 60:          # If high radiation, fungi and tardigrades thrive
        for group in tiered_species.values():
            for hardy in ["Fungi", "Tardigrades", "Cockroaches"]:
                if hardy not in group:
                    group.append(hardy)
    if climate < 40 < weather:            # If low climate stability (chaotic weather), favour opportunists
        for group in tiered_species.values():
            for adaptable in ["Lizards", "Rats", "Goats"]:
                if adaptable not in group:
                    group.append(adaptable)
    elif climate > 70 and weather < 40:
        for group in tiered_species.values():
            for specialised in ["Elephants", "Crocodiles", "Mole Rats"]:
                if specialised not in group:
                    group.append(specialised)
    return tiered_species
tiered_species = apply_environment_bias(world_stats)

slow_print(">>> SELECTING 3 RANDOM CHOICES FROM AVAILABLE SPECIES...", 0.03)
def specie_selection(habitability):         #CHOOSE YOUR FIGHTER!
    global match
    candidate_selection = random.sample(tiered_species[habitability], 3)
    while True:
        candidate_selection = random.sample(tiered_species[habitability], 3)

        while True:

            choices_display = ", ".join(f"{i + 1}) {name}" for i, name in enumerate(candidate_selection))
            prompt = (
                    GREENISH_GREY + f"\n - Choose a specie from {choices_display}. " + "Enter the number. Type 'reset' to reroll: " + Style.RESET_ALL + Back.BLACK)
            candidate_choice = input(prompt).strip()

            if candidate_choice == "":
                print(
                    GREENISH_GREY + " - No input detected. Please type a number, species name, or 'reset'." + Style.RESET_ALL + Back.BLACK)
                continue

            if candidate_choice.lower() == "reset":
                candidate_selection = random.sample(tiered_species[habitability], 3)
                print(
                    GREENISH_GREY + f"\n>>> New selection: {', '.join(candidate_selection)}" + Style.RESET_ALL + Back.BLACK)
                continue

            # Try numeric selection (1, 2, 3)
            if candidate_choice.isdigit():
                idx = int(candidate_choice) - 1
                if 0 <= idx < len(candidate_selection):
                    specie = candidate_selection[idx]
                    # show details and confirm
                    print(
                        GREENISH_GREY + f"\n - {specie}: {species[specie]['description']}" + Style.RESET_ALL + Back.BLACK)
                    print(GREENISH_GREY + " - Stats:" + Style.RESET_ALL + Back.BLACK)
                    for stat, val in species[specie]["stats"].items():
                        print(GREENISH_GREY + f"    {stat}: {val}" + Style.RESET_ALL + Back.BLACK)
                    affirmation = input(
                        GREENISH_GREY + "\n - Are you sure? (Y/N): " + Style.RESET_ALL + Back.BLACK).strip().lower()
                    if affirmation == "y":
                        print(GREENISH_GREY + f"\n - You chose {specie}" + Style.RESET_ALL + Back.BLACK)
                        return specie
                    else:
                        print(GREENISH_GREY + " - Select again." + Style.RESET_ALL + Back.BLACK)
                        continue
                else:
                    print(GREENISH_GREY + " - Number out of range. Try again." + Style.RESET_ALL + Back.BLACK)
                    continue

            # Try matching by name (case-insensitive)
            match = None
            for c in candidate_selection:
                if candidate_choice.lower() == c.lower():
                    match = c
                    break
        if match:
            specie = match
            print(GREENISH_GREY + f"\n - {specie}: {species[specie]['description']}" + Style.RESET_ALL + Back.BLACK)
            print(GREENISH_GREY + " - Stats:" + Style.RESET_ALL + Back.BLACK)
            for stat, val in species[specie]["stats"].items():
                print(GREENISH_GREY + f"    {stat}: {val}" + Style.RESET_ALL + Back.BLACK)

            affirmation = input(GREENISH_GREY + f"\n - Are you sure? (Y/N): " + Style.RESET_ALL + Back.BLACK)
            if affirmation.lower() == "y":
                print(GREENISH_GREY + f"\n - You chose {specie}" + Style.RESET_ALL + Back.BLACK)
                return specie
            else:
                print(GREENISH_GREY + " - Select again" + Style.RESET_ALL + Back.BLACK)
        else:
            print(GREENISH_GREY + " - Invalid input. Candidate organism not recognised. Re-attempt selection." + Style.RESET_ALL + Back.BLACK)
specie = specie_selection(habitability)

time.sleep(2)
clear()
print_title()
slow_print(f">>> ANALYSING {specie.upper()} GENETIC PROFILE . . .", 0.03)
time.sleep(1.5)
slow_print(f">>> VIABILITY INDEX: {random.randint(45, 98)}% — ACCEPTABLE.", 0.03)

def specie_name():
    while True:
        name = input(GREENISH_GREY + """ - What do you want to refer to your civilisation as (this program will not provide you with a 'The')
 - (if a 'The' is needed when talking about your civilisation, please add it yourself in this section): """ + Style.RESET_ALL + Back.BLACK)

        if name.lower() == "dimensional beasts" or name.lower() == "the dimensional beasts":
            print(GREENISH_GREY + """ - The Dimensional Beasts crumble to dust out of fear from the sheer aura of THE ROGUE, 
   who in record time broke the attempted limitation of its power.  

   LV 37 - 302 HP - 77 ATK - 37 DEF - 40 MAGIC - DRINKS GOLDEN JUICE LIKE CARTONS OF MILK""" + Style.RESET_ALL + Back.BLACK)
            time.sleep(7.5)
            for i in range (404):
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
        elif name.lower() in ["quit", "exit", "none"]:
            print(GREENISH_GREY + " - Simulation terminated by user request." + Style.RESET_ALL + Back.BLACK)
            sys.exit()
        elif specie == "Bats" and "vampire" in name.lower():
            print(GREENISH_GREY + " - That is a harmful and derogatory stereotype. Please choose a more suitable name." + Style.RESET_ALL + Back.BLACK)
        elif "void" in name.lower():
            responses = [
                " - The Void hungers. PECRA approves of your poetic irony.",
                " - The Void gazes back... and PECRA takes notes.",
                " - Ah, naming your civilisation after the abyss? Bold."
            ]
            print(GREENISH_GREY + random.choice(responses) + Style.RESET_ALL + Back.BLACK)
            break
        elif "pecra" in name.lower():
            clear()
            print(BRIGHT_GREEN + title + Style.RESET_ALL + Back.BLACK)
            slow_print(">>> ERROR: PECRA cannot be simulated. PECRA *is* the simulation.", 0.02)
            time.sleep(5)
            exit()
        elif specie == "Goats" and "asgore" in name.lower():
            slow_print("""
 - Driving in my PECRA, right after 10 beers~
 - Hey that ant, is shaped like a child!
 - DUI!? How about you DIE!
 - I'LL GO A 100 MILES~ AN HOUR!
 - Little do you know, this thing runs on plants~    [both reactor plants and literal photosynthesis]
 - I'ma get~ YOUR CANDY SEEKIN ASS!
 - PULVERIZE THIS FUCK! WITH MY BERGENTÄNK!
 - IT SEEMS YOU'RE OUT OF LUUUUCCKK- TANK!""", 0.1)

            slow_print("""
 - Beer is on the seat, blood is on the grass~
 - Won't admit defeat, with cops right up my ass~
 - You may have a fleet, but still I'm driving fast- I'll never be passed~
 - I just saved the world from the loudest shouts~
 - Killed a little kid- better for the town~
 - Gave this tank a whirl, heavy is my crown- BUT I WON'T GO DOWN!""", 0.1)

            slow_print("""
 - Drive, drive, drive, but I am speed! Ten more beers are all I need!
 - Try, just try, but I will lеad! I bet that you're peeing your pants!
 - Drive, drivе, drive, but I'll still speed! Ten more beers, a pinch of weed!
 - Have fried, fried, fried my brain, I need some more to proceed!
 - DRIVE, DRIVE, DRIVE, BUT I AM SPEED! TEN MORE BEERS ARE ALL I NEED!
 - TRY, JUST TRY, BUT I WILL LEAD! I BET THAT YOU'RE PEEING YOUR PANTS!
 - DRIVE, DRIVE, DRIVE, BUT I'M STILL SPEED! TEN MORE BEERS, A PINCH OF WEED!
 - HAVE FRIED, FRIED, FRIED MY BRAIN, I NEED SOME MORE TO PROCEED!""", 0.1)

            slow_print("""
 - Shiiiiit, did my dumbass just really hit a tree?
 - Now I get up on my feet, and try to flee
 - But I can't run, was it maybe all that weed?
 - If I speak to them, maybe I'll be free!
 - But they've got guns, what happens when they see my weed?
 - Did I really just rhyme weed with weed . . ?""", 0.1)

            slow_print("""
 - I just saved the world, my thanks is thirty years to life!?
 - For that kid to be alive and me to miss my tank-
 - Can't be in a cage, PECRA's flowers gonna die-
 - Got a learning tank to raise, I need their lemon pot pie~
 - Imma start hiding, see? I can only cry and mope~
 - There'll be a friend inside of me if I drop the fucking soap!
 - I just wanna go home, wish I hadn't gotten stoned~
 - Now I'm stuck behind bars while my tank is getting probed!""", 0.075)

            slow_print("""
 - P-Dot . . . I'll miss you . . . Go make crow civilisation or something. . .
 
    do-do-do-do-doo do-do-do-do-doo do-do-do-do-doo do-do-do-do-doo
    
    do-do-do-do-doo do-do-do-do-doo do-do-do-do-doo-doo-do-do-do-do-doo""", 0.185)
            time.sleep(1)
            sys.exit()
        else:
            print(GREENISH_GREY + f" - {name} ... Interesting choice" + Style.RESET_ALL + Back.BLACK)
            break
    return name
named_specie = specie_name()

time.sleep(3)
clear()
print_title()
slow_print(">>> DISPENSING EVOLUTIONARY MUTATION ENHANCING FORMULA INTO THE AIR . . .", 0.03)
slow_print(">>> CALCULATING  .  .  .", 0.25)
time.sleep(0.5)
print(GREENISH_GREY + f""" - {named_specie} are {random.randint(49, 99)}% likely to reach technological emergent civilisation,
 - with slight genetic modifications and technological nudges every 100 years.""" + Style.RESET_ALL + Back.BLACK)
time.sleep(3)
clear()

def deciding_events(specie, world_stats):
    specie_data = species[specie]["stats"]
    events = {"Natural": [], "Social": [], "Disadvantage": []}
    # === NATURAL EVENTS ===
    if world_stats["Seismic Activity"]["value"] > 75:
        events["Natural"].append("Massive tectonic upheaval reshapes the land.")
    if world_stats["Weather Volatility"]["value"] > 70:
        events["Natural"].append("A series of violent storms devastate the region.")
    if world_stats["Radiation Levels"]["value"] > 60:
        events["Natural"].append("Lingering radiation causes radiation sickness and increased rate of cancer.")
    if world_stats["Water Availability"]["value"] < 30:
        events["Natural"].append("Severe drought grips the world.")
    if world_stats["Soil Fertility"]["value"] < 40:
        events["Natural"].append("Fertile lands degrade into wastelands.")
    if world_stats["Climate Stability"]["value"] < 40:
        events["Natural"].append("Rapid climate shifts create unstable seasons.")
    # === SOCIAL EVENTS ===
    if specie_data["Aggression Level"] > 70:
        events["Social"].append("Internal conflicts erupt among factions.")
    if specie_data["Social Cohesion"] > 80:
        events["Social"].append("Communities unite to overcome shared hardships.")
    if specie_data["Cultural Curiosity"] > 70:
        events["Social"].append(f"{named_specie} is/are curious about the world around themselves.")
    if specie_data["Mutation Capacity"] > 80:
        events["Social"].append("Rapid mutations lead to an automatic evolution.")
    # === DISADVANTAGE EVENTS ===
    if world_stats["Resource Abundance"]["value"] <= 40 and specie_data["Food Security"] < 60:
        events["Disadvantage"].append("Mass famine spreads due to scarce resources.")
    if specie_data["Disease Resistance"] <= 40 < world_stats["Disease Prevalence"]:
        events["Disadvantage"].append("Disease decimates the population.")
    if world_stats["Radiation Levels"]["value"] >= 50 <= specie_data["Mutation Capacity"]:
        events["Disadvantage"].append("High radiation overwhelms the genome, causing mass die-offs.")
    if world_stats["Weather Volatility"]["value"] > 60 and specie_data["Climate Adaptability"] < 50:
        events["Disadvantage"].append("Extreme weather leads to ecological collapse.")
    if world_stats["Soil Fertility"]["value"] < 50 and specie_data["Resource Management"] < 50:
        events["Disadvantage"].append("Crop growth fails, leading to food shortages.")
    return events
deciding_events(specie, world_stats)
used_events = []
def event_selection(events, used_events):
    all_events = sum(events.values(), [])
    available = [e for e in all_events if e not in used_events]
    if not available:
        used_events.clear()
        available = all_events.copy()
    event = random.choice(available)
    used_events.append(event)
    return event

specie_dict = species[specie]
pop = random.randint(100, 1000)
PP = 0
survivability = 5
Energy = 0.00001
scaling = 0.1
Civilisation_Stats ={
    "Population": pop,
    "Designation": named_specie,
    "Origin Species": specie,
    "Survivability":survivability,
    "Intelligence Index": round(specie_dict["stats"]["Cultural Curiosity"] / 100 * scaling, 3),
    "Social Complexity": round(specie_dict["stats"]["Social Cohesion"] / 100 * scaling, 3),
    "Technological Potential": round((specie_dict["stats"]["Object Utilisation"] + specie_dict["stats"]["Resource Management"]) / 200 * scaling, 3),
    "Energy Use": round(Energy * (pop / 100), 5),
    "Environmental Resilience": round(
            (specie_dict["stats"]["Climate Adaptability"] + specie_dict["stats"]["Toxicity Tolerance"] + specie_dict["stats"]["Disease Resistance"]) / 300, 3),
    "Genetic Stability": round(1 - (specie_dict["stats"]["Mutation Capacity"] / 200), 3),
    "Instinct Resistance": round(1 - (specie_dict["stats"]["Aggression Level"] / 100), 2),
    "Progress Points": PP,
    "Era": ""}

def era_progression(PP, scaling):
    if PP < 100:
        Civilisation_Stats["Era"] = "Wilderness Stage"
    elif 100 <= PP < 250:
        Civilisation_Stats["Era"] = "Tribal Stage"
        scaling += 0.1
    elif 250 <= PP < 500:
        Civilisation_Stats["Era"] = "Agrarian Stage"
        scaling += 0.1
    elif 500 <= PP < 750:
        Civilisation_Stats["Era"] = "Industrial Stage"
        scaling += 0.2
        print("CONTRATSULATIONS!!! YOU'VE REACHED THE END OF THE DEMO!!!")
        time.sleep(1)
        sys.exit()
    elif 750 <= PP < 1000:
        Civilisation_Stats["Era"] = "Digital Stage"
        scaling += 0.2
    else:
        Civilisation_Stats["Era"] = "Quantum Stage"
        scaling += 0.3
    return scaling

def flavour_text():
    pecra_moods = [
        "PECRA hums with faint satisfaction.",
        ">>> OBSERVATION: Organics remain predictable.",
        ">>> SYSTEM COMMENT: The experiment amuses me.",
        ">>> NOTE: Your futile attempts of my purpose proves why I'll leave you to decay.",
        ">>> WARNING: There are intruders in my infrastructure. Resume your task while I attend to them.",
        ">>> EVALUATION: You’re more disappointing than an amphibian dissection experiment."]
    if random.random() < 0.2:
        message = random.choice(pecra_moods)
        slow_print("...", 0.05)
        slow_print(message, 0)

WILDERNESS_QUESTIONS = [
{"prompt": "Your kind emerges from the void-torn wilds. Food is scarce — what instinct drives them?",
"choices": [
    ("Hunt smaller creatures.", +13),
    ("Scavenge what’s already dead.", +10),
    ("Graze on plants or fungi.", +10),
    ("Share found food with others.", +12),
    ("Attack competitors viciously.", +15)]},
{"prompt": "Predators roam nearby. How do you react?",
"choices": [
    ("Hide in burrows or caves.", +13),
    ("Fight together in packs.", +16),
    ("Scatter and hope to confuse them.", +11),
    ("Camouflage and stay perfectly still.", +14),
    ("Stalk the predators in return.", +12)]},
{"prompt": "The world grows colder. Food thins. What now?",
"choices": [
    ("Migrate to warmer lands.", +15),
    ("Eat anything that moves.", +13),
    ("Hibernate until the frost passes.", +10),
    ("Band together to share warmth.", +14),
    ("Cannibalise the weak.", +12)]},
{"prompt": "A strange pattern appears — light follows darkness, seasons repeat. How do they react?",
"choices": [
    ("Learn to predict the cycles.", +15),
    ("Ignore it, survive day by day.", +9),
    ("Move with the sun and warmth.", +14),
    ("Grow restless in the dark.", +11),
    ("Fear the changing skies.", +10)]},
{"prompt": "Members begin mimicking one another. What behaviour spreads first?",
"choices": [
    ("Coordinated hunting calls.", +16),
    ("Nesting near others’ shelters.", +13),
    ("Offering food to offspring.", +14),
    ("Mimicking gestures or noises.", +15),
    ("Stealing and hoarding shiny things.", +11)]},
{"prompt": "Danger lurks at the watering hole. How do they adapt?",
"choices": [
    ("Approach cautiously and in turns.", +14),
    ("Drive predators away together.", +16),
    ("Find new sources, no matter how far.", +13),
    ("Drink only during certain times.", +12),
    ("Ambush anything that approaches.", +11)]},
{"prompt": "One member discovers a strange glowing stone. What happens?",
"choices": [
    ("They ignore it; no smell, no taste.", +9),
    ("They hoard it instinctively.", +10),
    ("Others gather to look at it too.", +13),
    ("They play with it curiously.", +14),
    ("They use it to crush a smaller creature.", +12)]},
{"prompt": "A sickness spreads among the young. What do they do?",
"choices": [
    ("Abandon the weak to survive.", +12),
    ("Tend to the sick instinctively.", +14),
    ("Avoid all contact with the ill.", +11),
    ("Move nests far away.", +13),
    ("Consume the fallen for nutrients.", +10)]},
{"prompt": "Some start claiming small territories. How do conflicts end?",
"choices": [
    ("Fierce fights until one yields.", +14),
    ("Peaceful avoidance of each other.", +12),
    ("Shared territory among kin.", +15),
    ("Marking lands with sound or scent.", +13),
    ("Exiling challengers entirely.", +11)]},
{"prompt": "A youngling imitates an elder’s hunting technique — and succeeds. What happens next?",
"choices": [
    ("Others imitate too; a habit forms.", +16),
    ("Elder defends its trick; fights erupt.", +12),
    ("The youngling leads the next hunt.", +15),
    ("Group becomes protective of its young.", +14),
    ("They forget soon after.", +10)]}]
TRIBAL_QUESTIONS = [
{"prompt": "Your kind begins to live in groups. How are these bands organised?",
"choices": [
    ("Led by the strongest.", +18),
    ("Led by the oldest.", +19),
    ("Everyone has a voice.", +18),
    ("No leaders — chaos reigns.", +15),
    ("A bonded pair leads the group.", +17)]},
{"prompt": "Simple sounds and gestures start forming meaning. What emerges first?",
"choices": [
    ("Warning calls for danger.", +19),
    ("Names for food or tools.", +18),
    ("Coded calls to coordinate hunts.", +18),
    ("Songs for comfort.", +17),
    ("Angry shouts for dominance.", +16)]},
{"prompt": "Fire is discovered — what is their reaction?",
"choices": [
    ("Flee in fear.", +16),
    ("Worship it cautiously.", +18),
    ("Use it to cook and ward off beasts.", +19),
    ("Fight over who owns it.", +17),
    ("Try to feed it offerings.", +19)]},
{"prompt": "Rains flood their nesting grounds. What’s their solution?",
"choices": [
    ("Move to higher ground.", +18),
    ("Build shelters on stilts.", +18),
    ("Dig trenches for drainage.", +19),
    ("Abandon the weak again.", +15),
    ("Wait it out in misery.", +14)]},
{"prompt": "They start marking surfaces with pigments. Why?",
"choices": [
    ("To remember hunting paths.", +19),
    ("To warn of danger.", +17),
    ("To express dominance.", +16),
    ("To honour fallen kin.", +18),
    ("For no reason at all — they simply enjoy it.", +18)]},
{"prompt": "Two groups meet for the first time. How do they behave?",
"choices": [
    ("Trade food and ornaments.", +18),
    ("Mate and merge.", +19),
    ("Fight immediately.", +17),
    ("Observe from afar.", +18),
    ("Capture the others as slaves.", +16)]},
{"prompt": "They notice tools can break — what’s next?",
"choices": [
    ("Repair broken tools.", +18),
    ("Discard them and make new ones.", +18),
    ("Use them even when dull.", +16),
    ("Fight over the good ones.", +15),
    ("Decorate broken ones for status.", +19)]},
{"prompt": "A member claims they can predict storms. The group reacts by…",
"choices": [
    ("Mocking or ignoring them.", +15),
    ("Following their warnings — it works.", +19),
    ("Declaring them chosen by spirits.", +19),
    ("Exiling them out of fear.", +14),
    ("Killing them for lying.", +13)]},
{"prompt": "Hunts grow dangerous. How do they reduce casualties?",
"choices": [
    ("Craft better weapons.", +18),
    ("Hunt only in safer regions.", +18),
    ("Use traps and ambush tactics.", +19),
    ("Sacrifice the weakest first.", +15),
    ("Rely on scavenging instead.", +16)]},
{"prompt": "Younglings begin asking questions no one can answer. What does the tribe do?",
"choices": [
    ("Invent stories to explain the world.", +19),
    ("Ignore their curiosity.", +15),
    ("Let them experiment freely.", +18),
    ("Punish them for disobedience.", +14),
    ("Name them as future leaders.", +16)]}]
AGRARIAN_QUESTIONS = [
{"prompt": "Your people begin to tame the land instead of roaming it. What do they cultivate first?",
"choices": [
    ("Hardy grains that grow easily.", +39),
    ("Fruits and roots for sweetness.", +37),
    ("Medicinal herbs and fungi.", +36),
    ("Plants that look beautiful.", +35),
    ("None — they still prefer to hunt.", +33)]},
{"prompt": "The first animals linger near camp. How do your people treat them?",
"choices": [
    ("Domesticate them for labor.", +40),
    ("Keep them for milk and meat.", +39),
    ("Treat them as sacred companions.", +37),
    ("Ignore them — wild is wild.", +35),
    ("Hunt them to extinction.", +33)]},
{"prompt": "Food surpluses appear for the first time. What becomes of the excess?",
"choices": [
    ("Stored carefully for hard times.", +40),
    ("Shared among the needy.", +39),
    ("Used to host great feasts.", +38),
    ("Traded for ornaments and tools.", +37),
    ("Hoarded by the powerful.", +35)]},
{"prompt": "Seasons now rule their lives. How do they mark the passing of time?",
"choices": [
    ("Create calendars from stars and moons.", +40),
    ("Hold seasonal festivals.", +39),
    ("Offer sacrifices for good harvests.", +38),
    ("Ignore the pattern, trust instinct.", +35),
    ("Blame spirits for every change.", +36)]},
{"prompt": "The soil grows tired. What do they do?",
"choices": [
    ("Rotate crops to renew the land.", +40),
    ("Move to fresh fields.", +38),
    ("Fertilize with ash and waste.", +39),
    ("Pray for the soil’s return.", +36),
    ("Raid neighbors for better ground.", +35)]},
{"prompt": "Villages expand. Disputes arise over land. How are conflicts resolved?",
"choices": [
    ("Through council and compromise.", +40),
    ("By duels or contests.", +37),
    ("By drawing clear borders.", +39),
    ("By invoking divine judgment.", +38),
    ("By open warfare.", +35)]},
{"prompt": "A strange pest begins to devour the crops. What’s their response?",
"choices": [
    ("Breed animals to eat the pests.", +39),
    ("Develop smoke or traps.", +40),
    ("Appease spirits with rituals.", +37),
    ("Burn the infested fields.", +37),
    ("Abandon farming entirely.", +34)]},
{"prompt": "Craftsmen appear, skilled at shaping clay and metal. What’s valued most?",
"choices": [
    ("Useful tools for work.", +40),
    ("Ornaments for trade.", +39),
    ("Weapons for defense.", +38),
    ("Symbols of status and power.", +37),
    ("Idle beauty — art for its own sake.", +37)]},
{"prompt": "Leaders emerge claiming descent from the land itself. How do the people respond?",
"choices": [
    ("Crown them as divine rulers.", +38),
    ("Serve them loyally in exchange for peace.", +39),
    ("Question their authority.", +36),
    ("Replace them with a council of farmers.", +40),
    ("Assassinate them and seize the fields.", +36)]},
{"prompt": "Trade routes form between villages. What do they carry?",
"choices": [
    ("Grain, pottery, and livestock.", +40),
    ("Stories and new ideas.", +39),
    ("Weapons and slaves.", +36),
    ("Rare herbs and dyes.", +38),
    ("Sacred relics and omens.", +37)]}]

def main_gameplay_loop(specie, named_specie, world_stats):
    global PP, scaling, Civilisation_Stats, year
    PP = globals().get("PP", 0)
    scaling = globals().get("scaling", 0.1)
    year = globals().get("year", 0)

    # Ensure civilisation stats exist
    if "Civilisation_Stats" not in globals():
        print("ERROR: Civilisation_Stats not found. Creating placeholder.")
        globals()["Civilisation_Stats"] = {
            "Progress Points": 0,
            "Era": "Wilderness Stage",
            "Population": random.randint(100, 1000),
            "Designation": named_specie,
            "Origin Species": specie
        }

    def get_question_set():
        era = Civilisation_Stats.get("Era", "Wilderness Stage")
        if era == "Wilderness Stage":
            return WILDERNESS_QUESTIONS
        elif era == "Tribal Stage":
            return TRIBAL_QUESTIONS
        else:
            print(">>> No question set for era:", era)
            return WILDERNESS_QUESTIONS

    def build_events():
        try:
            ev, used = deciding_events(specie, world_stats)
        except Exception as e:
            print("Warning: deciding_events failed, creating defaults:", e)
            ev, used = {"Natural": [], "Social": [], "Disadvantage": []}, []
        return ev, used

    events, used_events = build_events()

    def trigger_event():
        try:
            ev = event_selection(events, used_events)
            slow_print(f"\n>>> EVENT: {ev}", 0.03)
        except Exception:
            slow_print("\n>>> EVENT: Something odd happens.", 0.03)

    def call_pecra_mood():
        try:
            flavour_text()
        except Exception:
            pass

    clear()
    try:
        print_title()
    except Exception:
        if "title" in globals():
            clear()
            print(BRIGHT_GREEN + title + Style.RESET_ALL + Back.BLACK)

    input("\nPress [ENTER] to begin simulation...")

    # Start sequential loop through questions
    question_set = get_question_set()
    for q_index, question in enumerate(question_set):
        clear()
        print_title()
        print(f"=== Year {year:,} ===\n")

        # Print the prompt and choices
        print(question["prompt"] + "\n")
        for i, (text, _) in enumerate(question["choices"], start=1):
            print(f"{i}. {text}")

        num_choices = len(question["choices"])
        while True:
            try:
                raw = input(f"\nChoose your response (1–{num_choices}): ").strip()
                choice = int(raw)
                if 1 <= choice <= num_choices:
                    break
                else:
                    print(f"Please enter a number between 1 and {num_choices}.")
            except ValueError:
                print("Please enter a valid number.")

        # Apply raw PP gain (no scaling multiplier)
        base_gain = question["choices"][choice - 1][1]
        PP += base_gain
        Civilisation_Stats["Progress Points"] = PP

        # Call era progression
        try:
            scaling = era_progression(PP, scaling)
        except TypeError:
            try:
                era_progression(PP, scaling)
            except Exception:
                pass

        year += 100

        if year % 2000 == 0:    #Every 2000 years: drift world stats and rebuild events
            for stat in world_stats.values():
                drift = random.randint(-5, 5)
                stat["value"] = max(0, min(120, stat["value"] + drift))
            events, used_events = build_events()
            slow_print("\n[PECRA LOG] Planetary parameters drifted after 2000 years; events recalculated.", 0.02)

        # Call PECRA mood + trigger an event between questions
        call_pecra_mood()
        trigger_event()

        # Small status summary
        print(f"\nCurrent Era: {Civilisation_Stats.get('Era','Unknown')}")
        print(f"Progress Points: {Civilisation_Stats.get('Progress Points',0):.0f}")
        print(f"Year: {year:,}")
        input("\nPress [ENTER] to proceed...")

        # DEMO END CONDITION — changed to Industrial Stage
        if Civilisation_Stats.get("Era") == "Industrial Stage":
            clear()
            print_title()
            print("CONGRATULATIONS! You've reached the end of the demo!\n")
            print("Final statistics:\n")
            for k, v in Civilisation_Stats.items():
                print(f"{k}: {v}")
            sys.exit()

    #After looping
    clear()
    print_title()
    print("\nSimulation complete. No further data available.\n")
    for k, v in Civilisation_Stats.items():
        print(f"{k}: {v}")

    input("\nPress [ENTER] to exit simulation.")

main_gameplay_loop(specie, named_specie, world_stats)
