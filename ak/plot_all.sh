
source .venv/bin/activate
DST="./imgs/"

[ -d "$DST" ] || mkdir -p $DST

##################################################################################
#   plot 2.1 Interference
##################################################################################

python plot_csv.py \
    --reg-mode=none \
    --outfile $DST/2.1_Interferenz.png \
    ./data/2.1_Interferenz.csv

python plot_csv.py \
    --reg-mode=single \
    --mirror \
    --outfile $DST/2.1_Interferenz.fit.png \
    ./data/2.1_Interferenz.csv



##################################################################################
#   plot 2.3 Double Slit 
##################################################################################

python plot_csv.py \
    --reg-mode=none \
    --outfile $DST/2.2_Doppelspalt.png \
    ./data/2.2_doppelspalt.csv
# fit does is not stable
: 'python plot_csv.py \
    --reg-mode=double \
    --mirror \
    --outfile $DST/2.2_Doppelspalt.fit.png \
    ./data/2.2_doppelspalt.csv'

##################################################################################
#   plot 2.3 lloyd mirror
##################################################################################

python plot_csv.py \
    --reg-mode=none \
    --outfile $DST/2.3_lloydspiegel.png \
    ./data/2.3_lloydspiegel.csv

##################################################################################
#   plot 2.4 double generator
##################################################################################

python plot_csv.py \
    --reg-mode=none \
    --outfile $DST/2.4_doppelgenerator.png \
    ./data/2.4_doppelgenerator.csv

:'python plot_csv.py \
    --reg-mode=double \
    --mirror \
    --outfile $DST/2.4_doppelgenerator.fit.png \
    ./data/2.4_doppelgenerator.csv'
