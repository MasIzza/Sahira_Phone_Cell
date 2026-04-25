import re

with open('d:/Landing Page/LP_SAHIRA_CELL/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Problem & Solusi Items
content = content.replace(
    '<a href=\"#lokasi\" class=\"block p-6 md:p-8 border-b md:border-r border-slate-200/80 relative group cursor-pointer hover:bg-white/60 transition-colors flex items-center gap-5\">',
    '<a href=\"https://wa.me/6285813994032?text=Takut%20zonk,%20aman%20gak?\" target=\"_blank\" class=\"block p-6 md:p-8 border-b md:border-r border-slate-200/80 relative group cursor-pointer hover:bg-white/60 transition-colors flex items-center gap-5\">'
)

content = content.replace(
    '<a href=\"#layanan\" class=\"block p-6 md:p-8 relative group cursor-pointer hover:bg-white/60 transition-colors flex items-center gap-5\">',
    '<a href=\"https://wa.me/6285813994032?text=Admin,%20saya%20ingin%20bantuan\" target=\"_blank\" class=\"block p-6 md:p-8 relative group cursor-pointer hover:bg-white/60 transition-colors flex items-center gap-5\">'
)

# Replace the text= portions in URL query
content = content.replace(
    'Halo%20Admin,%20saya%20ingin%20tanya%20tentang%20Paylater%20atau%20Kredit',
    'Tanya%20paylater'
)

content = content.replace(
    'Halo%20Admin,%20saya%20ingin%20tanya%20tentang%20COD%20Area',
    'Bisa%20COD%20ke%20rumah?'
)

content = content.replace(
    'Halo%20Admin,%20saya%20ingin%20tanya%20tentang%20Cek%20dan%20Bayar%20di%20Rumah',
    'Bisa%20COD%20ke%20rumah?'
)

content = content.replace(
    'Halo%20Admin,%20saya%20ingin%20melihat%20katalog%20lengkapnya',
    'Cek%20stok%20dan%20harga'
)

content = content.replace(
    'Halo%20Sahira%20Phonecell,%20saya%20tertarik%20membeli%20iPhone',
    'Minta%20rekomendasi%20iPhone%20sesuai%20budget'
)

content = content.replace(
    'Halo%20Sahira%20Phonecell,%20saya%20ingin%20bertanya',
    'Admin,%20mau%20tanya'
)

with open('d:/Landing Page/LP_SAHIRA_CELL/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
