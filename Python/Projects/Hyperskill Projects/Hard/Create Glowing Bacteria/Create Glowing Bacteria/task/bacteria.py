match = {'T': 'A', 'A': 'T', 'C': 'G', 'G': 'C'}
with open(input()) as f:
    txt = f.read().strip().split('\n')
dna, sep, gfp, l, r = txt[0], txt[1], txt[2], txt[3].split()[0], txt[3].split()[1]
dna = dna[:dna.find(sep) + 1] + gfp[gfp.find(l) + 1: gfp.find(r) + 1] + dna[dna.find(sep) + 1:]
c_dna = ''.join(match[char] for char in dna)
print(dna, c_dna, sep='\n')
