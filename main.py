import json

pb_config = {"a": "z", "b": "p", "c": "h", "d": "n", "e": "m", "f": "s", "g": "w", "h": "c", "j": "y", 
             "k": "t", "l": "q", "m": "e", "n": "d", "p": "b", "q": "l", "s": "f", "t": "k", "w": "g", "y": "j", "z": "a"}

fr_config = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

ring_settings = [1, 1, 1]

def plugboard(x):
    key = x.lower()
    pb = json.loads(pb_config)
    if key in pb:
        return pb[key]
    else:
        return key
    
def update_ring_settings():
    if ring_settings[0] == 26:
        if ring_settings[1] == 26:
            if ring_settings[2] == 26:
                ring_settings = [1, 1, 1]
            else:
                ring_settings = [1, 1, ring_settings[2] + 1]
        else:
            ring_settings = [1, ring_settings[1] + 1, ring_settings[2]]
    else:
        ring_settings = [ring_settings[0] + 1, ring_settings[1], ring_settings[2]]

def first_rotor(x):
    rotor_value = ring_settings[0]
    char_value = ord(x) - 96
    difference = rotor_value - char_value
    cryptic_char_value = char_value + difference
    cryptic_char = chr(cryptic_char_value + 96)
    fr = json.loads(fr_config)
    return fr[cryptic_char]



