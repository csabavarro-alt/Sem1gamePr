import time
import random

species = {
    "Rats": {
        "description": "Burrowing mammals, opportunistic feeders, fast breeders, and classic urban survivors.",
        "stats": {
            "Food Security": 75,
            "Object Utilisation": 40,
            "Mutation Capacity": 65,
            "Aggression Level": 60,
            "Social Cohesion": 55,
            "Disease Resistance": 70,
            "Resource Abundance": 80,
            "Toxicity Tolerance": 60,
            "Climate Adaptability": 75,
            "Cultural Curiosity": 50
        }
    },
    "Eagles": {
    "description": "Majestic raptors with sharp eyesight, powerful hunting skills, and strong territorial instincts.",
    "stats": {
        "Food Security": 80,
        "Object Utilisation": 25,
        "Mutation Capacity": 50,
        "Aggression Level": 75,
        "Social Cohesion": 35,
        "Disease Resistance": 65,
        "Resource Abundance": 60,
        "Toxicity Tolerance": 35,
        "Climate Adaptability": 70,
        "Cultural Curiosity": 20
    }
},
    "Cockroaches": {
        "description": "Infamous insects that can withstand radiation, hunger, and thrive almost anywhere.",
        "stats": {
            "Food Security": 85,
            "Object Utilisation": 5,
            "Mutation Capacity": 70,
            "Aggression Level": 30,
            "Social Cohesion": 40,
            "Disease Resistance": 80,
            "Resource Abundance": 90,
            "Toxicity Tolerance": 85,
            "Climate Adaptability": 90,
            "Cultural Curiosity": 10
        }
    },
    "Ants": {
        "description": "Eusocial insects with complex colonies, advanced cooperation, and large-scale engineering potential.",
        "stats": {
            "Food Security": 65,
            "Object Utilisation": 25,
            "Mutation Capacity": 60,
            "Aggression Level": 75,
            "Social Cohesion": 95,
            "Disease Resistance": 55,
            "Resource Abundance": 80,
            "Toxicity Tolerance": 55,
            "Climate Adaptability": 70,
            "Cultural Curiosity": 20
        }
    },
    "Octopuses": {
        "description": "Intelligent marine invertebrates with problem-solving skills, dexterous limbs, and camouflage abilities.",
        "stats": {
            "Food Security": 60,
            "Object Utilisation": 75,
            "Mutation Capacity": 55,
            "Aggression Level": 50,
            "Social Cohesion": 40,
            "Disease Resistance": 50,
            "Resource Abundance": 65,
            "Toxicity Tolerance": 40,
            "Climate Adaptability": 55,
            "Cultural Curiosity": 80
        }
    },
    "Fungi": {
        "description": "Spore-producing decomposers, thriving on decay, radiation, and extreme conditions.",
        "stats": {
            "Food Security": 90,
            "Object Utilisation": 0,
            "Mutation Capacity": 85,
            "Aggression Level": 10,
            "Social Cohesion": 25,
            "Disease Resistance": 95,
            "Resource Abundance": 85,
            "Toxicity Tolerance": 90,
            "Climate Adaptability": 95,
            "Cultural Curiosity": 0
        }
    },
    "Crocodiles": {
        "description": "Ancient reptiles with patience, durability, and the ability to endure harsh conditions for millennia.",
        "stats": {
            "Food Security": 70,
            "Object Utilisation": 10,
            "Mutation Capacity": 40,
            "Aggression Level": 85,
            "Social Cohesion": 35,
            "Disease Resistance": 70,
            "Resource Abundance": 55,
            "Toxicity Tolerance": 50,
            "Climate Adaptability": 75,
            "Cultural Curiosity": 15
        }
    },
    "Jellyfish": {
        "description": "Simple, hardy sea creatures, some species capable of biological immortality.",
        "stats": {
            "Food Security": 65,
            "Object Utilisation": 0,
            "Mutation Capacity": 45,
            "Aggression Level": 20,
            "Social Cohesion": 10,
            "Disease Resistance": 80,
            "Resource Abundance": 70,
            "Toxicity Tolerance": 70,
            "Climate Adaptability": 85,
            "Cultural Curiosity": 0
        }
    },
    "Mole Rats": {
        "description": "Burrowing mammals adapted to low oxygen environments and extreme climates, with colony-like behavior.",
        "stats": {
            "Food Security": 55,
            "Object Utilisation": 15,
            "Mutation Capacity": 60,
            "Aggression Level": 40,
            "Social Cohesion": 70,
            "Disease Resistance": 65,
            "Resource Abundance": 60,
            "Toxicity Tolerance": 65,
            "Climate Adaptability": 75,
            "Cultural Curiosity": 25
        }
    },
    "Tardigrades": {
        "description": "Microscopic ‘water bears,’ capable of surviving vacuum, radiation, and total desiccation.",
        "stats": {
            "Food Security": 40,
            "Object Utilisation": 0,
            "Mutation Capacity": 75,
            "Aggression Level": 5,
            "Social Cohesion": 5,
            "Disease Resistance": 95,
            "Resource Abundance": 95,
            "Toxicity Tolerance": 95,
            "Climate Adaptability": 100,
            "Cultural Curiosity": 0
        }
    },
    "Pigeons": {
        "description": "Urban scavengers who thrive wherever humans once lived, adaptable and prolific breeders.",
        "stats": {
            "Food Security": 80,
            "Object Utilisation": 30,
            "Mutation Capacity": 55,
            "Aggression Level": 35,
            "Social Cohesion": 70,
            "Disease Resistance": 65,
            "Resource Abundance": 75,
            "Toxicity Tolerance": 40,
            "Climate Adaptability": 70,
            "Cultural Curiosity": 60
        }
    },
    "Goats": {
        "description": "Stubborn, hardy mammals capable of eating almost anything and surviving rugged terrain.",
        "stats": {
            "Food Security": 75,
            "Object Utilisation": 20,
            "Mutation Capacity": 50,
            "Aggression Level": 40,
            "Social Cohesion": 65,
            "Disease Resistance": 70,
            "Resource Abundance": 60,
            "Toxicity Tolerance": 55,
            "Climate Adaptability": 80,
            "Cultural Curiosity": 35
        }
    },
    "Wolves": {
        "description": "Social predators with pack structures, intelligence, and adaptability to varied climates.",
        "stats": {
            "Food Security": 65,
            "Object Utilisation": 25,
            "Mutation Capacity": 55,
            "Aggression Level": 75,
            "Social Cohesion": 85,
            "Disease Resistance": 65,
            "Resource Abundance": 55,
            "Toxicity Tolerance": 45,
            "Climate Adaptability": 75,
            "Cultural Curiosity": 45
        }
    },
    "Elephants": {
        "description": "Large-brained mammals with long lifespans, memory, and advanced social bonds.",
        "stats": {
            "Food Security": 60,
            "Object Utilisation": 60,
            "Mutation Capacity": 45,
            "Aggression Level": 50,
            "Social Cohesion": 90,
            "Disease Resistance": 55,
            "Resource Abundance": 50,
            "Toxicity Tolerance": 35,
            "Climate Adaptability": 65,
            "Cultural Curiosity": 85
        }
    },
    "Ravens": {
        "description": "Cousins of crows, with even higher problem-solving skills and mythic resilience.",
        "stats": {
            "Food Security": 70,
            "Object Utilisation": 85,
            "Mutation Capacity": 55,
            "Aggression Level": 45,
            "Social Cohesion": 65,
            "Disease Resistance": 60,
            "Resource Abundance": 70,
            "Toxicity Tolerance": 45,
            "Climate Adaptability": 70,
            "Cultural Curiosity": 90
        }
    },
    "Squids": {
        "description": "Marine hunters with intelligence, fast growth, and rapid adaptation.",
        "stats": {
            "Food Security": 70,
            "Object Utilisation": 65,
            "Mutation Capacity": 70,
            "Aggression Level": 60,
            "Social Cohesion": 40,
            "Disease Resistance": 50,
            "Resource Abundance": 65,
            "Toxicity Tolerance": 40,
            "Climate Adaptability": 60,
            "Cultural Curiosity": 75
        }
    },
    "Lizards": {
        "description": "Cold-blooded survivors, highly adaptable and widespread across all climates.",
        "stats": {
            "Food Security": 60,
            "Object Utilisation": 15,
            "Mutation Capacity": 65,
            "Aggression Level": 40,
            "Social Cohesion": 30,
            "Disease Resistance": 70,
            "Resource Abundance": 80,
            "Toxicity Tolerance": 55,
            "Climate Adaptability": 85,
            "Cultural Curiosity": 20
        }
    },
    "Bats": {
        "description": "Nocturnal flyers with echolocation, colony organisation, and virus tolerance.",
        "stats": {
            "Food Security": 65,
            "Object Utilisation": 25,
            "Mutation Capacity": 60,
            "Aggression Level": 35,
            "Social Cohesion": 75,
            "Disease Resistance": 90,
            "Resource Abundance": 70,
            "Toxicity Tolerance": 60,
            "Climate Adaptability": 80,
            "Cultural Curiosity": 40
        }
    },
    "Squat Lobsters": {
        "description": "Resilient crustaceans dwelling in deep seas, scavenging and withstanding pressure extremes.",
        "stats": {
            "Food Security": 55,
            "Object Utilisation": 10,
            "Mutation Capacity": 50,
            "Aggression Level": 30,
            "Social Cohesion": 25,
            "Disease Resistance": 75,
            "Resource Abundance": 80,
            "Toxicity Tolerance": 65,
            "Climate Adaptability": 85,
            "Cultural Curiosity": 15
        }
    },
    "Slime Moulds": {
        "description": "Uncanny amoeboid organisms capable of collective intelligence and navigating mazes without brains.",
        "stats": {
            "Food Security": 85,
            "Object Utilisation": 5,
            "Mutation Capacity": 80,
            "Aggression Level": 0,
            "Social Cohesion": 45,
            "Disease Resistance": 80,
            "Resource Abundance": 85,
            "Toxicity Tolerance": 85,
            "Climate Adaptability": 95,
            "Cultural Curiosity": 30
        }
    }
}

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def boot_sequence():
    slow_print(">>> INITIALISING P.E.C.R.A. SIMULATION...", 0.03)
    time.sleep(1)
    slow_print(">>> USER DETECTED. TESTING PROTOCOL COMMENCING...", 0.03)
    time.sleep(1)
    slow_print(">>> LOADING BIOSPHERE TEMPLATES...", 0.03)
    time.sleep(1)
    slow_print(">>> GENERATING SURVIVOR CANDIDATES...", 0.03)
    print("\n")

