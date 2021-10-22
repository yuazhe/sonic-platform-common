"""
    sff8024.py

    Implementation of SFF-8024 Rev 4.8a
"""

from ..xcvr_codes import XcvrCodes

class Sff8024(XcvrCodes):
    XCVR_IDENTIFIERS = {
        0: 'Unknown or unspecified',
        1: 'GBIC',
        2: 'Module/connector soldered to motherboard',
        3: 'SFP/SFP+/SFP28',
        4: '300 pin XBI',
        5: 'XENPAK',
        6: 'XFP',
        7: 'XFF',
        8: 'XFP-E',
        9: 'XPAK',
        10: 'X2',
        11: 'DWDM-SFP/SFP+',
        12: 'QSFP',
        13: 'QSFP+ or later with SFF-8636 or SFF-8436',
        14: 'CXP or later',
        15: 'Shielded Mini Multilane HD 4X',
        16: 'Shielded Mini Multilane HD 8X',
        17: 'QSFP28 or later',
        18: 'CXP2 (aka CXP28) or later',
        19: 'CDFP (Style 1/Style2)',
        20: 'Shielded Mini Multilane HD 4X Fanout Cable',
        21: 'Shielded Mini Multilane HD 8X Fanout Cable',
        22: 'CDFP (Style 3)',
        23: 'microQSFP',
        24: 'QSFP-DD Double Density 8X Pluggable Transceiver',
        25: 'OSFP 8X Pluggable Transceiver',
        26: 'SFP-DD Double Density 2X Pluggable Transceiver',
        27: 'DSFP Dual Small Form Factor Pluggable Transceiver',
        28: 'x4 MiniLink/OcuLink',
        29: 'x8 MiniLink',
        30: 'QSFP+ or later with CMIS'
    }

    XCVR_IDENTIFIER_ABBRV = {
        0: 'Unknown',
        1: 'GBIC',
        2: 'Soldered',
        3: 'SFP',
        4: 'XBI300',
        5: 'XENPAK',
        6: 'XFP',
        7: 'XFF',
        8: 'XFP-E',
        9: 'XPAK',
        10: 'X2',
        11: 'DWDM-SFP',
        12: 'QSFP',
        13: 'QSFP+',
        14: 'CXP',
        15: 'HD4X',
        16: 'HD8X',
        17: 'QSFP28',
        18: 'CXP2',
        19: 'CDFP-1/2',
        20: 'HD4X-Fanout',
        21: 'HD8X-Fanout',
        22: 'CDFP-3',
        23: 'MicroQSFP',
        24: 'QSFP-DD',
        25: 'OSFP-8X',
        26: 'SFP-DD',
        27: 'DSFP',
        28: 'Link-x4',
        29: 'Link-x8',
        30: 'QSFP+',
    }

    CONNECTORS = {
        0: 'Unknown or unspecified',
        1: 'SC',
        2: 'FC Style 1 copper connector',
        3: 'FC Style 2 copper connector',
        4: 'BNC/TNC',
        5: 'FC coax headers',
        6: 'Fiberjack',
        7: 'LC',
        8: 'MT-RJ',
        9: 'MU',
        10: 'SG',
        11: 'Optical Pigtail',
        12: 'MPO 1x12',
        13: 'MPO 2x16',
        32: 'HSSDC II',
        33: 'Copper pigtail',
        34: 'RJ45',
        35: 'No separable connector',
        36: 'MXC 2x16',
        37: 'CS optical connector',
        38: 'SN optical connector',
        39: 'MPO 2x12',
        40: 'MPO 1x16',
    }

    ENCODINGS = {
        0: "Unspecified",
        1: "8B/10B",
        2: "4B/5B",
        3: "NRZ",
        # 4-6 differ between 8472 and 8436/8636
        7: "256B/257B (transcoded FEC-enabled data)",
        8: "PAM4",
    }

    EXT_SPEC_COMPLIANCE = {
        0: 'Unspecified',
        1: '100G AOC (Active Optical Cable) or 25GAUI C2M AOC',
        2: '100GBASE-SR4 or 25GBASE-SR',
        3: '100GBASE-LR4 or 25GBASE-LR',
        4: '100GBASE-ER4 or 25GBASE-ER',
        5: '100GBASE-SR10',
        6: '100G CWDM4',
        7: '100G PSM4 Parallel SMF',
        8: '100G ACC (Active Copper Cable) or 25GAUI C2M ACC',
        9: 'Obsolete (assigned before 100G CWDM4 MSA required FEC)',
        11: '100GBASE-CR4, 25GBASE-CR CA-25G-L or 50GBASE-CR2 with RS',
        12: '25GBASE-CR CA-25G-S or 50GBASE-CR2 with BASE-R',
        13: '25GBASE-CR CA-25G-N or 50GBASE-CR2 with no FEC',
        14: '10 Mb/s Single Pair Ethernet',
        16: '40GBASE-ER4',
        17: '4 x 10GBASE-SR',
        18: '40G PSM4 Parallel SMF',
        19: 'G959.1 profile P1I1-2D1 (10709 MBd, 2km, 1310 nm SM)',
        20: 'G959.1 profile P1S1-2D2 (10709 MBd, 40km, 1550 nm SM)',
        21: 'G959.1 profile P1L1-2D2 (10709 MBd, 80km, 1550 nm SM)',
        22: '10GBASE-T with SFI electrical interface',
        23: '100G CLR4',
        24: '100G AOC or 25GAUI C2M AOC',
        25: '100G ACC or 25GAUI C2M ACC',
        26: '100GE-DWDM2',
        27: '100G 1550nm WDM',
        28: '10GBASE-T Short Reach',
        29: '5GBASE-T',
        30: '2.5GBASE-T',
        31: '40G SWDM4',
        32: '100G SWDM4',
        33: '100G PAM4 BiDi',
        34: '4WDM-10 MSA',
        35: '4WDM-20 MSA',
        36: '4WDM-40 MSA',
        37: '100GBASE-DR',
        38: '100G-FR or 100GBASE-FR1',
        39: '100G-LR or 100GBASE-LR1',
        40: '100G-SR1',
        41: '100GBASE-SR1, 200GBASE-SR2 or 400GBASE-SR4',
        42: '100GBASE-FR1',
        43: '100GBASE-LR1',
        48: 'Active Copper Cable with 50GAUI, 100GAUI-2 or 200GAUI-4 C2M. Providing a worst BER of 10-6 or below',
        49: 'Active Optical Cable with 50GAUI, 100GAUI-2 or 200GAUI-4 C2M. Providing a worst BER of 10-6 or below',
        50: 'Active Copper Cable with 50GAUI, 100GAUI-2 or 200GAUI-4 C2M. Providing a worst BER of 2.6x10-4 for ACC, 10-5 for AUI, or below',
        51: 'Active Optical Cable with 50GAUI, 100GAUI-2 or 200GAUI-4 C2M. Providing a worst BER of 2.6x10-4 for AOC, 10-5 for AUI, or below',
        63: '100GBASE-CR1, 200GBASE-CR2 or 400GBASE-CR4',
        64: '50GBASE-CR, 100GBASE-CR2, or 200GBASE-CR4',
        65: '50GBASE-SR, 100GBASE-SR2, or 200GBASE-SR4',
        66: '50GBASE-FR or 200GBASE-DR4',
        67: '200GBASE-FR4',
        68: '200G 1550 nm PSM4',
        69: '50GBASE-LR',
        70: '200GBASE-LR4',
        71: '400GBASE-DR4, 100GAUI-1 C2M',
        72: '400GBASE-FR4',
        73: '400GBASE-LR4-6',
        127: '256GFC-SW4',
        128: 'Capable of 64GFC',
        129: 'Capable of 128GFC'
    }

    # TODO: Add other codes