from bs4 import BeautifulSoup
import requests

def scrape_agmarknet(commodity, state, market):
    # Construct URL as per site structure
    url = f"https://agmarknet.gov.in/SomePath?commodity={commodity}&state={state}&market={market}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    # Find table, parse rows
    # rows = table.find_all("tr")
    # result = []
    # for row in rows[1:]:
    #     cols = row.find_all("td")
    #     result.append({
    #         "Min Price": cols[2].text.strip(),
    #         "Max Price": cols[3].text.strip(),
    #         "Modal Price": cols[4].text.strip(),
    #         "Date": cols[1].text.strip()
    #     })
    return soup.prettify()  # Placeholder return

print(scrape_agmarknet("Onion", "Karnataka", "Bangalore"))