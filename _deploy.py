import ftplib, os

host = 'pixie-ss1-ftp.porkbun.com'
user = 'tarocchi.help'
pw   = 'HxJKsLbZrzKRamxh9Vyq^mCD'

ftp = ftplib.FTP(host)
ftp.login(user, pw)
ftp.set_pasv(True)
print('LOGIN OK')
print('ROOT:', ftp.nlst())

# Ensure data/ directory exists
try:
    ftp.mkd('data')
    print('Created data/')
except ftplib.error_perm:
    print('data/ already exists')

# Upload index.html
with open('index.html', 'rb') as f:
    ftp.storbinary('STOR index.html', f)
print('UPLOADED index.html')

# Upload data/cards.json
ftp.cwd('data')
with open('data/cards.json', 'rb') as f:
    ftp.storbinary('STOR cards.json', f)
print('UPLOADED data/cards.json')

with open('data/spreads.json', 'rb') as f:
    ftp.storbinary('STOR spreads.json', f)
print('UPLOADED data/spreads.json')

with open('data/historical_decks.json', 'rb') as f:
    ftp.storbinary('STOR historical_decks.json', f)
print('UPLOADED data/historical_decks.json')

with open('data/card_witnesses.json', 'rb') as f:
    ftp.storbinary('STOR card_witnesses.json', f)
print('UPLOADED data/card_witnesses.json')

ftp.cwd('..')
# Upload explorer.html
with open('explorer.html', 'rb') as f:
    ftp.storbinary('STOR explorer.html', f)
print('UPLOADED explorer.html')

# Upload data/images/ recursively
images_root = os.path.join('data', 'images')
if os.path.isdir(images_root):
    # Ensure data/images/ exists
    ftp.cwd('data')
    try:
        ftp.mkd('images')
        print('Created data/images/')
    except ftplib.error_perm:
        print('data/images/ already exists')
    ftp.cwd('images')

    # Upload manifest.json
    manifest_path = os.path.join(images_root, 'manifest.json')
    if os.path.isfile(manifest_path):
        with open(manifest_path, 'rb') as f:
            ftp.storbinary('STOR manifest.json', f)
        print('UPLOADED data/images/manifest.json')

    # Upload each deck subdir
    for deck_id in sorted(os.listdir(images_root)):
        deck_dir = os.path.join(images_root, deck_id)
        if not os.path.isdir(deck_dir):
            continue
        try:
            ftp.mkd(deck_id)
            print(f'Created data/images/{deck_id}/')
        except ftplib.error_perm:
            pass  # already exists
        ftp.cwd(deck_id)
        # Get already-uploaded files to skip them
        try:
            existing = set(ftp.nlst())
        except Exception:
            existing = set()
        files = [f for f in os.listdir(deck_dir) if os.path.isfile(os.path.join(deck_dir, f))]
        uploaded = 0
        skipped = 0
        for fname in sorted(files):
            if fname in existing:
                skipped += 1
                continue
            with open(os.path.join(deck_dir, fname), 'rb') as f:
                ftp.storbinary(f'STOR {fname}', f)
            uploaded += 1
        print(f'UPLOADED data/images/{deck_id}/ ({uploaded} new, {skipped} skipped of {len(files)} total)')
        ftp.cwd('..')

    ftp.cwd('../..')
else:
    print('No data/images/ directory found — skipping image upload')

ftp.quit()
print('DONE')
