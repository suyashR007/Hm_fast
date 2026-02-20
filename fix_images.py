import os
import re

for f in ['pages/women.html', 'pages/men.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    def replace_img(match):
        img_tag = match.group(0)
        if 'width="400"' in img_tag:
            return img_tag
        return img_tag.replace('>', ' width="400" height="600" loading="lazy">')
        
    new_content = re.sub(r'<img\s+src="(?:\.\.)?/images/products/(?:women|men|kids)/\d+\.jpg"[^>]*>', replace_img, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)

print('Images fixed in women.html and men.html.')
