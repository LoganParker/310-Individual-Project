#!/bin/bash
pip install nltk
pip install pyspellchecker
pip install stanza
pip install --upgrade google-cloud-translate
pip install requests
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\alien\School\310\310-Individual-Project\bot\credentia
ls.json"
python py_lib_install.py
sleep 10