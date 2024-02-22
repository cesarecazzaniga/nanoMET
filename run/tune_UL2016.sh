#UL2016 tuning
#python tune.py --addon v9 --year 2016 --ttbarModifier 1 --selection diMuon-looseLeptonVeto-onZ-noEEJets --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err 
#python tune.py --addon v9 --year 2016 --runData         --selection diMuon-looseLeptonVeto-onZ-noEEJets --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err                                                                                                                                               

#python tune.py --addon v9 --year 2016 --ttbarModifier 1 --selection diMuon-looseLeptonVeto-onZ-noEEJets --maxSig 25 --jetThreshold 15 --pTdependent --prevfp #>> /dev/null 2>>tune.err 
python tune.py --addon v9 --year 2016 --runData  --selection diMuon-looseLeptonVeto-onZ-noEEJets --maxSig 25 --jetThreshold 15 --pTdependent --prevfp #>> /dev/null 2>>tune.err                                                                                                                                               
