import os
import re

directories = [
    r"c:\Users\sneha\Documents\GitHub\Hm_fast",
    r"c:\Users\sneha\Documents\GitHub\hm_slow"
]

replacements = {
    # Men
    r"Regular Fit Sports vest top with DryMove™": "Regular Fit Oxford Shirt",
    r"Regular Fit Sports vest top with DryMove\\u2122": "Regular Fit Oxford Shirt",
    r"Regular Fit Sweatpants": "Relaxed Fit Linen Shirt",
    r"Oversized Cotton Shirt": "Regular Fit Cotton Shorts",
    
    # Ladies
    r"Floral Chiffon Dress": "Wide-Leg Cotton Trousers",
    r"Ribbed Tank Top": "High-Waist Tailored Trousers",
    r"Cropped Denim Jacket": "Slim Fit Chinos",
    r"Tailored Blazer": "Crepe Wrap Dress",
    r"Cotton Poplin Skirt": "Straight-Leg Suit Trousers",
    r"Wide High Jeans": "Relaxed Fit Cargo Trousers",
    r"Motif-detail wide leg jeans": "Relaxed Fit Cargo Trousers",
    r"Tailored Shorts": "Jersey A-Line Dress",
    r"Fitted Blazer Dress": "Paperbag-Waist Trousers",
    r"Cotton Sweatshirt": "Slim Mom High Jeans",
    r"Wide-leg linen trousers": "Fine-Knit Cardigan",
    r"Pointelle jersey top": "Rib-Knit Vest Top", # My guess for knit cropped top based on products-data.js 
    r"Quilted Jacket": "Rhinestone Hair Clip",
    r"Pleated Trousers": "Pleated Satin Skirt",
    r"Cotton Blouse": "Oversized Bomber Jacket",
    
    # Kids
    r"Loose-fit denim shirt": "Printed Jersey Top",
    r"Loose Fit Denim Shirt": "Printed Jersey Top",
    r"Denim Dress": "Patterned Cotton Dress",
    r"Shirt Dress": "Animal Print Sweatshirt",
    r"Printed cotton leggings": "Tulle-Trimmed Skirt",
    r"Cotton Polo Shirt": "Padded Puffer Jacket",
    r"2-piece T-shirt and sweatshorts set": "Printed Pyjama Set" # My guess for matching outfit set
}

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return
        
    original_content = content
    
    for old, new in replacements.items():
        # Case insensitive regex replacement
        pattern = re.compile(old, re.IGNORECASE)
        content = pattern.sub(new, content)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

for d in directories:
    for root, _, files in os.walk(d):
        # Avoid node_modules or .git if they exist
        if '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith('.html') or file.endswith('.js') or file.endswith('.json'):
                process_file(os.path.join(root, file))
