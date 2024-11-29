
source .venv/bin/activate
DST="./imgs/"

[ -d "$DST" ] || mkdir -p $DST

##################################################################################
#   plot 2.1 Interference
##################################################################################

echo "plotting single slit"
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

echo "plotting double slit"
python plot_csv.py \
    --reg-mode=none \
    --outfile $DST/2.2_Doppelspalt.png \
    ./data/2.2_doppelspalt.csv
# fit over double is not stable
python plot_csv.py \
    --reg-mode=single_max \
    --mirror \
    --outfile $DST/2.2_Doppelspalt.fit.png \
    ./data/2.2_doppelspalt.csv

##################################################################################
#   plot 2.3 lloyd mirror
##################################################################################

echo "plotting lloyd mirror"
python plot_csv.py \
    --reg-mode=none \
    --outfile $DST/2.3_lloydspiegel.png \
    ./data/2.3_lloydspiegel.csv

##################################################################################
#   plot 2.4 double generator
##################################################################################

echo "plotting double generator"
python plot_csv.py \
    --reg-mode=none \
    --outfile $DST/2.4_doppelgenerator.png \
    ./data/2.4_doppelgenerator.csv

python plot_csv.py \
    --reg-mode=single_max \
    --mirror \
    --outfile $DST/2.4_doppelgenerator.fit.png \
    ./data/2.4_doppelgenerator.csv

deactivate
