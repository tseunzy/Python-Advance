
#  PDF Document Downloader

import time
import requests
import concurrent.futures
import os

# Sample PDF URLs (public domain documents)
pdf_urls = [
    'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
    'https://www.africau.edu/images/default/sample.pdf',
    'https://www.orimi.com/pdf-test.pdf',
    'https://www.clickdimensions.com/links/TestPDFfile.pdf',
    'https://www.adobe.com/support/products/enterprise/knowledgecenter/media/c4611_sample_explain.pdf',
    'https://www.hq.nasa.gov/alsj/a17/A17_FlightPlan.pdf',
    'https://www.ets.org/Media/Tests/GRE/pdf/gre_research_validity_data.pdf',
    'https://css4.pub/2015/weather/weather.pdf',
]


#WITHOUT THREAD
# for pdf in pdf_urls:        # Loop through each PDF link
#     try:
#         response = requests.get(pdf, timeout=10)    # Download the file
#         response.raise_for_status()         # Check for errors

#         pdf_name = pdf.split('/')[-1]           # Extract filename from URL

#         with open(pdf_name, 'wb') as pdf_file:  # Save file in binary mode
#             pdf_file.write(response.content)

#         print(f"Downloaded: {filename}")

#     except Exception as e:            # Catch any error that happens during download.
#         return f"Failed: {url} -> {e}"
        

DOWNLOAD_DIR = "downloads"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

start = time.time()
def download_pdf(url):
    try:
        response = requests.get(url, timeout=20)      # Download the file & Wait up to 20 seconds before giving up
        response.raise_for_status()                   # Check for errors

        pdf_name = url.split("/")[-1] or "file.pdf"       # Extract filename from URL
        filepath = os.path.join(DOWNLOAD_DIR, pdf_name)

        with open(filepath, "wb") as f:               # Save file in binary mode
            f.write(response.content)

        return f"✅ Downloaded: {pdf_name}"

    except Exception as e:                          # Catch any error that happens during download.
        return f"❌ Failed: {url} -> {e}"


# max_workers is a thread that does a job - Create a pool of 10 threads that can work at the same time.
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    futures = []
    for url in pdf_urls:
        futures.append(executor.submit(download_pdf, url))

    for future in concurrent.futures.as_completed(futures):
        print(future.result())

end = time.time()
print(f'Finished in {round((end-start),2)} seconds')
