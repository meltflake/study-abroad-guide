#!/usr/bin/env python3
"""Add studentFacultyRatio, internationalRate, graduationRateNum to all schools."""
import json, glob

# Known data for major schools (studentFacultyRatio, internationalRate%, graduationRate%)
KNOWN = {
    # US
    'harvard': (6, 25, 98), 'mit': (3, 33, 96), 'stanford': (5, 24, 96),
    'princeton': (5, 24, 98), 'yale': (6, 22, 97), 'caltech': (3, 33, 94),
    'uchicago': (5, 28, 95), 'columbia': (6, 33, 96), 'upenn': (6, 22, 96),
    'duke': (6, 20, 96), 'northwestern': (6, 20, 95), 'jhu': (7, 27, 94),
    'dartmouth': (7, 15, 96), 'brown': (6, 16, 96), 'cornell': (9, 25, 95),
    'rice': (6, 18, 93), 'vanderbilt': (7, 14, 93), 'notre-dame': (10, 7, 96),
    'georgetown': (11, 17, 95), 'ucla': (18, 16, 92), 'uc-berkeley': (20, 17, 93),
    'berkeley': (20, 17, 93), 'ucsd': (19, 22, 88), 'ucsb': (18, 15, 84),
    'ucd': (20, 16, 86), 'ucdavis': (20, 16, 86), 'uci': (18, 19, 87),
    'ucirvine': (18, 19, 87), 'umich': (12, 17, 93), 'uva': (15, 11, 95),
    'cmu': (5, 42, 93), 'nyu': (9, 30, 87), 'georgia-tech': (18, 19, 90),
    'uiuc': (20, 23, 87), 'ut-austin': (18, 12, 84), 'utaustin': (18, 12, 84),
    'uw-madison': (17, 14, 88), 'uwmadison': (17, 14, 88),
    'purdue': (13, 23, 82), 'ohio-state': (19, 14, 84), 'osu': (19, 14, 84),
    'penn-state': (16, 15, 86), 'pennstate': (16, 15, 86),
    'uf': (17, 8, 90), 'unc': (13, 9, 91), 'bu': (10, 27, 89),
    'northeastern': (14, 23, 90), 'usc': (9, 24, 92), 'emory': (9, 20, 91),
    'tufts': (9, 18, 93), 'wake-forest': (11, 10, 91),
    'william-mary': (12, 9, 91), 'brandeis': (10, 22, 90),
    'case-western': (11, 23, 85), 'tulane': (8, 12, 84),
    'indiana': (16, 16, 79), 'wustl': (7, 20, 95), 'urochester': (10, 28, 88),
    'uwash': (20, 18, 84), 'umiami': (12, 19, 83), 'umin': (17, 13, 82),
    'umaryland': (18, 15, 87), 'msu': (16, 15, 80), 'ucolo': (18, 10, 72),
    'scu': (11, 9, 91), 'arizona': (16, 12, 65), 'asu': (22, 12, 69),
    'stonybrook': (19, 24, 76), 'rutgers': (16, 18, 81),
    'lehigh': (10, 14, 89), 'rpi': (13, 22, 86), 'uconn': (16, 11, 84),
    'clemson': (16, 5, 84), 'stevens': (10, 20, 83), 'villanova': (11, 5, 91),
    'drexel': (11, 16, 74), 'smu': (11, 15, 82), 'fordham': (14, 11, 82),
    'temple': (14, 10, 73), 'tamu': (19, 10, 82), 'upitt': (14, 13, 83),
    # US Art schools
    'risd': (9, 33, 89), 'parsons': (9, 47, 78), 'saic': (9, 35, 72),
    'pratt': (10, 30, 69), 'calarts': (7, 28, 76), 'scad': (17, 25, 68),
    # UK
    'oxford': (10, 46, 97), 'cambridge': (11, 39, 97), 'imperial': (11, 60, 93),
    'ucl': (10, 52, 90), 'lse': (12, 70, 90), 'edinburgh': (13, 47, 87),
    'kcl': (12, 49, 86), 'manchester': (14, 42, 86), 'bristol': (14, 32, 89),
    'warwick': (13, 40, 89), 'glasgow': (16, 35, 85), 'leeds': (15, 30, 86),
    'sheffield': (14, 34, 85), 'birmingham': (15, 30, 87), 'southampton': (14, 32, 85),
    'nottingham': (14, 28, 87), 'liverpool': (14, 30, 85), 'exeter': (14, 30, 90),
    'newcastle': (14, 30, 86), 'cardiff': (16, 27, 85), 'bath': (14, 33, 91),
    'stAndrews': (11, 45, 92), 'durham': (12, 30, 92), 'york': (14, 28, 87),
    'lancaster': (14, 30, 86), 'lboro': (15, 20, 89), 'surrey': (15, 25, 85),
    'sussex': (14, 32, 82), 'reading': (15, 28, 83), 'qmul': (15, 45, 82),
    'leicester': (14, 28, 83), 'aberdeen': (14, 35, 82), 'qub': (15, 22, 85),
    'dundee': (13, 25, 83), 'royalholloway': (14, 38, 85), 'uea': (14, 28, 84),
    'heriotwatt': (16, 35, 78), 'strathclyde': (16, 22, 82),
    'swansea': (16, 22, 80), 'brunel': (16, 30, 78), 'kent': (16, 28, 80),
    'coventry': (18, 35, 76), 'aston': (16, 32, 80), 'huddersfield': (18, 20, 75),
    'ulster': (18, 15, 78), 'keele': (16, 15, 82), 'derby': (20, 18, 70),
    'plymouth': (18, 15, 75), 'city': (16, 48, 78), 'essex': (16, 40, 78),
    'greenwich': (20, 35, 70), 'westminster': (18, 45, 68),
    'soas': (11, 55, 82), 'birkbeck': (18, 30, 72), 'brunel': (16, 30, 78),
    # UK Art schools
    'ual': (16, 55, 80), 'goldsmiths': (14, 40, 78), 'gsa': (12, 30, 82),
    # AU
    'umelb': (22, 47, 85), 'usyd': (18, 35, 86), 'anu': (14, 38, 85),
    'unsw': (16, 40, 84), 'uq': (18, 30, 82), 'monash': (18, 40, 82),
    'uwa': (16, 28, 82), 'adelaide': (18, 35, 80), 'uts': (20, 32, 78),
    'macquarie': (20, 30, 78), 'qut': (22, 18, 76), 'rmit': (22, 35, 72),
    'curtin': (22, 30, 74), 'deakin': (22, 22, 75), 'wollongong': (18, 32, 76),
    'unisa': (22, 20, 72), 'tasmania': (20, 25, 70), 'western-sydney': (25, 28, 68),
    'murdoch': (22, 25, 70), 'bond': (10, 40, 82), 'scu_au': (22, 18, 68),
    'canberra': (22, 20, 70), 'cqu': (25, 18, 65), 'ecu': (22, 15, 70),
    'vic': (22, 22, 72), 'charles-darwin': (22, 22, 65),
    'latrobe': (20, 28, 72), 'griffith': (22, 25, 73), 'flinders': (18, 25, 74),
    'utas': (20, 22, 70), 'unewcastle': (18, 20, 76), 'swinburne': (20, 28, 72),
    'jcu': (20, 18, 72),
    # AU Art schools
    'nida': (8, 15, 90), 'vca': (12, 20, 85),
    # CA
    'utoronto': (16, 25, 87), 'mcgill': (16, 30, 85), 'ubc': (16, 28, 86),
    'uwaterloo': (18, 28, 84), 'western': (18, 18, 87), 'queens': (16, 14, 90),
    'mcmaster': (18, 18, 84), 'ualberta': (18, 22, 80), 'uottawa': (22, 20, 82),
    'ucalgary': (18, 20, 78), 'dalhousie': (18, 18, 78), 'usask': (18, 16, 75),
    'umanitoba': (20, 18, 76), 'uvic': (18, 20, 80), 'sfu': (20, 25, 78),
    'concordia': (22, 20, 72), 'carleton': (20, 18, 78), 'ryerson': (22, 20, 74),
    'laurier': (22, 12, 78), 'brock': (22, 12, 75),
    'yorku': (22, 22, 72), 'guelph': (20, 12, 82), 'uwinnipeg': (22, 14, 70),
    'unb': (16, 18, 76), 'uregina': (20, 15, 72), 'ulethbridge': (20, 14, 72),
    'lakehead': (22, 10, 68), 'trent': (18, 10, 78), 'acadia': (16, 14, 76),
    'mta': (16, 12, 78), 'stfx': (16, 8, 80), 'upei': (18, 18, 74),
    'nipissing': (18, 8, 74), 'laurentian': (22, 10, 68), 'brandon': (20, 12, 65),
    'cape-breton': (18, 22, 62), 'algoma': (20, 15, 60),
    'mun': (18, 16, 72), 'wnmu': (18, 10, 65), 'uoit': (20, 12, 75),
    # SG
    'nus': (12, 35, 92), 'ntu_sg': (14, 30, 90), 'smu_sg': (15, 35, 88),
    'sutd': (10, 30, 90), 'sit': (18, 10, 85), 'sim': (20, 35, 78),
    # HK
    'hku': (12, 50, 90), 'cuhk': (12, 35, 88), 'hkust': (12, 40, 90),
    'polyu': (16, 30, 82), 'cityu': (14, 45, 85), 'hkbu': (16, 28, 80),
    # CN
    'tsinghua': (12, 12, 97), 'pku': (10, 15, 96), 'fudan': (12, 15, 95),
    'sjtu': (12, 14, 95), 'zju': (14, 14, 95), 'ustc': (8, 8, 93),
    'nju': (12, 12, 94), 'whu': (14, 10, 92), 'hust': (14, 10, 92),
    'xjtu': (14, 8, 91), 'hit': (14, 10, 92), 'scut': (16, 8, 90),
    'bit': (14, 8, 91), 'buaa': (14, 8, 92), 'tjlu': (16, 6, 88),
    'dlut': (16, 6, 88), 'neu': (16, 6, 87), 'cqu_cn': (16, 5, 86),
    'nudt': (8, 2, 95), 'ecnu': (14, 10, 90), 'sysu': (14, 12, 92),
    # DE
    'tum': (20, 40, 80), 'lmu': (18, 20, 75), 'heidelberg': (12, 20, 82),
    'rwth': (18, 28, 78), 'hu-berlin': (16, 22, 75), 'fu-berlin': (16, 25, 75),
    'kit': (18, 22, 78), 'fau': (18, 18, 72), 'tu-berlin': (18, 30, 70),
    'goettingen': (14, 18, 78),
    # JP
    'utokyo': (8, 15, 95), 'kyoto': (8, 12, 93), 'osaka': (10, 12, 92),
    'tohoku': (10, 12, 90), 'tokyo-tech': (8, 18, 92), 'nagoya': (10, 10, 90),
    'hokkaido': (12, 10, 88), 'kyushu': (12, 10, 88), 'waseda': (18, 18, 85),
    'keio': (14, 14, 87),
    # KR
    'snu': (10, 12, 90), 'kaist': (8, 12, 92), 'yonsei': (12, 14, 88),
    'korea': (12, 12, 86), 'postech': (6, 10, 92), 'skku': (14, 16, 84),
    'hanyang': (14, 14, 82), 'sogang': (12, 12, 84),
    # NL
    'uva_nl': (16, 22, 82), 'utwente': (14, 30, 78), 'tud': (14, 28, 78),
    'leiden': (14, 20, 80), 'rug': (16, 28, 78), 'uu': (16, 18, 80),
    'eindhoven': (14, 25, 78),
    # NZ
    'auckland': (16, 32, 82), 'otago': (16, 22, 80), 'canterbury': (16, 20, 78),
    'victoria': (18, 22, 78), 'waikato': (18, 20, 75), 'massey': (20, 18, 72),
    # IE
    'tcd': (14, 30, 88), 'ucd_ie': (16, 28, 85), 'ucdie': (16, 28, 85),
    'nuig': (16, 20, 82), 'ucc': (16, 18, 82), 'dcu': (16, 22, 80),
    # CH
    'eth': (12, 42, 88), 'epfl': (12, 60, 85), 'uzh': (14, 25, 80),
    'unibe': (14, 18, 78),
    # FR
    'psl': (8, 35, 85), 'sorbonne': (16, 22, 78), 'paris-saclay': (14, 28, 80),
    # IT
    'polimi': (18, 25, 75), 'bologna': (22, 18, 72), 'sapienza': (22, 15, 68),
    # SE
    'kth': (14, 30, 80), 'lund': (14, 28, 82), 'uu_se': (14, 22, 80),
    # DK
    'copenhagen': (14, 22, 82), 'dtu': (14, 25, 80),
    # FI
    'aalto': (14, 22, 80), 'helsinki': (14, 18, 82),
    # MY
    'um': (16, 20, 80), 'utm': (18, 18, 78),
    # IN
    'iisc': (8, 5, 90), 'iitb': (10, 5, 88), 'iitd': (10, 5, 87),
    # Others
    'uba': (14, 8, 45),  # AR
    'kuleuven': (16, 22, 82),  # BE
    'usp': (14, 5, 65),  # BR
    'msu_ru': (12, 18, 80),  # RU
    'ntu_tw': (16, 12, 85),  # TW
}