def planet_scan():
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
        "Disease Prevalence": {"value": random.randint(0, 90), "positive": False}}

    slow_print(">>> PLANETARY ASSESSMENT:", 0.02)
    time.sleep(1.5 )
    for stat, data in stats.items():
        val = data["value"]
        bar = "█" * (val // 10) + "░" * (10 - val // 10)
        print(f" - {stat:22}: {bar} {val}%")

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
    print(f"\n - Conclusion: {conclusion}")
    return habitability

boot_sequence()
habitability = planet_scan()

def specie_selection(habitability):
    tiered_species = {
        4: ["Elephants", "Ravens", "Eagles", "Octopuses", "Squids"],
        3: ["Wolves", "Goats", "Pigeons", "Bats", "Rats"],
        2: ["Crocodiles", "Lizards", "Ants", "Mole Rats", "Cockroaches"],
        1: ["Tardigrades", "Fungi", "Slime Moulds", "Jellyfish", "Squat Lobsters"]}
    candidate_selection = random.sample(tiered_species[habitability], 3)
    while True:
        candidate_choice = input(f"\n - Choose a specie from {', '.join(candidate_selection)}: ")
        match = None
        for c in candidate_selection:
            if candidate_choice.lower() == c.lower():
                match = c
                break
        if match:
            chosen = match
            print(f"\n - {chosen}: {species[chosen]['description']}")
            print(" - Stats:")
            for stat, val in species[chosen]["stats"].items():
                print(f"    {stat}: {val}")

            affirmation = input(f"\n - Are you sure? (Y/N): ")
            if affirmation.lower() == "y":
                print(f"\n - You chose {chosen}")
                return chosen
            else:
                print(" - Select again")
        else:
            print(" - Please select a specie from the available selection")

specie = specie_selection(habitability)
