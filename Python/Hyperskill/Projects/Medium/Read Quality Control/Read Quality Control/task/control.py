import gzip
best_file = {}
for _ in range(3):
    file_name = input()
    with gzip.open(file_name, "rt") as f:
        text = f.read().split('\n')
    seq = [str(text[i]) for i in range(1, len(text), 4)]
    gc_average = [(round(((seq[i].count('G') + seq[i].count('C')) / len(seq[i])) * 100, 2)) for i in range(len(seq))]
    best_file[file_name] = round(sum(gc_average) / len(gc_average), 2)
file_name = list(best_file.keys())[0]
max_ = best_file[file_name]
for key in best_file:
    if best_file[key] > max_:
        file_name = key
with gzip.open(file_name, "rt") as f:
    text = f.read().split('\n')
seq = [str(text[i]) for i in range(1, len(text), 4)]
counts = [len(seq[i]) for i in range(len(seq))]
gc_average = [(round(((seq[i].count('G') + seq[i].count('C')) / len(seq[i])) * 100, 2)) for i in range(len(seq))]
n_list = [(seq[i].count('N') / len(seq[i]) * 100) for i in range(len(seq))]
print(f'Reads in the file = {len(seq)}:')
print(f'Reads sequence average length = {round(sum(counts) / len(seq))}')
print(f'\nRepeats = {len(seq) - len(list(set(seq)))}\nReads with Ns = {len(n_list) - n_list.count(0)}')
print(f'\nGC content average = {round(sum(gc_average) / len(gc_average), 2)}%')
print(f'Ns per read sequence = {round(sum(n_list) / len(n_list), 2)}%')
