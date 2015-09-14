from os.path import getsize, getmtime
from time import localtime, asctime
import modutils

mods = modutils.find('time')

for mod in mods:
    tm = asctime(localtime(getmtime(mod)))
    kb = getsize(mod) / 1024
    print('%s: (%d kbytes, %s)' % (mod, kb, tm))
