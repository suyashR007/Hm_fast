import os
import re

directories = [
    r'c:\Users\sneha\Documents\GitHub\Hm_fast',
    r'c:\Users\sneha\Documents\GitHub\hm_slow'
]

replacements = {
    r'Matching outfit set': 'Printed Pyjama Set'
}

for d in directories:
    for root, _, files in os.walk(d):
        if '.git' in root or 'node_modules' in root: continue
        for file in files:
            if file.endswith('.html') or file.endswith('.js') or file.endswith('.json'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        text = f.read()
                    
                    original = text
                    for old, new in replacements.items():
                        text = re.sub(old, new, text, flags=re.IGNORECASE)
                        
                    if text != original:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(text)
                        print(f"Updated: {filepath}")
                except:
                    pass
