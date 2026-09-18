import os
import hashlib
from pathlib import Path
from datetime import datetime
import pandas as pd
from PIL import Image
import pypandoc

BASE_DIR = Path(__file__).resolve().parent
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp'}

TITLES_MAP = {
    "01-user-management": "مدیریت کاربری",
    "auth-registration": "ثبت‌نام و لاگین",
    "account-blocking": "مسدودی حساب",
    "flagging-system": "سیستم فلگ و گزارش",
    "identity-verification": "احراز هویت (KYC)",
    "access-roles-permissions": "سطوح دسترسی و نقش‌ها",
    "profile-management": "مدیریت پروفایل",
    "address-book": "دفترچه آدرس",
    "representory": "نمایندگی‌",
    "02-product-catalog": "کاتالوگ کالا، تجهیز و پلنت",
    "specifications": "مشخصات فنی",
    "official-documents": "اسناد رسمی",
    "units-of-measure": "واحدهای سنجش",
    "part-numbers": "پارت نامبر",
    "creation-lifecycle": "چرخه حیات ایجاد",
    "external-integration": "اتصال به خارج ",
    "media-assets": "تصاویر و رسانه",
    "03-project-catalog": "کاتالوگ پروژه‌",
    "fields": "فیلدهای تخصصی",
    "04-ads": "آگهی‌ها",
    "lifecycle": "چرخه عمر آگهی",
    "pricing-schemes": "مدل‌های قیمت‌گذاری",
    "insurance-warranty": "بیمه و گارانتی",
    "verification-documents": "مدارک مالکیتی و فنی",
    "review-approval": "بررسی و انتشار",
    "lock-and-reserve": "قفل و بیعانه",
    "expert-inspection": "کارشناسی تجهیزات دست‌دوم",
    "delivery-terms": "شرایط تحویل",
    "project-listings": "آگهی‌های پروژه‌ای",
    "sell-buy-requests": "آگهی فروش و استعلام خرید",
    "rent-requests": "آگهی و درخواست اجاره",
    "partnership": "آگهی مشارکت",
    "05-negotiation-room": "اتاق مذاکره و پیش‌نویس قرارداد",
    "negotiation-rooms": "اتاق‌های گفتگو",
    "data-masking": "فیلتر اطلاعات تماسی (Anti-Bypass)",
    "admin-oversight": "نظارت ادمین بر مذاکرات",
    "archive-history": "بایگانی گفتگوها",
    "06-contract-common": "مشترکات قراردادها",
    "final-approval": "تایید نهایی و امضا",
    "audit-change-log": "لاگ تغییرات مفاد",
    "invoicing": "صدور فاکتور و پیش‌فاکتور",
    "amendments": "متمم و الحاقیه‌ها",
    "07-sales-contract": "قرارداد فروش",
    "snapshot-state": "اسنپ‌شات وضعیت سفارش",
    "payments-escrow": "پرداخت‌ها و حساب امانی (Escrow)",
    "shipping-logistics": "لجستیک و حمل‌ونقل",
    "inspection-handover": "بازرسی فنی و تحویل قطعی",
    "return-process": "فرآیند مرجوعی کالا",
    "delay-penalty-damages": "خسارت تاخیر و جریمه",
    "08-rental-contract": "قرارداد اجاره",
    "timeline-schedule": "زمان‌بندی دوره اجاره",
    "pricing-deposit": "اجاره‌بها و ودیعه ضمانت",
    "handover-return-terms": "تحویل و عودت دستگاه",
    "maintenance-repair": "نگهداری و تعمیرات",
    "insurance": "پوشش‌های بیمه‌ای",
    "09-partnership-contract": "قرارداد مشارکت",
    "capital-contributions": "آورده نقدی و غیرنقدی",
    "profit-loss-sharing": "تسهیم سود و زیان",
    "governance-signoff": "حق امضا و تصمیم‌گیری",
    "exit-strategy": "خروج شرکا و تصفیه",
    "10-project-contract": "قرارداد پروژه",
    "scope-commitments": "شرح خدمات و تعهدات",
    "project-timeline": "گانت چارت و فازبندی",
    "milestone-payments": "پرداخت‌های مرحله‌ای و تسویه",
    "contract-amendments": "دستور تغییر کار و الحاقیه",
    "11-academy": "آکادمی و دانش صنعتی",
    "courses-curriculum": "دوره‌ها و سرفصل‌ها",
    "field-experiences": "مستندسازی تجارب",
    "qna-discussions": "پرسش و پاسخ",
    "certifications": "گواهینامه‌ها",
    "instructor-payouts": "تسویه حساب مالکان محتوا",
    "12-experts": "متخصصین",
    "screening-assessment": "ارزیابی صلاحیت و رتبه‌بندی",
    "expert-profile": "شناسنامه حرفه‌ای متخصص",
    "specializations": "شاخه‌های تخصصی",
    "expertise-levels": "سطوح خبرگی (Grade)",
    "task-dispatch": "ارجاع و تخصیص کار",
    "compensation-fee": "دستمزد",
    "service-calendar": "تقویم کاری و رزرو زمان",
    "13-finance-and-wallet": "سیستم مالی و کیف پول",
    "double-entry-accounting": "دفترکل",
    "deposit-withdrawal": "واریز و برداشت",
    "payment-gateways": "درگاه‌های پرداخت",
    "wallet-freeze-escrow": "فریز وجوه و مسدودی بیعانه",
    "platform-fees": "تعیین کارمزد پلتفرم",
    "14-platform-commons": "زیرساخت و سرویس‌های عمومی",
    "file-city-storage": "شهر فایل و S3 Storage",
    "notifications-engine": "موتور اعلان (SMS/email/Push)",
    "numbering-schemes": "سیستم شماره‌گذاری اسناد",
    "audit-logs": "لاگ رویدادها و مانیتورینگ",
    "live-chat-engine": "موتور چت زنده",
    "disaster-backup": "پشتیبان‌گیری دوره‌ای",
    "security-compliance": "الزامات امنیتی و احراز",
    "infrastructure-server": "پیکربندی سرور و داکر",
    "search-filtering": "موتور جستجو و الستیک",
    "taxonomy-categories": "درخت دسته‌بندی‌ها",
    "print-document-generator": "PDF چاپ",
    "idempotency-guard": "گارد تکرار درخواست (Idempotency)",
    "dispute-arbitration": "داوری و حل اختلاف حقوقی"
}

