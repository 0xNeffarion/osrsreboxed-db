import requests
import subprocess

release = requests.get("https://api.github.com/repos/abextm/osrs-cache/releases/latest")
download_url = release.json()["assets"][0]["browser_download_url"]
tarball = requests.get(download_url)
open('cache.tar.gz', 'wb').write(tarball.content)
subprocess.run(["tar", "-xzvf", "cache.tar.gz", "-C", "data/cache", "--strip-components=1"])
subprocess.run(["rm", "cache.tar.gz"])
