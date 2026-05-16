# 📰 מערכת אגרגציה חדשות ישראל

## 📖 תיאור

מערכת אוטומטית המאגדת חדשות מ-**50+ אתרי חדשות אמינים בישראל** ויוצרת דף HTML עדכני כל שעה.

## ✨ תכונות

- ✅ **עדכון אוטומטי כל שעה** דרך GitHub Actions
- ✅ **50+ מקורות חדשות** מאתרים אמינים
- ✅ **דף HTML סטטי** עם עיצוב מודרני
- ✅ **הסרת כפילויות** חכמה של חדשות
- ✅ **מיון לפי תאריך** (חדשות ראשונה קודם)
- ✅ **Responsive Design** - עבד בטלפון וטאבלט
- ✅ **RSS Feeds** מכל האתרים הגדולים

## 🚀 מקורות החדשות

### ערוצי בעברית
- 📺 **Ynet** - ynet.co.il
- 📺 **Mako** - mako.co.il
- 📺 **Walla** - walla.co.il
- 📺 **NRG** - nrg.co.il
- 📺 **Haaretz** - haaretz.co.il
- 📺 **Calcalist** - calcalist.co.il
- 📺 **Globes** - globes.co.il
- 📺 **10 TV** - 10tv.nana10.co.il
- 📺 **Kan (ערוץ הראשון)** - kan.org.il
- 📺 **Israel Hayom** - israelhayom.co.il
- 📺 **Kvodo** - kvodo.co.il

### ערוצים בינלאומיים
- 🌐 **Jerusalem Post** - jpost.com
- 🌐 **Times of Israel** - timesofisrael.com
- 🌐 **i24news** - i24news.tv
- 🌐 **Arutz Sheva** - inn.co.il
- 🌐 **Media Line** - themedialine.org

### מקורות רשמיים
- 🎖️ **צה"ל** - idf.il
- 🎖️ **Tazpit Press Agency** - tazpit.tv

## 🛠️ טכנולוגיה

- **Python 3.11** - שפת תכנות
- **BeautifulSoup4** - Web Scraping
- **Feedparser** - ניתוח RSS Feeds
- **GitHub Actions** - אוטומציה
- **HTML5 + CSS3** - ממשק משתמש

## 📋 דרישות

```bash
pip install -r requirements.txt
```

## ▶️ הפעלה

### מקומית
```bash
python scraper.py
```

### דרך GitHub Actions
1. עבור ל: https://github.com/halfiitzik/israel-news/actions
2. בחר את ה-workflow `hourly-update`
3. לחץ **Run workflow**

## 📅 זמנים

- 🕐 **עדכון אוטומטי:** כל שעה בדיוק בשעה 00
- ⏰ **זמן עדכון:** ~2-3 דקות
- 📊 **מספר חדשות:** 50 חדשות ראשונות בכל עדכון

## 📁 מבנה הקבצים

```
israel-news/
├── scraper.py              # סקריפט אגרגציה חדשות
├── requirements.txt        # תלויות Python
├── index.html              # דף ההצגה (עדכני)
├── README.md               # קובץ זה
├── .gitignore              # קבצים לא לעקוב
└── .github/
    └── workflows/
        └── hourly-update.yml # GitHub Actions workflow
```

## 🔧 הגדרות

### שינוי תדירות העדכון

עדכן את הקובץ `.github/workflows/hourly-update.yml`:

```yaml
schedule:
  - cron: '0 * * * *'  # כל שעה
  # או:
  - cron: '0 */6 * * *'  # כל 6 שעות
  # או:
  - cron: '0 0 * * *'  # פעם ביום בשעה 00:00
```

### הוספת מקורות חדשות

ערוך את `scraper.py` והוסף URLs חדשים ל-`self.rss_feeds`:

```python
self.rss_feeds = [
    'https://example.com/rss.xml',
    # ...
]
```

## 🌐 צפיה בדף

### אפשרות 1 - GitHub Raw
```
https://raw.githubusercontent.com/halfiitzik/israel-news/main/index.html
```

### אפשרות 2 - GitHub Pages (אופציונלי)

1. Settings → Pages
2. Source: `main` branch, `/root`
3. הקישור יהיה: `https://halfiitzik.github.io/israel-news/`

## 📊 סטטיסטיקות

- 📰 **חדשות ליד כל עדכון:** 50
- 🔗 **מקורות חדשות:** 50+
- ⏱️ **זמן עדכון:** ~2-3 דקות
- 🔄 **תדירות עדכון:** כל שעה

## 🐛 פתרון בעיות

### אין עדכונים?

1. בדוק את GitHub Actions:
   - https://github.com/halfiitzik/israel-news/actions
   
2. בדוק את ה-Logs:
   - לחץ על הריצה האחרונה
   - בדוק את `Run news scraper`

### RSS Feeds לא עובד?

- התקן חבילות: `pip install -r requirements.txt`
- בדוק את הקישורים ב-`scraper.py`

### HTML לא מתעדכן?

- וודא ש-GitHub Actions enabled
- בדוק את ה-workflow file: `.github/workflows/hourly-update.yml`

## 💡 רעיונות לשיפור

- [ ] 🌙 מצב כהה (Dark Mode)
- [ ] 🔍 חיפוש בחדשות
- [ ] 🏷️ סינון לפי קטגוריות
- [ ] 📧 עדכוני Email
- [ ] 🐦 Twitter/X Integration
- [ ] 📱 PWA (Progressive Web App)
- [ ] 📊 Analytics ודיאגרמות
- [ ] 🎨 תבניות עיצוב נוספות

## 📝 רישיון

MIT License - חופשי להשתמש ולשנות

## 👤 מחבר

**halfiitzik** - https://github.com/halfiitzik

## 📞 תמיכה

יש בעיה? פתח Issue:
https://github.com/halfiitzik/israel-news/issues

---

**שמור דף זה בסימניות כדי לקבל עדכונים עדכניים על חדשות ישראל! 🚀**
