# This script will be used to convert Airr quote formatting to Obsidian formatting
# Written by: anitrama

import re
from pathlib import Path

user_input = input('paste file path here: ')
input_fixed = user_input.strip('"')
filename = Path(input_fixed)

final_list = []
with open(filename, 'r+') as f:
    lines = f.readlines()
    non_blank_lines = []
    for line in lines:
        if line.rstrip():
            non_blank_lines.append(line)

    for line in non_blank_lines:
        new_string = re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+', line)
        quote_words = new_string[2:]
        # you can do the if statement inline
        quote = ' '.join(quote_words) if quote_words else "1"
        final_form = str('- [' + quote + "]" + new_string[1])
        final_list.append(final_form)
    
    # write the same file. Avoids the double IO
    for line in final_list:
        f.write('%s\n' % line)
