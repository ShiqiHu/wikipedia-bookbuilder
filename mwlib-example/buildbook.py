import subprocess

METABOOK = 'metabook.physics.json'
ZIP_FILE = 'physics.zip'
PDF_FILE = 'physics.pdf'

# Extract metabook defined English Wikipedia contents into an interim zip file
# execute: mw-zip -c :en -m metabook.physics.json -o physics.zip
subprocess.call(['mw-zip', '-c', ':en', '-m', METABOOK, '-o' ZIP_FILE])


# Render the zip file contents to a pdf file with the reportlab writer
# execute: mw-render -c physics.zip -o physics.pdf -w rl
subprocess.call(['mw-render', '-c', ZIP_FILE, '-o', PDF_FILE, '-w', 'rl'])