def convert_docx_to_md(docx_path: Path):
    md_path = docx_path.with_suffix('.md')
    parent_key = docx_path.parent.name
    fa_title = TITLES_MAP.get(parent_key, parent_key)
    
    frontmatter = (
        f"---\n"
        f"title: \"{docx_path.stem}\"\n"
        f"section: \"{fa_title}\"\n"
        f"last_updated: \"{datetime.now().strftime('%Y-%m-%d %H:%M')}\"\n"
        f"---\n\n"
    )
    try:
        body = pypandoc.convert_file(str(docx_path), 'gfm', extra_args=['--wrap=none'])
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + body)
        print(f"[✓ Word] {docx_path.relative_to(BASE_DIR)} -> .md")
    except Exception as e:
        print(f"[✗ Error Word] {docx_path.name}: {e}")

def convert_xlsx_to_md(xlsx_path: Path):
    md_path = xlsx_path.with_suffix('.md')
    parent_key = xlsx_path.parent.name
    fa_title = TITLES_MAP.get(parent_key, parent_key)
    
    output = [
        f"---\n"
        f"title: \"{xlsx_path.stem}\"\n"
        f"section: \"{fa_title}\"\n"
        f"last_updated: \"{datetime.now().strftime('%Y-%m-%d %H:%M')}\"\n"
        f"---\n\n"
    ]
    try:
        excel_file = pd.ExcelFile(xlsx_path)
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(excel_file, sheet_name=sheet_name)
            df = df.dropna(how='all')
            if not df.empty:
                output.append(f"### شیت: {sheet_name}\n\n")
                output.append(df.to_markdown(index=False))
                output.append("\n\n")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.writelines(output)
        print(f"[✓ Excel] {xlsx_path.relative_to(BASE_DIR)} -> .md")
    except Exception as e:
        print(f"[✗ Error Excel] {xlsx_path.name}: {e}")

def convert_images_to_webp(img_path: Path):
    webp_path = img_path.with_suffix('.webp')
    if webp_path.exists():
        return
    try:
        with Image.open(img_path) as img:
            img.save(webp_path, 'WEBP', quality=85)
        print(f"[✓ Image] {img_path.relative_to(BASE_DIR)} -> .webp")
    except Exception as e:
        print(f"[✗ Error Image] {img_path.name}: {e}")

def generate_root_readme():
    readme_path = BASE_DIR / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# پلتفرم مگاوات - ساختار فنی و مستندات سیستم\n\n")
        f.write("این مخزن شامل نیازمندی‌های بیزنسی، مدل‌های داده، فرآیندهای مالی و قراردادهای پلتفرم است.\n\n")
        f.write("## سرفصل‌های معماری\n\n")
        
        for main_folder in sorted(os.listdir(BASE_DIR)):
            folder_path = BASE_DIR / main_folder
            if folder_path.is_dir() and not main_folder.startswith('.'):
                fa_main = TITLES_MAP.get(main_folder, main_folder)
                f.write(f"### {fa_main} (`{main_folder}`)\n")
                for sub in sorted(os.listdir(folder_path)):
                    sub_path = folder_path / sub
                    if sub_path.is_dir() and not sub.startswith('.'):
                        fa_sub = TITLES_MAP.get(sub, sub)
                        rel_link = f"./{main_folder}/{sub}"
                        f.write(f"- [{fa_sub}]({rel_link})\n")
                f.write("\n")
    print("[✓ Index] README.md اصلی به‌روزرسانی شد.")

def main():
    print(" شروع فرآیند بیلد و بهینه‌سازی اسناد مگاوات...")
    for root, _, files in os.walk(BASE_DIR):
        root_path = Path(root)
        if '.git' in root_path.parts:
            continue
        for f in files:
            if f.startswith("~$"):
                continue
            file_path = root_path / f
            ext = file_path.suffix.lower()
            if ext == '.docx':
                convert_docx_to_md(file_path)
            elif ext in ('.xlsx', '.xls'):
                convert_xlsx_to_md(file_path)
            elif ext in IMAGE_EXTENSIONS:
                convert_images_to_webp(file_path)

    generate_root_readme()
    print(" تمام عملیات با موفقیت پایان یافت.")

if __name__ == "__main__":
    main()
