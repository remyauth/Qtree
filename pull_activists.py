import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_LGBT_rights_activists"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# This is a rough structure: <ul><li><a href=...>Name</a> Description...</li></ul>
entries = soup.select("ul > li > a[href^='/wiki/']")

people = []

for a in entries:
    parent_li = a.find_parent("li")
    if not parent_li: continue

    name = a.text.strip()
    link = "https://en.wikipedia.org" + a['href']
    full_text = parent_li.text.strip()

    # Try to remove the name from the start of the bio
    bio = full_text.replace(name, "").strip(" –—:,.")
    
    person = {
        "name": name,
        "wikipedia": link,
        "bio": bio,
        "tags": ["activist"]  # can refine later
    }

    people.append(person)

# Save to JSON
with open("figures.json", "w", encoding="utf-8") as f:
    json.dump(people, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(people)} entries.")


