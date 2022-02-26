import sys

if len(sys.argv) < 3:
    print('Use to find identical lines between two files and save to a third file.')
    print(f'Usage: {sys.argv[0]} <input1.txt> <input2.txt> <output.txt>')
    sys.exit(1)

input1 = sys.argv[1]
input2 = sys.argv[2]
output = sys.argv[3]

with open(input1) as f1:
    with open(input2) as f2:
        identical = set(f1).intersection(f2)

with open(output, 'w') as f3:
    for line in sorted(identical):
        if not line.isspace():
            f3.write(line)

print(f'{len(identical)} lines are identical')