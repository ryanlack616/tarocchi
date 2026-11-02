import ftplib, os
_pw = os.environ.get('TAROCCHI_FTP_PASS', '')
if not _pw:
    raise SystemExit('TAROCCHI_FTP_PASS not set in environment')
ftp = ftplib.FTP('pixie-ss1-ftp.porkbun.com')
ftp.login('tarocchi.help', _pw)
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
