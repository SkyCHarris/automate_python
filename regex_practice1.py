# Enter a regexp that matches all the items in the first column.
# You need to match the whole line, meaning a full match.


# pit
# spot
# spate
# spate
# slap two
# respite

import re


wordRegex = re.compile(r'\w+\s?\w+')
mo = wordRegex.findall('pit, spot, spate, spate, slap two, respite')
print(mo)