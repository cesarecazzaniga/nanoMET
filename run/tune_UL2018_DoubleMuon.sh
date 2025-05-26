#UL2018 tuning
python tune_doublemu.py --addon v9 --year 2018 --ttbarModifier 1 --selection diMuon1718-tuneElectronVeto-onZ --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err 
python tune_doublemu.py --addon v9 --year 2018 --runData --selection diMuon1718-tuneElectronVeto-onZ --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err                                                                                                                              
