mkdir -p data/esc-50
wget https://github.com/karoldvl/ESC-50/archive/master.zip -P data/esc-50
cd data/esc-50
unzip master.zip
rm -f master.zip
mv master/ESC-50-master/audio .

