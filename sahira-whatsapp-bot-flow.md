# WhatsApp Bot Flow SAHIRA PHONECELL

Versi: 2026-04-25

Tujuan bot: membalas cepat, membaca kebutuhan calon pembeli, mengurangi ragu awal, lalu menyerahkan chat ke admin dengan konteks yang sudah jelas. Bot tidak dipakai untuk hard selling atau janji stok/harga yang belum dicek admin.

## Prinsip Utama

1. Jawab cepat, singkat, dan ramah.
2. Kumpulkan informasi minimum yang membantu admin lanjut.
3. Jangan kirim katalog panjang otomatis.
4. Jangan menjanjikan paylater, COD, garansi, atau stok sebelum dicek admin.
5. Arahkan buyer ke next step kecil: cek stok, kirim opsi, cek unit, COD, trade-in, atau konsultasi budget.

## Data yang Perlu Dicatat

Setiap lead minimal punya:

- nama jika tersedia
- nomor WhatsApp
- sumber lead jika tersedia: Meta Ads, IG, FB, organik, referral, lainnya
- kebutuhan utama
- seri yang dicari
- budget
- preferensi baru/second
- area/lokasi jika tanya COD
- HP lama jika tanya tukar tambah
- status follow-up
- hasil akhir: kirim opsi, visit, COD, booking, deal, lost

## Menu Utama

Pesan pertama:

```text
Halo kak, selamat datang di SAHIRA PHONECELL.
Mau dibantu untuk kebutuhan apa?
```

Pilihan:

1. Cek stok & harga iPhone
2. Konsultasi upgrade / tukar tambah
3. Cari iPhone sesuai budget
4. Tanya COD / datang ke store
5. Tanya paylater
6. Bicara dengan admin

Tag awal:

```text
new_lead
```

## Flow 1 - Cek Stok & Harga iPhone

Trigger:

- user pilih menu 1
- user tanya "ready?"
- user tanya "harga iPhone berapa?"
- user menyebut seri iPhone tertentu

Bot:

```text
Siap kak. Mau cari seri iPhone apa?
Kalau belum pasti, boleh info budget amannya di kisaran berapa.
```

Data yang diminta:

- seri iPhone
- budget
- preferensi baru atau second

Jika user sudah menyebut seri:

```text
Baik kak. Untuk cek yang paling pas, kakak lebih cari baru atau second?
Budget amannya di kisaran berapa?
```

Balasan sebelum handoff:

```text
Siap kak, saya teruskan ke admin untuk cek unit yang ready, harga, dan detail kondisinya.
Nanti admin bantu kirim opsi yang paling cocok ya.
```

Tag lead:

```text
stock_inquiry
```

Ringkasan untuk admin:

```text
Lead cek stok.
Seri: {seri}
Budget: {budget}
Preferensi: {baru_second}
Sumber: {source}
```

## Flow 2 - Konsultasi Upgrade / Tukar Tambah

Trigger:

- user pilih menu 2
- user bilang "mau upgrade"
- user tanya "bisa tukar tambah?"
- user punya HP lama

Bot:

```text
Bisa kak. Biar admin bantu arahkan, HP lama kakak tipe apa dan kondisinya bagaimana?
Kalau sudah ada target iPhone, boleh sebutkan juga.
```

Data yang diminta:

- tipe HP lama
- kondisi umum
- target iPhone
- budget tambah jika ada

Pertanyaan lanjutan jika data belum lengkap:

```text
Siap kak. Kira-kira budget tambah yang aman berapa?
Nanti admin bantu cek opsi upgrade yang paling masuk akal.
```

Balasan sebelum handoff:

```text
Baik kak, saya teruskan ke admin untuk cek kemungkinan trade-in dan opsi upgrade.
Kalau nanti cocok, bisa sekalian dibantu arahkan proses pindah data.
```

Tag lead:

```text
upgrade_tradein
```

Ringkasan untuk admin:

```text
Lead upgrade/trade-in.
HP lama: {hp_lama}
Kondisi: {kondisi}
Target iPhone: {target_iphone}
Budget tambah: {budget_tambah}
Sumber: {source}
```

## Flow 3 - Cari iPhone Sesuai Budget

Trigger:

