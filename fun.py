from math import inf

klasse_formaten = {
    'brievenbus':
        {'afmeting':[35,25,3], 'gewicht':[0,2]},
    'S':
        {'afmeting':[22,20,15], 'gewicht':[0,2]},
    'M':
        {'afmeting':[30,22,25], 'gewicht':[2,5]},
    'L':
        {'afmeting':[42,30,20], 'gewicht':[5,10]},
    'XL':
        {'afmeting':[60,40,40], 'gewicht':[10,20]},
    'XXL':
        {'afmeting':[inf, inf, inf], 'gewicht':[20, inf]},        
}

klasse_tarieven = {
    'brievenbus':
        [5.5, 5.25, 5],
    'S':
        [7.75, 7.5, 7.25],
    'M':
        [8.25, 8, 7.75],
    'L':
        [8.75, 8.5, 8.25],
    'XL':
        [9.5, 9.25, 9],
    'XXL':
        [12.5, 12.25, 12],        
}



def klasse_volgens_afmetingen(afmeting):
    for klasse in klasse_formaten.keys():
        #afmetingen = klasse_formaten[klasse]
        klasse_afmetingen = klasse_formaten[klasse]['afmeting']
        
        klasse_afmetingen_op_volgorde = sorted(klasse_afmetingen,reverse=True)
        afmetingen_op_volgorde = sorted(afmeting, reverse=True)
        
        alle_dimensies = [afmetingen_op_volgorde[i] <= klasse_afmetingen_op_volgorde[i] for i in range(3)]

        
        if all(alle_dimensies):
            return klasse
        

def klasse_volgens_gewicht(gewicht):
    for klasse in klasse_formaten.keys():
        #afmetingen = klasse_formaten[klasse]
        gewichten = klasse_formaten[klasse]['gewicht']
        
        if (gewicht>=gewichten[0]) & (gewicht<=gewichten[1]):
            return klasse
        
        
def andor(a, b):
    return any([a and b, a or b])

volgorde = list(klasse_tarieven.keys())
flipped_volgorde = volgorde[::-1]

def twee_klasses_naar_hoogste(klasse1, klasse2):
    for klasse in flipped_volgorde:
        if andor(klasse==klasse1, klasse==klasse2):
            return klasse
        
        
def omvang_naar_klasse(afmetingen: list, gewicht: float) -> str:
    volgens_afmetingen = klasse_volgens_afmetingen(afmetingen)
    volgens_gewicht = klasse_volgens_gewicht(gewicht)
    return twee_klasses_naar_hoogste(volgens_afmetingen, volgens_gewicht)


def klasse_en_afzet_naar_bedrag(klasse:str, afzet:int) -> dict:
    
    tarieven = klasse_tarieven[klasse]
    
    if afzet < 25:
        totaal = tarieven[0] * afzet
    elif afzet < 50:
        totaal = tarieven[1] * afzet
    elif afzet < 100:
        totaal = tarieven[2] * afzet
    else:
        return None
        
    return {'totaal':round(totaal,2), 'per_product':round(totaal / afzet,2)}  

def sales_naar_bedrag(afmetingen: list, gewicht: float, afzet: int) -> dict:
    klasse = omvang_naar_klasse(afmetingen, gewicht)
    output = klasse_en_afzet_naar_bedrag(klasse, afzet)
    output['klasse'] = klasse
    return output