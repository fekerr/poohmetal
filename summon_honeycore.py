import toml
import zlib

# Load the compressed saga from the TOML file
with open("honeycore_saga.toml", "r") as file:
    data = toml.load(file)

compressed_data = data["session"]["compressed_data"]

# Decompression function
def unleash_honeycore(compressed_data):
    return zlib.decompress(compressed_data.encode()).decode("utf-8")

# Summon the full saga
print(unleash_honeycore(compressed_data))
