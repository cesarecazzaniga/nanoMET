#UL2018 tuning
python tune_singlemu.py --addon v9 --year 2018 --ttbarModifier 1 --selection TunegoodIsoMuons18-zeroGoodJetVeto --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err 
python tune_singlemu.py --addon v9 --year 2018 --runData         --selection TunegoodIsoMuons18-zeroGoodJetVeto --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err                                                                                                                                               

python tune_singlemu.py --addon v9 --year 2018 --ttbarModifier 1 --selection TunegoodIsoMuons18-zeroGoodJets --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err 
python tune_singlemu.py --addon v9 --year 2018 --runData         --selection TunegoodIsoMuons18-zeroGoodJets --maxSig 25 --jetThreshold 15 --pTdependent #>> /dev/null 2>>tune.err                                                                                                                                               
