from math import inf

formaten_per_klasse = {
    'XXXXS':150,
    'XXXS':1776,
    'XXS':2886,
    'XS': 5200,
    'S':10_800,
    'M':38_500,
    'L':147_600,
    'XL':240_000,
    'XXL':inf
}


prijzen_per_klasse = {
    'XXXXS':0.001,
    'XXXS':0.01,
    'XXS':0.02,
    'XS': 0.04,
    'S': 0.05,
    'M': 0.08,
    'L': 0.1,
    'XL': 0.18,
    'XXL': 0.25
}


def formaten_naar_klasse(formaten:list) -> str:
    som = formaten[0] * formaten[1] * formaten[2]
    for klasse in formaten_per_klasse.keys():
        if som < formaten_per_klasse[klasse]:
            return klasse
        
        
klasse_naar_prijs = lambda klasse: prijzen_per_klasse[klasse]