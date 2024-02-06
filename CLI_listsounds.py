import sys
from sounds_list import *

if sys.argv[1] == '-ls' or sys.argv[1] == '--list_sounds':
     for sound in sounds_list:
           print(sound)
