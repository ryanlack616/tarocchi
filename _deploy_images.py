"""Upload data/images/ to FTP, reconnecting per deck to avoid timeouts."""
import ftplib, os, time

HOST = 'pixie-ss1-ftp.porkbun.com'
USER = 'tarocchi.help'
PW   = 'HxJKsLbZrzKRamxh9Vyq^mCD'

def connect():
    ftp = ftplib.FTP()
    ftp.connect(HOST, timeout=60)
    ftp.login(USER, PW)
    ftp.set_pasv(True)
    return ftp

def ensure_dir(ftp, name):
    try:
        ftp.mkd(name)
    except ftplib.error_perm:
        pass

def get_existing(ftp):
    try:
        return set(ftp.nlst())
    except Exception:
        return set()

images_root = os.path.join('data', 'images')

# ── manifest.json ────────────────────────────────────────────────
ftp = connect()
ensure_dir(ftp, 'data')
ftp.cwd('data')
ensure_dir(ftp, 'images')
ftp.cwd('images')
manifest_path = os.path.join(images_root, 'manifest.json')
with open(manifest_path, 'rb') as f:
    ftp.storbinary('STOR manifest.json', f)
print('UPLOADED manifest.json')
ftp.quit()

# ── each deck — fresh connection per deck ────────────────────────
for deck_id in sorted(os.listdir(images_root)):
    deck_dir = os.path.join(images_root, deck_id)
    if not os.path.isdir(deck_dir):
        continue

    files = sorted(f for f in os.listdir(deck_dir) if os.path.isfile(os.path.join(deck_dir, f)))
    if not files:
        continue

    ftp = connect()
    ftp.cwd('data/images')
    ensure_dir(ftp, deck_id)
    ftp.cwd(deck_id)
    existing = get_existing(ftp)

    uploaded = skipped = errors = 0
    for fname in files:
        if fname in existing:
            skipped += 1
            continue
        local_path = os.path.join(deck_dir, fname)
        for attempt in range(3):
            try:
                with open(local_path, 'rb') as f:
                    ftp.storbinary(f'STOR {fname}', f)
                uploaded += 1
                break
            except (ftplib.all_errors, OSError) as e:
                print(f'  RETRY {attempt+1} {fname}: {e}')
                time.sleep(2)
                try:
                    ftp.quit()
                except Exception:
                    pass
                ftp = connect()
                ftp.cwd(f'data/images/{deck_id}')
        else:
            errors += 1
            print(f'  FAILED {fname}')

    print(f'{deck_id}: {uploaded} uploaded, {skipped} skipped, {errors} errors  ({len(files)} total)')
    try:
        ftp.quit()
    except Exception:
        pass

print('DONE')
