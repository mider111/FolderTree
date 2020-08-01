import os


def folder_tree(path):
    tree = os.walk(path)
    for p, dirs, files in tree:
        level = p.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(p)}/')
        sindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{sindent}{f}')
