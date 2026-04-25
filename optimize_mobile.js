const fs = require('fs');

const filePath = 'd:/Landing Page/LP_SAHIRA_CELL/index.html';
let content = fs.readFileSync(filePath, 'utf-8');

// Container padding improvements for mobile
content = content.replace(
    '<section id="kenapa" class="max-w-4xl mx-auto px-8 py-12">',
    '<section id="kenapa" class="max-w-4xl mx-auto px-4 md:px-8 py-12">'
);

content = content.replace(
    '<div class="max-w-4xl mx-auto px-8">',
    '<div class="max-w-4xl mx-auto px-4 md:px-8">'
);

content = content.replace(
    '<section id="katalog" class="max-w-7xl mx-auto px-8 py-12">',
    '<section id="katalog" class="max-w-7xl mx-auto px-4 md:px-8 py-12">'
);

content = content.replace(
    '<section id="lokasi" class="max-w-7xl mx-auto px-8 py-24 mb-16">',
    '<section id="lokasi" class="max-w-7xl mx-auto px-4 md:px-8 py-24 mb-16">'
);

// Fix Exclusive Benefits section negative margins for mobile
// Before: p-8 -m-8
// After: p-4 -m-4 md:p-8 md:-m-8
content = content.replaceAll(
    'class="group flex items-start gap-8 p-8 -m-8 rounded-[2rem] transition-all hover:bg-white hover:shadow-2xl hover:shadow-primary/5 active:scale-[0.97] cursor-pointer">',
    'class="group flex items-start gap-4 md:gap-8 p-4 -m-4 md:p-8 md:-m-8 rounded-[2rem] transition-all hover:bg-white hover:shadow-2xl hover:shadow-primary/5 active:scale-[0.97] cursor-pointer">'
);

fs.writeFileSync(filePath, content, 'utf-8');
console.log('Mobile layout optimized');
