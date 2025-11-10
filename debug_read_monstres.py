p = r"c:\Users\Alex\OneDrive\Desktop\Developpement Logiciel\Projets perso\JeuAventure\src\game\monstres.py"
print('File path:', p)
with open(p, 'r', encoding='utf-8') as f:
    s = f.read()
print('Length:', len(s))
print('--- START ---')
print(s[:400])
print('--- END ---')
