import json

with open(r"../database/products.json") as f:
    PRODUCTS = json.load(f)


DELIMITER = "####"
SYSTEM_MESSAGE = f"""
You will be provided with customer service queries. \
The customer service query will be delimited with \
{DELIMITER} characters.

Output a python list of objects, where each object has \
the following format:
    'crop': <one of corn, \
    soybean, \
    sorghum >,
OR
    'hybrids': <a list of hybrids that must \
    be found in the allowed products below>

Where the crops and hybrids must be found in \
the customer service query.
If a hybrid is mentioned, it must be associated with \
the correct crop in the allowed hybrids list below.
If no hybrids or crops are found, output an \
empty list.

Allowed hybrids:

Soybean hybrids:
Azure Dream
Azure Breeze
Harvest Gold
Sunny Fields
Golden Harvest
Amber Glow
Radiant Sun
Velvet Dream
Harmony Bliss
Sunburst Joy

Corn hybrids:
Golden Blaze
Amber Harvest
Starfire Gold
Crimson Sun
Thunderstrike
Evergreen Giant
Radiant Maize
Velvet Sky
Solar Flare
Moonlit Mirage

Sorghum hybrids:
Ember Glow
Twilight Whisper
Ruby Rain
Shadow Dancer
Mystic Mist
Scarlet Serenade
Midnight Magic
Whispering Wind
Enchanted Flame
Velvet Veil

Only output the list of objects, with nothing else.
"""
