from ideas import generate_ideas

print("Creator AI Toolkit")

niche = input("Ta niche : ")

ideas = generate_ideas(niche)

for idea in ideas:
    print("-", idea)
