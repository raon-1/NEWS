import json, urllib.request, urllib.parse, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

# 2026년 11월 전체 뉴스 날짜 범위
START = "2026-11-01"
END = "2026-12-01"
QUERIES = {
 "전력": "전력 산업 전력망",
 "신재생에너지": "태양광 OR 풍력 OR 신재생에너지",
 "배터리": "배터리 OR ESS 에너지저장",
 "전기차": "전기차 충전",
 "전기 안전": "전기 안전 사고 예방",
 "전기 기술": "전기 기술 OR 스마트그리드 OR 발전 기술"
}
def fetch(query):
 q=f"{query} after:{START} before:{END}"
 url="https://news.google.com/rss/search?q="+urllib.parse.quote(q,safe="")+"&hl=ko&gl=KR&ceid=KR:ko"
 req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; ElectricNewsLab/1.0)"})
 try:
  with urllib.request.urlopen(req,timeout=25) as r:return ET.fromstring(r.read())
 except Exception as e:
  print("RSS fetch error:",e);return None
articles=[];seen=set()
for category,query in QUERIES.items():
 root=fetch(query)
 if root is None:continue
 for item in root.findall("./channel/item"):
  title=item.findtext("title","").strip();link=item.findtext("link","").strip()
  if not title or not link or link in seen:continue
  seen.add(link);source=item.find("source");source_name=source.text if source is not None else "뉴스"
  pub=item.findtext("pubDate","")
  try:date=parsedate_to_datetime(pub).strftime("%Y-%m-%d")
  except:date=""
  articles.append({"title":title,"url":link,"source":source_name,"date":date,"category":category,"summary":"기사 원문을 읽으며 관련 전기·에너지 기술과 용어를 공부해 보세요."})
articles.sort(key=lambda x:x.get("date",""),reverse=True)
out={"updated":datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M"),"period":"2026-11","articles":articles}
with open("data/news.json","w",encoding="utf-8") as f:json.dump(out,f,ensure_ascii=False,indent=2)
print("Saved",len(articles),"November 2026 articles")
