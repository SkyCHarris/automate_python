# Enter a regexp that matches all the items in the first column.
# You need to match the whole line, meaning a full match.

# assumes word senses. Within
# does the clustering. In the
# but when? It was hard to tell
# he arrive." After she had
# mess! He did not let it
# it wasn't hers!' She replied
# always thought so.) Then

import re

sentenceRegex = re.compile(r'^\w+\s*\W*\s*\w+$')
sentenceRegex.search('assumes word senses. Within, does the clustering. In the, but when? It was hard to tell, he arrive." After she had')
