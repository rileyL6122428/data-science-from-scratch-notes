import sys, re

pattern = sys.argv[1]

for line in sys.stdin:
    if re.search(pattern, line):
        sys.stdout.write(line)
