import os
import re

directories = [
    r'c:\Users\sneha\Documents\GitHub\Hm_fast',
    r'c:\Users\sneha\Documents\GitHub\hm_slow'
]

exact_mismatches = [
    # Men
    r'Regular Fit Sports vest top',
    r'Regular Fit Sweatpants',
    r'Oversized Cotton Shirt',
    
    # Ladies
    r'Floral Chiffon Dress',
    r'Ribbed Tank Top',
    r'Cropped Denim Jacket',
    r'Tailored Blazer',
    r'Cotton Poplin Skirt',
    r'Wide Leg Jeans',
    r'Tailored Shorts',
    r'Fitted Blazer',
    r'Cotton Sweatshirt',
    r'Wide Leg Linen Trouser',
    r'Wide-Leg Linen Trouser',
    r'Knit Cropped Top',
    r'Pointelle jersey top',
    r'Quilted Jacket',
    r'Pleated Trouser',
    r'Cotton Blouse',
    
    # Kids
    r'Loose fit denim shirt',
    r'Denim Dress',
    r'Shirt Dress',
    r'Printed cotton legging',
    r'Cotton polo shirt',
    r'Matching outfit set',
    r'2-piece T-shirt and sweatshorts set'
]

for d in directories:
    for root, _, files in os.walk(d):
        if '.git' in root or 'node_modules' in root: continue
        for file in files:
            if file.endswith('.html') or file.endswith('.js') or file.endswith('.json'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        text = f.read()
                    for m in exact_mismatches:
                        if re.search(m, text, re.IGNORECASE):
                            print(f"Found '{m}' in {filepath}")
                except Exception as e:
                    pass