- user pilih menu 3
- user bilang "budget saya..."
- user belum tahu seri
- user minta rekomendasi

Bot:

```text
Siap kak, saya bantu arahkan.
Budget aman kakak berapa dan iPhone-nya lebih banyak dipakai untuk apa?
```

Pilihan kebutuhan:

- pemakaian harian
- kamera / konten
- kerja
- game
- hadiah
- belum tahu

Data yang diminta:

- budget
- kebutuhan
- preferensi ukuran atau seri jika ada

Balasan sebelum handoff:

```text
Baik kak. Admin akan bantu sempitkan 2-3 opsi yang paling realistis sesuai budget dan kebutuhan.
Jadi kakak tidak perlu bingung compare terlalu banyak.
```

Tag lead:

```text
budget_recommendation
```

Ringkasan untuk admin:

```text
Lead rekomendasi budget.
Budget: {budget}
Kebutuhan: {kebutuhan}
Preferensi: {preferensi}
Sumber: {source}
```

## Flow 4 - Tanya COD / Datang ke Store

Trigger:

- user pilih menu 4
- user tanya "bisa COD?"
- user tanya alamat toko
- user ingin cek unit langsung

Bot:

```text
Bisa kak, nanti disesuaikan area dan unit yang dipilih.
Kakak lebih nyaman datang cek unit ke store atau tanya COD ke lokasi kakak?
```

Jika pilih store:

```text
Siap kak. Admin akan bantu info jam, arahan lokasi, dan unit yang bisa dicek.
Kakak mau cari seri apa dulu?
```

Jika pilih COD:

```text
Boleh kak. Mohon info area/lokasi kakak dulu agar admin cek apakah bisa dijangkau.
Kakak mau cari seri apa?
```

Data yang diminta:

- preferensi: store atau COD
- area/lokasi
- seri iPhone jika ada

Balasan sebelum handoff:

```text
Siap kak, saya teruskan ke admin untuk cek jalur yang paling memungkinkan dan detail prosesnya.
```

Tag lead:

```text
cod_store_visit
```

Ringkasan untuk admin:

```text
Lead COD/store.
Preferensi: {store_cod}
Area: {area}
Seri: {seri}
Sumber: {source}
```

## Flow 5 - Tanya Paylater

Trigger:

- user pilih menu 5
- user tanya cicilan
- user tanya DP
- user tanya paylater

Bot:

```text
Bisa ditanyakan dulu kak.
Biar admin bantu arahkan, kakak ingin seri apa dan budget awal yang tersedia berapa?
```

Data yang diminta:

- seri yang diminati
- budget awal
- kebutuhan utama

Catatan bahasa:

- gunakan "dibantu cek"
- gunakan "opsi yang tersedia"
- gunakan "sesuai ketentuan"
- jangan tulis "pasti bisa"

Balasan sebelum handoff:

```text
Siap kak. Admin akan bantu jelaskan opsi yang tersedia dan pilihan unit yang paling realistis sesuai ketentuan.
```

Tag lead:

```text
paylater_inquiry
```

Ringkasan untuk admin:

```text
Lead paylater.
Seri: {seri}
Budget awal: {budget_awal}
Kebutuhan: {kebutuhan}
Sumber: {source}
```

## Flow 6 - Bicara dengan Admin

Trigger:

- user pilih menu 6
- user mengetik "admin"
- user marah / komplain
- user butuh bantuan yang tidak cocok dijawab bot

Bot:

```text
Siap kak, saya teruskan ke admin ya.
Boleh tulis singkat kebutuhannya supaya admin bisa langsung bantu dari konteks yang tepat.
```

Tag lead:

```text
human_request
```

Ringkasan untuk admin:

```text
User minta bicara dengan admin.
Kebutuhan: {last_message}
Sumber: {source}
```

## Fallback Intent

Jika bot tidak paham:

```text
Maaf kak, biar saya bantu lebih tepat.
Kakak mau cek stok, upgrade/tukar tambah, cari sesuai budget, COD/store, paylater, atau bicara dengan admin?
```

Jika user hanya tulis "harga":

```text
Boleh kak. Untuk harga tergantung seri, kondisi, dan stok unit.
Kakak cari seri apa atau budgetnya kisaran berapa?
```

