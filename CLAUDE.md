# 9-maktab × Codial sayti

Farg'ona shahridagi 9-maktabda o'tadigan Codial tadbiri uchun sayt. O'quvchilar pechat qilingan QR kodni skanerlaydi va shu saytga tushadi. Bu sayt 6-maktab saytining (`D:\wibecoding\maktab6`) nusxasi — tuzilishi, uslubi va Codial haqidagi faktlar bir xil. Farqi: tadbirga xos bo'limlar (iste'dodlilar/o'rinlar, bonus, galereya) `index.html` ichida **izohda** (`<!-- -->`) turibdi va tadbirda rasm/ma'lumot kelganda ochiladi.

## Eng muhim qoida: manzil o'zgarmasligi kerak

- Jonli sayt: https://ilhomjon1502.github.io/maktab9-fargona/
- Repo: https://github.com/Ilhomjon1502/maktab9-fargona (public)
- QR kod (`qr/`) shu manzilga olib boradi va pechat qilinadi. Shuning uchun repo nomini o'zgartirma, o'chirma, private qilma; GitHub Pages (`main` branch, `/` root) sozlamasini o'zgartirma; `index.html` ildizda qolsin; build tizimi qo'shma.

## Yangilash (deploy)

GitHub Pages `main` branch'dan avtomatik chiqaradi.

1. `index.html` ni tahrirla.
2. `git add -A` → `git commit` (o'zbekcha xabar) → `git push`. Push qilishga foydalanuvchi oldindan ruxsat bergan.
3. 30–90 soniyada jonli saytda chiqadi. Tekshirish: `curl -s https://ilhomjon1502.github.io/maktab9-fargona/ | grep "<matn>"`

## Tadbirda tez ishlash (shu tartibda)

Foydalanuvchi rasm va o'rinlarni beradi. Imkon qadar kam so'rov va tez deploy:

1. **Rasmlar:** `python -I scripts/rasm.py <manba> img/tadbir/<nom>.webp [x0,y0,x1,y1]` — 1200px WebP, metadata'siz. Avval rasmlarni ko'rib chiq (Read), keraksiz/takroriy/xira rasmlarni tanlab ol.
2. **O'rinlar/iste'dodlilar:** `[TADBIR] Eng iste'dodlilar / o'rinlar` izohini och, sarlavha va matnni berilgan ma'lumotga moslab o'zgartir (1-, 2-, 3-o'rin va h.k.), rasmlarni qo'y.
3. **Galereya:** `[TADBIR] Tadbirdan lavhalar` izohini och, rasmlarni qo'y.
4. **Bonus:** `[TADBIR] Bonus sertifikat` — faqat 9-maktabda ham bonus berilgan bo'lsa och. Shartlari (nechta kun, qaysi kurs) foydalanuvchidan so'ra; 6-maktabdagi shart (7 kun, Kompyuter savodxonligi) bu yerga avtomatik o'tmaydi.
5. Telefon o'lchamida (375px) tekshir, push qil.

Izohni ochganda `<!--` va `-->` qatorlarini o'chir. Izoh ichida `--` ishlatma (HTML buzilishi mumkin).

## Darsga yozilish

"Darsga yozilish" tugmalari (hero va pastdagi CTA, ikkalasi `class="btn"`) Codial'ning rasmiy saytidagi ariza oynasiga olib boradi: https://codialinfo.uz/#ariza (maydonlar: ism, telefon, qiziqqan kurs, rozilik). Ikkala tugmani birga o'zgartir.

6-maktabning Google Formasi 9-maktabga **ulanmagan** (javoblar aralashib ketmasin). Agar 9-maktab uchun alohida forma kerak bo'lsa, tugmalar hrefini almashtir.

## Fayllar

- `index.html` — butun sayt, CSS ichida. Tashqi kutubxona/framework/JS yo'q — shunday qolsin.
- `img/codial-white.png` (hero, to'q fon), `img/codial.png` (footer, oq fon).
- `img/tadbir/` — tadbir rasmlari (hozircha bo'sh, `scripts/rasm.py` yaratadi).
- `qr/qr-maktab9.png` (2000px), `qr/qr-maktab9.svg` — pechat uchun QR kod.
- `.claude/launch.json` — lokal server (`site`, `python -m http.server 8000`). Rasmlarni `file://` orqali emas, server orqali ko'r.

## Uslub

- Til: o'zbek, lotin. Bolalarga **"sen"** deb murojaat qilinadi.
- Brend ranglari: ko'k `#00527E`, to'q sariq `#FF9F00` (CSS `:root`).
- Mobile-first, katta tugmalar, kam matn. Har doim 375px da tekshir.
- Yolg'on shoshiltirish yozma — faqat foydalanuvchi tasdiqlagan faktlar.
- Bolalar rasmlari bor: o'quvchilarning ism-familiyasini sayt matniga yozma. Sertifikatdagi ismlar rasmda o'qilsa, foydalanuvchiga ayt (xiralashtirish mumkin).

## Codial haqida faktlar (foydalanuvchi tasdiqlagan)

- Faqat **Farg'ona** filiali. 2021-yilda tashkil etilgan. **11 yoshdan** o'qitadi.
- Kurslar (narxlar **oylik**): Kompyuter savodxonligi 500 000 so'm (1 oy); Vibe coding, Backend, Flutter, SMM, Kiberxavfsizlik — har biri 750 000 so'm.
- Telegram https://t.me/codialuz · Instagram https://instagram.com/codialuz · YouTube https://youtube.com/@Codialuz
- Rasmiy veb-sayt yo'q — havola qo'yma.
