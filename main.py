import json
import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

countries = soup.find_all("div", class_="col-md-4 country")
count = 1
data = []
for country in countries:
    country_name = country.find("h3").get_text(strip=True)
    capital = country.find("span", class_="country-capital").get_text(strip=True)
    print(f"{count}. Country: {country_name}; Capital: {capital};")
    count += 1
    data.append({"country": country_name, "capital": capital})

with open("dump.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)


html_table = """
<!DOCTYPE html>
<html>
<head>
  <title>Страны и столицы</title>
  <style>
    table, th, td {
      border: 1px solid rgb(207, 4, 156);
      border-collapse: collapse;
      background: rgb(159, 103, 173);
      text-align: center;
    }
  </style>
</head>
<body>
  <h1>Страны и столицы</h1>
  <table>
    <thead>
      <tr>
        <th>№</th>
        <th>Страна</th>
        <th>Столица</th>
      </tr>
    </thead>
    <tbody>
"""

count = 1
for item in data:
    html_table += f"""
      <tr>
        <td>{count}</td>
        <td>{item["country"]}</td>
        <td>{item["capital"]}</td>
      </tr>
"""
    count += 1

html_table += """
    </tbody>
  </table>
</body>
</html>
"""

# Записать HTML-код в файл Index.html
with open("Index.html", "w", encoding="utf-8") as f:
    f.write(html_table)