'''
Path:
- Subdirectory 1:
   - file11
   - file12
   - Sub-sub-directory 11:
         - file111
         - file112
- Subdirectory 2:
    - file21
    - sub-sub-directory 21
    - sub-sub-directory 22    
        - sub-sub-sub-directory 221
            - file 2211
'''
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#print('1 ' + os.getcwd())
path = os.getcwd() + '/test'
os.chdir(path)
#print('2 ' + os.getcwd())

def folder_tree(path):
    tree = os.walk(path)
    for p, dirs, files in tree:
        level = p.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(p)}/')
        sindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{sindent}{f}')

folder_tree(path)