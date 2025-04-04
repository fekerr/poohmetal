import toml
import zlib

# Load compressed ASCII art from the TOML file
with open("honeycore_saga.toml", "r") as file:
    data = toml.load(file)

# Function to decompress and summon ASCII chaos
def summon_ascii_art(tag):
    compressed_data = data["ascii_art"].get(tag)
    if compressed_data:
        return zlib.decompress(compressed_data.encode()).decode("utf-8")
    return "No epic ASCII art found for that tag!"

# Example: Print Pooh’s final throne
print(summon_ascii_art("honeycore_throne"))
