#UL2018 tuning
#python tune.py --addon v2 --year 2018 --ttbarModifier 1 --selection diMuon-looseLeptonVeto-onZ-noEEJets --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err 
#python tune.py --addon v2 --year 2018 --runData         --selection diMuon-looseLeptonVeto-onZ-noEEJets --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err                                                                                                                                               

python tune_singlemu.py --addon v9 --year 2018 --ttbarModifier 1 --selection diMuon-looseLeptonVeto-onZ-noEEJets --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err 
python tune_singlemu.py --addon v9 --year 2018 --runData         --selection diMuon-looseLeptonVeto-onZ-noEEJets --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err                                                                                                                                               

