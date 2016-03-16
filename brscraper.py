from bs4 import BeautifulSoup
import urllib.request
import requests

class BRScraper:
    
    def __init__(self, server_url="http://www.baseball-reference.com/"):
        self.server_url = server_url
    
    def parse_tables(self, resource, table_ids=None, verbose=False):
        """
        Given a resource on the baseball-reference server (should consist of 
        the url after the hostname and slash), returns a dictionary keyed on 
        table id containing arrays of data dictionaries keyed on the header 
        columns. table_ids is a string or array of strings that can optionally 
        be used to filter out which stats tables to return. 
        """

        def is_parseable_table(tag):
            if not tag.has_attr("class"): return False
            return tag.name == "table" and "stats_table" in tag["class"] and "sortable" in tag["class"]

        def is_parseable_row(tag):
            if not tag.name == "tr": return False
            if not tag.has_attr("class"): return True  # permissive
            return "league_average_table" not in tag["class"] and "stat_total" not in tag["class"] and "minors_table" not in tag["class"]

        if isinstance(table_ids, str): table_ids = [table_ids]

        page = requests.get(self.server_url + resource) 
#        print(page.headers)
#        print(page.encoding)
#        print(page.text)
        soup = BeautifulSoup(page.text,"html.parser")

        # Filter out batting tables for pitchers and pitching tables for hitters - AE

        def get_role(soup):
            if soup.find(itemprop="role"):
                role = soup.find(itemprop="role").get_text()
#            print("Role found: ",role)
            return role
        #       print(table_ids)

        role = ''
        if "players" in resource:
            role = get_role(soup)
            if "Pitcher" in role:
                table_ids = ["pitching_standard"]
            elif role:
                table_ids = ["batting_standard"]


        tables = soup.find_all(is_parseable_table)
        data = {}

#        print("Parsing with table_ids set to ",table_ids)

        # Read through each table, read headers as dictionary keys
        for table in tables:
#            print("Table found with id ",table["id"])
            
            if table_ids != None and table["id"] not in table_ids: continue
            if verbose: print("Processing table " + table["id"])
            data[table["id"]] = []
            
            headers = table.find("thead").find_all("th")
            header_names = []
            for header in headers:
                if header.string == None: 
                    base_header_name = u""
                else: base_header_name = header.string.strip()
                if base_header_name in header_names:
                    i = 1
                    header_name = base_header_name + "_" + str(i)
                    while header_name in header_names:
                        i += 1
                        header_name = base_header_name + "_" + str(i)
                    if verbose: 
                        if base_header_name == "":
                            print("Empty header relabeled as %s" % header_name)
                        else:
                            print("Header %s relabeled as %s" % (base_header_name, header_name))
                else:
                    header_name = base_header_name
                header_names.append(header_name)
            
            rows = table.find("tbody").find_all(is_parseable_row)
            for row in rows:
                entries = row.find_all("td")
                entry_data = []
                for entry in entries:
#                   if entry == entries[0]:
#                        print(type(entry))
#                        print(entry)
                    if entry.string == None:
                        if len(entry.contents) > 1:
                            entry_data.append(entry.contents[0])
                            continue
                        entry_data.append(u"")
                    else:
                        entry_data.append(entry.string.strip())
                if len(entry_data) > 0:
                    data[table["id"]].append(dict(zip(header_names, entry_data)))
        
        return data,role


scraper = BRScraper()
#data = scraper.parse_tables("players/r/rodrial01.shtml",['batting_standard'],True)
#print(data)
