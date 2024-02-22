#UL2017 tuning
python tune.py --addon v2 --year 2017 --ttbarModifier 1 --selection diMuon-looseLeptonVeto-onZ-noEEJets --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err 
python tune.py --addon v2 --year 2017 --runData --selection diMuon-looseLeptonVeto-onZ-noEEJets --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err                                                                                                                                               
