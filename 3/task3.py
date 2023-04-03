import urllib.request
import json

def frequency_count(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode()

    freq = {}
    for char in html:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    with open('readme.md', 'w') as f:
        json.dump(freq, f, indent=4)

freq = frequency_count("https://www.python.org")

print("results were written in readme.md")