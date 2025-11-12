import feedparser, textwrap, json, re
feed = feedparser.parse('https://www.theverge.com/rss/index.xml')
entry = feed.entries[0]
title = entry.title
summary = re.sub('<[^<]+?>', '', entry.summary)
content = f"{title}\n\n{summary}"
with open("out/title.txt","w") as f: f.write(title)
with open("out/desc.txt","w") as f: f.write(summary)
with open("out/script.txt","w") as f: f.write(textwrap.fill(content, 80))
print("✅ Script ready")
