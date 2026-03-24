from BaseClasses import ItemClassification
#"x button icon" 0x808878f8 - 32bit
#"camera reel 1" 0x80888fbc - 32bit for each picture
#"ship access" 0x80888a58
#pearlcount 0x8088848c (keep same as mammago)
#pearlcount for mammago 0x8088bef4


class AnimalPic:
    """loc is vanilla location
    value is ingame value
    ItemID is archipelago itemcode
    """
    #memloc is 0x80888fbc start, +0x4 per picture
    memvalue: int
    ItemID: int
    classification: ItemClassification.progression
    ItemType = "Picture"


Pics_h: dict[str, AnimalPic] = {
    "Canis Canis":  AnimalPic(0x1,   1),
    "Aedes Raymanis":   AnimalPic(0x2,    2),
    "Rattus Giganteus": AnimalPic(0x3,  3),
    "Amoeba Polypodia": AnimalPic(0x4,  4),
    "Anemonia Mutabilis":   AnimalPic(0x5,    5),
    "Timorea Saponifera":   AnimalPic(0x6,    6),
    "Cyclopeus Palustris":  AnimalPic(0x7,   7),
    "Priodontes Campestris":    AnimalPic(0X8, 8),
    "Adalia Octopunctata":  AnimalPic(0X9,  9),
    "Rhinoceros Sapiens":   AnimalPic(0xa,  10),
    "Megaptera Anaerobia":  AnimalPic(0xb,  11),
    "Palinurus Rupestris":  AnimalPic(0xc,  12),
    "Cyanea Urtica":    AnimalPic(0xd,  13),
    "Larus Albus":  AnimalPic(0xe,  14),
    "Koi Kumonryu": AnimalPic(0xf,  15),
    "Lampyris Campestris":  AnimalPic(0x10, 16),
    "Helix Rupestris":  AnimalPic(0x11, 17),
    "Anguilla Bifida":  AnimalPic(0x12, 18),
    "Megaptera Borealis":   AnimalPic(0x13, 19),
    "Pelagia Pachydermis":  AnimalPic(0x14, 20),
    "Nautilus Fluoreus":    AnimalPic(0x15, 21),
    "Crochax Velox":    AnimalPic(0x16, 22),
    "Vorax Nocturnis":  AnimalPic(0x17, 23),
    "Blabera Gregaria": AnimalPic(0x18, 24),
    "Ignis Ignifera":   AnimalPic(0x19, 25),
    "Teratosaurus Imperator":   AnimalPic(0x1a, 26),
    "Aurelia Magnificens":  AnimalPic(0x1b, 27),
    "Trilobites Saltans":   AnimalPic(0x1c, 28),
    "Arachnis Viridis": AnimalPic(0x1d, 29),
    "Pterolimax Gigantea":  AnimalPic(0x1e, 30),
    "Rascax Caeruleus": AnimalPic(0x1f, 31),
    "Dipneustes Trilineatus":   AnimalPic(0x20, 32),
    "Musca Saprophagia":    AnimalPic(0x21, 33),
    "Planaria Rupestris":   AnimalPic(0x22, 34),
    "Lycoperdon Fugiferus": AnimalPic(0x23, 35),
    "Sarcophagus Domzii":   AnimalPic(0x24, 36),
    "Taurus Sapiens":   AnimalPic(0x25, 37),
    "Astacus Erectus":  AnimalPic(0x26, 38),
    "Amoeba Saltans":   AnimalPic(0x27, 39),
    "Carcharodon Sapiens":  AnimalPic(0x28, 40),
    "Rattus Albus": AnimalPic(0x29, 41),
    "Bufo Erectus": AnimalPic(0x2a, 42),
    "Papilio Pilosus":  AnimalPic(0x2b, 43),
    "Lutra Erecta": AnimalPic(0x2c, 44),
    "Macropodia Omnivora":  AnimalPic(0x2d, 45),
    "Homo Sapiens": AnimalPic(0x2e, 46),
    "Megaptera Purpurea":   AnimalPic(0x2f, 47),
    "Manta Cyanea": AnimalPic(0x30, 48),
    "Sus Sapiens":  AnimalPic(0x31, 49),
    "Alicia Splendens": AnimalPic(0x32, 50),
    "Manta Magnificens":    AnimalPic(0x33, 51),
    "Felis Sapiens":    AnimalPic(0x34, 52),
    "Walrus Sapiens":   AnimalPic(0x35, 53),
    "Aquilus Sapiens":  AnimalPic(0x36, 54),
    "Capra Sapiens":    AnimalPic(0x37, 55),
    "Spongus Gluanteus": AnimalPic(0x38,    56),
}

class MDisk:
#bitfield
    memvalue: int
    ItemID: int
    classification: ItemClassification.progression
    memloc = 0x8088922c
    ItemType = "MDisk"

Disks = {
    "1 - Game Save": MDisk(1,    57),
    "2 - Mr De Castellac":  MDisk(8,    58),
    "3 - The Pearl and The Currents": MDisk(4,  59),
    "4 - For Jade": MDisk(0x10, 60),
    "5 - Surveillance Camera":  MDisk(0x800,    61),
    "6 - Hillyan Army Databank":    MDisk(2,    62),
    "7 - Beluga Check-up":  MDisk(0x400,    63),
    "8 - Animal Species":   MDisk(0x20, 64),
    "9 - Iris 511": MDisk(0x40, 65),
    "10 - Iris 512":    MDisk(0x80, 66),
    "11 - Iris 513":    MDisk(0x100,    67),
    "12 - Iris 514":    MDisk(0x200,    68),
    "13 - Disk Game":   MDisk(0X1000,   69),
}

class KeyItem:
    memloc: int
    memvalue: int
    ItemID: int
    classification: ItemClassification.progression

KeyItems = {
    "Dai-jo":   KeyItem(0x808883e8, 1,  70),
    "Camera":   KeyItem(0x808883d8, 1,  71),
    "Pearl":    KeyItem(0x8088848c&0x8088bef4,  1,  72)
}

class DiskCheck:
    memloc: int
    memvalue: int

DiskChecks = {
    "PeyJ's Workshop MDisk":    DiskCheck(0x80888a61,   4)
}

class ShipPart:
    memvalue: int
    ItemID: int
    memloc = 0x8088848c

ShipParts = {
    "Speedcraft Motor": ShipPart(2, )

}

class Junk:
    memloc: int
    memvalue: int
    ItemID: int | None

JunkItems = {
    "Starkos":  Junk(0x80888450,    1,  ),
    "P-O-D":    Junk(0x80888414,    1,  ),
    "Mecha Impulser":   Junk(),
    "Boost":    Junk(0x8088846c,    1,  ),
    "Health":   Junk(0x80887c68,    1,  ), #float
    "Credits":  Junk(0x80887c78,    1,  ),
}
