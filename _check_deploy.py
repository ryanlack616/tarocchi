import ftplib
ftp = ftplib.FTP('pixie-ss1-ftp.porkbun.com')
ftp.login('tarocchi.help', 'HxJKsLbZrzKRamxh9Vyq^mCD')
ftp.cwd('data/images')
items = ftp.nlst()
print('data/images/ contents:', items)
for item in items:
    if item in ('manifest.json',):
        continue
    try:
        ftp.cwd(item)
        files = ftp.nlst()
        print(f'  {item}/: {len(files)} files')
        ftp.cwd('..')
    except Exception:
        pass
ftp.quit()
