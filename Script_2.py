from pyvis.network import Network
import json
import random

File = "global_network.json"


def get_data(file):
    with open(file, "r") as json_file:
        data = json.load(json_file)
        return data


def map_countries(data):
    g = Network(height="720px", width="100%",
                bgcolor="#2B2E4A", font_color="white", select_menu=True, )

    unique_colors = set()
    added_countries = set()
    added_populations = set()
    for nation in data:
        country = nation["country_name"]

        # Generate a unique color for each country node
        color = generate_unique_color(unique_colors)
        population = nation["Population (2020)"]

        if country not in added_countries and population not in added_populations:
            size = generate_node_size(population)
            g.add_node(country, color=color, labelhighlight=color, size=size, borderWidth=(
                size // 100), borderWidthSelected=(size // 10))
            added_countries.add(country)

        borders = nation["country_border_name"]
        if borders != "":
            if borders in added_countries:
                g.add_edge(country, borders, color="#903749", value=2)

    g.force_atlas_2based(gravity=-70)
    # g.inherit_edge_colors(True)
    # g.show_buttons(filter_=["physics", "edges"])
    g.write_html("Global_network.html")


def generate_unique_color(unique_colors):
    while True:
        # Generate a random hex color code
        color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        if color not in unique_colors:
            unique_colors.add(color)
            return color


def generate_node_size(population, threshold=1000000, default_size=10, max_size=180):
    population = int(float(population))
    if population < threshold:
        size = default_size
    else:
        size = population // (397628 * 5)
        if size < default_size:
            size = default_size
        elif size > max_size:
            size = max_size
    return size


global_data = get_data(File)
map_countries(global_data)
