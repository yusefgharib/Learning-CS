import hashlib
import os, sys
from collections import defaultdict


def get_paths_sizes(path, order, ext):
    sizes, paths = [], []
    for root, dirs, files in os.walk(path, topdown=order):
        for name in files:
            full_path = os.path.join(root, name)
            file_size = os.path.getsize(full_path)
            if name.endswith(ext):
                sizes.append(file_size)
                paths.append(full_path)
    return [sizes, paths]


def get_duplicates(sizes, paths):
    indexes = defaultdict(list)
    for i, size in enumerate(sizes):
        indexes[size].append(i)
    for key in indexes:
        for i in range(len(indexes[key])):
            indexes[key][i] = paths[indexes[key][i]]
    return indexes


def get_duplicate_hash(bytes_p):
    duplicate_hashes = defaultdict(lambda: defaultdict(list))
    for size, files in bytes_p.items():
        for file in files:
            with open(file, "rb") as f:
                duplicate_hashes[size][hashlib.md5(f.read()).hexdigest()].append(file)
    return duplicate_hashes


def print_duplicate_hashes(duplicate_hashes):
    c = 1
    for size, hashes in duplicate_hashes.items():
        print(f"\n{size} bytes")
        for hash_, files in hashes.items():
            if len(files) > 1:
                print(f"Hash: {hash_}")
                for path in files:
                    print(f"{c}. {path}")
                    c += 1
    return c


def delete(size_hash_paths, choice):
    idx = 1
    for size, hashes in size_hash_paths.items():
        for paths in hashes.values():
            if len(paths) > 1:
                for path in paths:
                    if idx == choice:
                        os.remove(path)
                        return size
                    idx += 1
    raise IndexError


try:
    root_folder = sys.argv[1]
    file_type = input('Enter file format:')
    print("Size sorting options:\n"
          "1. Descending\n"
          "2. Ascending")
    sort_option = input("Enter a sorting option:")
    while sort_option not in '12':
        sort_option = input("Wrong option")
    sort_option = True if sort_option == '1' else False
    size_l, path_l = get_paths_sizes(root_folder, sort_option, file_type)
    duplicates = get_duplicates(size_l, path_l)
    sorted_keys = sorted([i for i in duplicates if duplicates[i] != duplicates.default_factory()], reverse=sort_option)
    sizes_paths_dict = defaultdict(list)
    for size in sorted_keys:
        print(size, 'bytes')
        for j in range(len(duplicates[size])):
            sizes_paths_dict[size].append(duplicates[size][j])
            print(duplicates[size][j])
    check_dup = input("Check for duplicates?")
    while check_dup not in ["yes", "no"]:
        check_dup = input("Wrong option")
    if check_dup == 'yes':
        answer = get_duplicate_hash(sizes_paths_dict)
        num_files = print_duplicate_hashes(answer)
        del_option = input("Delete files?")
        while del_option not in ["yes", "no"]:
            del_option = input("Wrong option")
        if del_option == "yes":
            while True:
                try:
                    to_delete = input("\nEnter file numbers to delete:\n").split()

                    if not to_delete:
                        raise ValueError
                    to_delete = [int(x) for x in to_delete]
                except ValueError:
                    print("Wrong option\n")
                else:
                    if all(1 <= idx <= num_files for idx in to_delete):
                        break
            freed = sum(delete(answer, x) for x in to_delete)
            print("Total freed up space:", freed, "bytes")





except IndexError:
    print("Directory is not specified")
