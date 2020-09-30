import time
from datetime import date
from spydr.spydr import Spydr
from urllib.parse import urlparse


target_url = input("Enter the URL to crawl:\t")

start_time = time.time()

domain_file_name = urlparse(target_url).netloc.replace(".", "_")

result = Spydr().crawl(target_url)

end_time = time.time()

print(f"\n{len(result)} URLs Crawled in {end_time - start_time} seconds")

file_name = domain_file_name + "_" + str(date.today().isoformat()) + ".txt"

with open(file_name, 'w') as wf:
    for entry in result:
        wf.write(entry + "\n")
        
print("Result file created!")