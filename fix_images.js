const fs = require('fs');

function fixImages(filePath) {
    let html = fs.readFileSync(filePath, 'utf8');

    // Quick replace for any img containing 'women' or 'men' product images that lacks width
    let pattern = /<img[^>]*src="[^"]*images\/products\/(women|men)\/\d+\.jpg"[^>]*>/g;

    html = html.replace(pattern, (match) => {
        if (match.includes('width=')) return match;

        let newImg = match.replace('>', ' width="400" height="600" loading="lazy">');

        // Also ensure it has class="product-image" so we know the lazy class exists if needed.
        if (!newImg.includes('class=')) {
            newImg = newImg.replace('>', ' class="product-image">');
        } else if (!newImg.includes('product-image') && match.includes('class=')) {
            newImg = newImg.replace(/class="/, 'class="product-image ');
        }

        return newImg;
    });

    fs.writeFileSync(filePath, html);
    console.log('Fixed images in ' + filePath);
}

fixImages('pages/women.html');
fixImages('pages/men.html');
