# Jill-Jênn Vie

My webpage, a collection of reStructuredText files for Sphinx.

    python3 -m venv venv
    source venv activate
    pip install -r requirements.txt  # To install Sphinx

Then you can have minimal configuration:

    mkdir _static /tmp/stats
    echo 'FLASK_DIR="/tmp"' > secret.py
    python demotivators.py
    python anime-sheet-music.py
    make html
