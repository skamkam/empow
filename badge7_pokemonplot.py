# Start with your imports
import pandas as pd
import matplotlib.pyplot as plt

# This loads from the file
pokemons = pd.read_csv("pokemon.csv")

# Only keep the generation 1 pokemon
pokemons = pokemons.loc[pokemons["generation"] == 1]

# create lists of atk hp and labels
atk = pokemons["attack"]
hp = pokemons["hp"]
labels = pokemons["name"]

# create the plots
fig, ax = plt.subplots()
ax.scatter(atk, hp)

# Set title and axis labels
ax.set_xlabel("Attack (HP)")
ax.set_ylabel("Health (HP)")
ax.set_title("Attack vs Health of Gen 1 Pokemon")

for i, txt in enumerate(labels):
    ax.annotate(txt, (atk[i], hp[i]))

# Show the plot
plt.show()