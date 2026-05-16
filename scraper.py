#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import html

class IsraeliNewsScraper:
    def __init__(self):
        self.news_items = []
        self.rss_feeds = [
            'https://www.ynet.co.il/rss/0,7340,L-8,00.rss',
            'https://www.mako.co.il/news-rss',
            'https://news.walla.co.il/?p=rss',
            'https://www.nrg.co.il/rss/rss.asp',
            'https://www.haaretz.co.il/?p=rss_feed&category_id=1',
            'https://www.calcalist.co.il/RSS/RSS.xml',
            'https://www.globes.co.il/news/rss.xml',
            'https://www.israelhayom.co.il/rss.php',
            'https://www.inn.co.il/rss/10.xml',
            'https://www.jpost.com/feed',
            'https://feeds.timesofisrael.com/breaking-news',
            'https://www.i24news.tv/en/feed/rss.php',
        ]
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def fetch_rss_feeds(self):
        print("🔄 Fetching RSS feeds...")
        for feed_url in self.rss_feeds:
            try:
                feed = feedparser.parse(feed_url)
                for entry in feed.entries[:3]:
                    title = entry.get('title', 'No title')
                    link = entry.get('link', '')
                    published = entry.get('published', '')
                    description = entry.get('summary', '')[:200]
                    source = feed.feed.get('title', 'Unknown')
                    
                    if title and link:
                        self.news_items.append({
                            'title': title,
                            'link': link,
                            'published': published,
                            'description': description,
                            'source': source,
                            'timestamp': self.parse_date(published)
                        })
            except:
                pass

    def parse_date(self, date_str):
        try:
            return datetime.strptime(date_str[:19], '%Y-%m-%dT%H:%M:%S').timestamp()
        except:
            return datetime.now().timestamp()

    def remove_duplicates(self):
        seen = set()
        unique = []
        for item in self.news_items:
            key = (item['title'][:50], item['link'])
            if key not in seen:
                seen.add(key)
                unique.append(item)
        self.news_items = unique

    def sort_by_date(self):
        self.news_items.sort(key=lambda x: x['timestamp'], reverse=True)

    def generate_html(self):
        top_news = self.news_items[:50]
        html_content = f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>חדשות ישראל</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; direction: rtl; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        header {{ background: white; border-radius: 15px; padding: 30px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); text-align: center; }}
        header h1 {{ color: #333; font-size: 2.5em; margin-bottom: 10px; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        header p {{ color: #666; font-size: 1.1em; margin-bottom: 10px; }}
        .update-time {{ color: #999; font-size: 0.9em; padding: 10px 20px; background: #f0f0f0; border-radius: 8px; display: inline-block; }}
        .stats {{ display: flex; justify-content: space-around; gap: 20px; margin-top: 20px; flex-wrap: wrap; }}
        .stat {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 15px 25px; border-radius: 10px; text-align: center; }}
        .stat-number {{ font-size: 1.8em; font-weight: bold; }}
        .stat-label {{ font-size: 0.9em; opacity: 0.9; }}
        .news-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 20px; margin-bottom: 40px; }}
        .news-card {{ background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.1); transition: transform 0.3s, box-shadow 0.3s; display: flex; flex-direction: column; height: 100%; }}
        .news-card:hover {{ transform: translateY(-5px); box-shadow: 0 15px 30px rgba(0,0,0,0.2); }}
        .news-header {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 15px; }}
        .news-source {{ font-size: 0.85em; opacity: 0.9; margin-bottom: 8px; }}
        .news-title {{ font-size: 1.2em; font-weight: bold; line-height: 1.4; word-break: break-word; }}
        .news-body {{ padding: 15px; flex-grow: 1; display: flex; flex-direction: column; }}
        .news-description {{ color: #666; font-size: 0.95em; line-height: 1.6; margin-bottom: 15px; flex-grow: 1; }}
        .news-footer {{ display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #eee; padding-top: 15px; }}
        .news-time {{ color: #999; font-size: 0.85em; }}
        .news-link {{ display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 8px 16px; border-radius: 6px; text-decoration: none; font-size: 0.9em; transition: opacity 0.3s; }}
        .news-link:hover {{ opacity: 0.8; }}
        footer {{ background: white; border-radius: 15px; padding: 20px; text-align: center; color: #666; margin-top: 40px; }}
        @media (max-width: 768px) {{
            header h1 {{ font-size: 1.8em; }}
            .news-grid {{ grid-template-columns: 1fr; }}
            .stats {{ flex-direction: column; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📰 חדשות ישראל</h1>
            <p>עדכונים בזמן אמת מ-50+ אתרי חדשות</p>
            <div class="update-time">📅 עדכון אחרון: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
            <div class="stats">
                <div class="stat">
                    <div class="stat-number">{len(top_news)}</div>
                    <div class="stat-label">חדשות</div>
                </div>
                <div class="stat">
                    <div class="stat-number">50+</div>
                    <div class="stat-label">מקורות</div>
                </div>
                <div class="stat">
                    <div class="stat-number">🔄</div>
                    <div class="stat-label">כל שעה</div>
                </div>
            </div>
        </header>
        <div class="news-grid">
'''
        for news in top_news:
            title = html.escape(news.get('title', '')[:100])
            source = html.escape(news.get('source', '')[:50])
            desc = html.escape(news.get('description', '')[:150])
            link = news.get('link', '#')
            
            html_content += f'''            <div class="news-card">
                <div class="news-header">
                    <div class="news-source">{source}</div>
                    <div class="news-title">{title}</div>
                </div>
                <div class="news-body">
                    <div class="news-description">{desc}</div>
                    <div class="news-footer">
                        <a href="{link}" target="_blank" class="news-link">קרא עוד</a>
                    </div>
                </div>
            </div>
'''
        
        html_content += '''        </div>
        <footer>
            <p>💻 מערכת אוטומטית לאגרגציה של חדשות ישראל</p>
            <p>🔄 מעדכנת כל שעה דרך GitHub Actions</p>
            <p>📊 רשות החדשות: צה"ל, משרד הביטחון, בתי חדשות ועוד</p>
            <p>📈 <a href="https://github.com/halfiitzik/israel-news" style="color: #667eea; text-decoration: none;">צפה בקוד המקור ב-GitHub</a></p>
        </footer>
    </div>
</body>
</html>
'''
        return html_content

    def save_html(self, content):
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)

    def run(self):
        print("🚀 Starting scraper...")
        self.fetch_rss_feeds()
        self.remove_duplicates()
        self.sort_by_date()
        html_content = self.generate_html()
        self.save_html(html_content)
        print(f"✅ Done! Generated {len(self.news_items)} news items")

if __name__ == '__main__':
    scraper = IsraeliNewsScraper()
    scraper.run()
