import zipfile
import sys
from pathlib import Path


# A list of common encodings:
# current_default_encoding = 'iso-8859-1'   # identical to latin-1, used in some English versions of macOS
# current_default_encoding = 'gb18030'      # Chinese envs, used in some Chinese versions of Windows
current_default_encoding = 'cp437'          # Code Page 437, i.e. DOS Latin US, used in some English versions of Windows 
# current_default_encoding = 'shift-jis'    # Japenese envs, used in some Japenese versions of Windows
# current_default_encoding = 'utf-8'        # used in most linux distros

original_encoding = 'gb18030'

def unzip(f, encoding, v):
    print("Trying to unzip file " + f + " with encoding " + encoding + '...')
    try:
        with zipfile.ZipFile(f) as z:
            for i in z.namelist():
                print(i)
                n = Path(i.encode(current_default_encoding).decode(encoding))
                if v:
                    print(n)
                if i[-1] == '/':
                    if not n.exists():
                        n.mkdir()
                else:
                    with n.open('wb') as w:
                        w.write(z.read(i))
        print("Unzipped " + f)
    except UnicodeEncodeError as e:
        print(e)
        print("Failed to encode the filename with specified encoding, check the config. Aborted.")
    except UnicodeDecodeError as e:
        print(e)
        print("Failed to decode the filename with encoding " + encoding + ', maybe try another one. Aborted.')

if __name__ == '__main__':
    for i in sys.argv[1:]:
        unzip(i, original_encoding, True)