# Country defaults for schools not in KNOWN
COUNTRY_DEFAULTS = {
    'US': (15, 15, 80), 'UK': (16, 35, 80), 'AU': (20, 30, 75),
    'CA': (20, 18, 75), 'SG': (14, 30, 88), 'HK': (14, 35, 85),
    'CN': (14, 10, 90), 'DE': (18, 22, 75), 'JP': (12, 12, 88),
    'KR': (12, 12, 84), 'NL': (16, 25, 80), 'NZ': (18, 22, 78),
    'IE': (16, 22, 82), 'CH': (14, 25, 80), 'FR': (16, 25, 78),
    'IT': (20, 18, 72), 'SE': (14, 25, 80), 'DK': (14, 22, 80),
    'FI': (14, 20, 80), 'MY': (18, 20, 78), 'IN': (10, 5, 85),
    'BE': (16, 22, 82), 'BR': (14, 5, 65), 'AR': (14, 8, 45),
    'RU': (12, 18, 80), 'TW': (16, 12, 85),
}

updated = 0
for fp in sorted(glob.glob('*-schools.json')):
    with open(fp) as f:
        schools = json.load(f)
    for s in schools:
        sid = s['id']
        country = s['country']
        ratio, intl, grad = KNOWN.get(sid, COUNTRY_DEFAULTS.get(country, (16, 20, 78)))
        s['studentFacultyRatio'] = ratio
        s['internationalRate'] = intl
        s['graduationRateNum'] = grad
        updated += 1
    with open(fp, 'w') as f:
        json.dump(schools, f, ensure_ascii=False, indent=2)

print(f"Updated {updated} schools")
