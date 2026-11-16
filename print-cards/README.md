# Nizar Al-Fan — NFC Smart Business Cards (print)

بطاقات NFC الفعلية للطباعة — ٣ أشخاص، وجهان لكل بطاقة، مع كود QR **متجهي (vector)** وشعار اللمس الذكي / NFC.

## الملف الجاهز للطباعة
- **`Nizar Al-Fan NFC Smart Business Cards.pdf`** — ٦ صفحات (وجه لكل صفحة)، PDF **متجهي**:
  - كود QR = vector (مُولّد بـ qrencode، مستوى تصحيح H) ومُتحقّق من مسحه لكل بطاقة.
  - النصوص = خطوط مضمّنة (TrueType) متجهية.
  - الوحيد غير المتجه: شعار الحرف N (PNG صغير `assets/mark.png`) — بدقة عالية كافية للطباعة.

## المصدر
- **`nfc-cards.html`** — القالب القابل للتعديل (كل النصوص/الألوان هنا)، فيه رموز `@@QR_*@@`.
- **`build.py`** — يحقن كود QR المتجهي داخل القالب وينتج `nfc-cards.build.html`.
- **`assets/qr-*.svg`** — أكواد QR المتجهية. **`assets/mark.png`** — شعار الحرف N.
- **`preview/all-cards.png`** — معاينة.

## المقاس
- القصّ النهائي: **٨٥٫٦ × ٥٤ مم** (CR80 — مقاس بطاقة NFC القياسي).
- مع هامش القصّ (bleed): **٩١٫٦ × ٦٠ مم**.

## إعادة التوليد بعد أي تعديل
```bash
cd print-cards
python3 build.py
google-chrome-stable --headless=new --disable-gpu --no-sandbox \
  --print-to-pdf="Nizar Al-Fan NFC Smart Business Cards.pdf" --no-pdf-header-footer \
  "file://$PWD/nfc-cards.build.html"
```

## الروابط داخل أكواد QR (مُتحقّق منها)
- المتجر → `https://nizar-alfan-cards.vercel.app/`
- محمود → `https://nizar-alfan-cards.vercel.app/mahmoud`
- موفق → `https://nizar-alfan-cards.vercel.app/moafaq`
