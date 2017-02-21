wget  https://raw.githubusercontent.com/HiggsBoson3310/hw1/master/DatosRadioSonda.dat
mkdir Convection
cd Convection
mv ../DatosRadioSonda.dat ../Convection
mv DatosRadioSonda.dat TempHeight.txt
python ../PLOTS_Convection.py
