# Core code credit: Simple downloading with progress indicator, by Cees Timmerman, 16mar12.
# Modified for GOES downloader by Jeff Kelly K2SDR
# version 8
# Converted to Python3 By RF-Fox/XE3FOX. Code is kept as close to original version as possible.

import os
import urllib.request, urllib.error, urllib.parse
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


timestr1 = time.strftime("Download Date:%m%d%Y Time:%H%M")
print(timestr1)

timestr = time.strftime("%m%d%Y_%H%M")

cwd = os.getcwd()

path = cwd + "/" + "GOES16_" + timestr

try:
    os.makedirs(path)
except OSError:
    pass
print("Image files will be saved to: " + path)	
print("")

remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/5424x5424.jpg"
local = path + "/FULLDISK_GEOCOLOR_5424x5424" + "_" + timestr + ".jpg"
u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")

fp.flush()
fp.close()
if not totalSize:
    print()




remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/01/5424x5424.jpg"
local = path + "/FULLDISK_BAND_01_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()




remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/02/5424x5424.jpg"
local = path + "/FULLDISK_BAND_02_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()




remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/03/5424x5424.jpg"
local = path + "/FULLDISK_BAND_03_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/04/5424x5424.jpg"
local = path + "/FULLDISK_BAND_04_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/05/5424x5424.jpg"
local = path + "/FULLDISK_BAND_05_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/06/5424x5424.jpg"
local = path + "/FULLDISK_BAND_06_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/07/5424x5424.jpg"
local = path + "/FULLDISK_BAND_07_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/08/5424x5424.jpg"
local = path + "/FULLDISK_BAND_08_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/09/5424x5424.jpg"
local = path + "/FULLDISK_BAND_09_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/10/5424x5424.jpg"
local = path + "/FULLDISK_BAND_10_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/11/5424x5424.jpg"
local = path + "/FULLDISK_BAND_11_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/12/5424x5424.jpg"
local = path + "/FULLDISK_BAND_12_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/13/5424x5424.jpg"
local = path + "/FULLDISK_BAND_13_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/14/5424x5424.jpg"
local = path + "/FULLDISK_BAND_14_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/15/5424x5424.jpg"
local = path + "/FULLDISK_BAND_15_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/16/5424x5424.jpg"
local = path + "/FULLDISK_BAND_16_5424x5424" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()












remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/5000x3000.jpg"
local = path + "/CONUS_GEOCOLOR_5000X3000.jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")

fp.flush()
fp.close()
if not totalSize:
    print()




remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/01/5000x3000.jpg"
local = path + "/CONUS_BAND_01_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()




remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/02/5000x3000.jpg"
local = path + "/CONUS_BAND_02_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()




remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/03/5000x3000.jpg"
local = path + "/CONUS_BAND_03_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/04/5000x3000.jpg"
local = path + "/CONUS_BAND_04_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/05/5000x3000.jpg"
local = path + "/CONUS_BAND_05_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/06/5000x3000.jpg"
local = path + "/CONUS_BAND_06_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/07/5000x3000.jpg"
local = path + "/CONUS_BAND_07_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/08/5000x3000.jpg"
local = path + "/CONUS_BAND_08_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/09/5000x3000.jpg"
local = path + "/CONUS_BAND_09_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/10/5000x3000.jpg"
local = path + "/CONUS_BAND_10_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/11/5000x3000.jpg"
local = path + "/CONUS_BAND_11_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/12/5000x3000.jpg"
local = path + "/CONUS_BAND_12_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/13/5000x3000.jpg"
local = path + "/CONUS_BAND_13_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/14/5000x3000.jpg"
local = path + "/CONUS_BAND_14_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/15/5000x3000.jpg"
local = path + "/CONUS_BAND_15_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()





remote = r"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/16/5000x3000.jpg"
local = path + "/CONUS_BAND_16_5000x3000" + "_" + timestr + ".jpg"

u = urllib.request.urlopen(remote)
h = u.info()
totalSize = int(h["Content-Length"])

print("Downloading %s bytes..." % totalSize, end=' ')
fp = open(local, 'wb')

blockSize = 8192 #100000 # urllib.urlretrieve uses 8192
count = 0
while True:
    chunk = u.read(blockSize)
    if not chunk: break
    fp.write(chunk)
    count += 1
    if totalSize > 0:
        percent = int(count * blockSize * 100 / totalSize)
        if percent > 100: percent = 100
        print("%2d%%" % percent, end=' ')
        if percent < 100:
            print("\b\b\b\b\b", end=' ')  # Erase "NN% "
        else:
            print("Done.")
fp.flush()
fp.close()
if not totalSize:
    print()