Jika user tanya "aman gak":

```text
Wajar kak kalau mau pastikan dulu.
Di SAHIRA bisa tanya detail unit, minta info kondisi, dan pilih jalur cek unit yang paling nyaman.
Kakak mau cari seri apa dulu?
```

Jika user tanya "ready?":

```text
Siap kak, saya bantu cek arahnya dulu.
Kakak cari seri apa dan preferensinya baru atau second?
```

Jika user tanya "alamat mana?":

```text
Siap kak, nanti admin bantu info lokasi dan arahan cek unit.
Kakak sekalian mau cek seri apa?
```

## Follow-Up Otomatis

Follow-up hanya aktif jika user sudah memberi minat awal, bukan untuk semua orang.

### Setelah 4 jam tanpa balasan

```text
Kak, saya follow up ya.
Kalau masih mau cari iPhone yang cocok, admin bisa bantu sempitkan opsi sesuai budget kakak.
```

### Setelah 1 hari

```text
Kak, kalau masih ragu pilih seri, boleh kirim budget dan kebutuhan.
Nanti dibantu pilihkan 2-3 opsi yang paling masuk akal.
```

### Setelah 3 hari

```text
Halo kak, stok iPhone bisa berubah harian.
Kalau masih mau cek opsi yang ready, tinggal balas chat ini ya.
```

### Setelah 7 hari

```text
Baik kak, saya tutup follow up dulu.
Kalau nanti butuh info iPhone, trade-in, COD, atau paylater, silakan chat lagi ya.
```

## Aturan Admin Saat Ambil Alih

Admin wajib lanjut dengan:

1. Jawab kebutuhan utama user.
2. Kirim 1-3 opsi, jangan katalog panjang.
3. Beri proof yang relevan: foto/video unit, kondisi, garansi, COD/store.
4. Tanyakan next step kecil: cek detail, datang, COD, booking, atau estimasi trade-in.
5. Catat hasil akhir chat.

Contoh transisi admin:

```text
Halo kak, saya bantu lanjut ya.
Saya cek dari chat tadi kakak cari {kebutuhan}. Saya bantu kirim opsi yang paling cocok dulu.
```

## Keyword Routing

| Keyword user | Flow |
|---|---|
| harga, price, berapa, ready, stok | stock_inquiry |
| upgrade, tukar tambah, trade in, hp lama | upgrade_tradein |
| budget, dana, rekomendasi, cocoknya | budget_recommendation |
| COD, kirim, lokasi, alamat, toko, store | cod_store_visit |
| cicilan, paylater, DP, tenor | paylater_inquiry |
| admin, CS, komplain, bantuan | human_request |
| aman, takut zonk, garansi, ori | trust_objection |

## Metrics yang Harus Dicatat

- jumlah chat masuk per source iklan
- intent utama
- budget
- seri yang dicari
- response time pertama
- lead berhasil diklasifikasi atau tidak
- lanjut kirim opsi atau tidak
- lanjut visit/COD/booking atau tidak
- deal atau lost
- alasan lost

## Test Script

Gunakan percakapan ini untuk mengecek bot.

### Test 1 - Harga

User:

```text
Harga iPhone 13 berapa?
```

Expected:

```text
stock_inquiry
```

Bot harus tanya preferensi baru/second dan budget, lalu handoff.

### Test 2 - Tukar Tambah

User:

```text
Mau tukar tambah dari XR ke 13 bisa?
```

Expected:

```text
upgrade_tradein
```

Bot harus tanya kondisi HP lama, target, dan budget tambah.

### Test 3 - Budget

User:

```text
Budget 5 jutaan cocok ambil apa?
```

Expected:

```text
budget_recommendation
```

Bot harus tanya kebutuhan pemakaian lalu handoff ke admin.

### Test 4 - COD

User:

```text
Bisa COD ke rumah?
```

Expected:

```text
cod_store_visit
```

Bot harus tanya area/lokasi dan seri yang dicari.

### Test 5 - Trust

User:

```text
Takut zonk, aman gak?
```

Expected:

```text
trust_objection
```

Bot harus menenangkan, jelaskan bisa tanya detail/cek unit, lalu tanya seri.
