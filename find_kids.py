import json
import re

with open(r'c:\Users\sneha\Documents\GitHub\Hm_fast\pages\kids.html', 'r', encoding='utf-8') as f:
    text = f.read()

names = re.findall(r'data-name="([^"]+)"', text)
uniq_names = sorted(list(set(names)))
for name in uniq_names:
    print(name)

with open(r'c:\Users\sneha\Documents\GitHub\Hm_fast\js\products-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

names = re.findall(r'"name":\s*"([^"]+)"', text)
print("\n--- KIDS ---\n")
match = re.search(r'"kids":\s*\[(.*?)\]\s*(?:,\s*"home"|}|\Z)', text, re.DOTALL)
if match:
    kids_text = match.group(1)
    kids_names = re.findall(r'"name":\s*"([^"]+)"', kids_text)
    for n in sorted(list(set(kids_names))):
        print(n)
