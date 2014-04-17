import os
import stat

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testpath')
file = os.path.join(path, 'hello.sh')

if not os.path.exists(path):
        os.makedirs(path)

with open(file, 'w') as f:
    f.write('#!/bin/bash\n')
    f.write('echo $1')

mode = os.stat(file).st_mode

# set executable flag on file
os.chmod(file, mode | stat.S_IXUSR)

os.system(file + ' "Hello World!"')