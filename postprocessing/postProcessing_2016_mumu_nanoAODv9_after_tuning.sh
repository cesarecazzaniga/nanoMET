#CES: UL legacy 2016
##preVPF MC
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples DYJetsToLL_M50 #SPLIT180  
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples DYJetsToLL_M50_NLO #SPLIT180                                                                                                             
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples TTLep_pow_CP5 #SPLIT40    
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples TToLeptons_sch_amcatnlo #SPLIT40   
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples T_tch_pow #SPLIT12 
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples TBar_tch_pow #SPLIT12 
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples T_tWch #SPLIT12   
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples TBar_tWch #SPLIT11                                                                                                                        
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples WZTo3LNu #SPLIT20                                                                                                                                                                                                                                                  
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples WWW_4F #SPLIT5                                                                                                                                
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples WWZ_4F #SPLIT5                                                                                                                                   
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples WZZ #SPLIT5                                                                                                                                   
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --prevfp --after_tuning --samples ZZZ #SPLIT5    

##nanoAODv9 MC (postVPF)
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples DYJetsToLL_M50 #SPLIT180
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples DYJetsToLL_M50_NLO #SPLIT180                                                                                                               
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples TTLep_pow_CP5 #SPLIT40    
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples TToLeptons_sch_amcatnlo #SPLIT40   
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples T_tch_pow #SPLIT12 
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples TBar_tch_pow #SPLIT12 
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples T_tWch #SPLIT12   
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples TBar_tWch #SPLIT11                                                                                                                        
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples WZTo3LNu #SPLIT20                                                                                                                                                                                                                                                  
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples WWW_4F #SPLIT5                                                                                                                                
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples WWZ_4F #SPLIT5                                                                                                                                   
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples WZZ #SPLIT5                                                                                                                                   
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples ZZZ #SPLIT5 

##preVPF DATA
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --prevfp --samples DoubleMuon_Run2016Bver1_preVFP #SPLIT50                                                                                                   
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --prevfp --samples DoubleMuon_Run2016Bver2_preVFP #SPLIT50                                                                                                        
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --prevfp --samples DoubleMuon_Run2016C_preVFP #SPLIT50                                                                                                        
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --prevfp --samples DoubleMuon_Run2016D_preVFP #SPLIT50                                                                                                        
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --prevfp --samples DoubleMuon_Run2016E_preVFP #SPLIT50                                                                                                        
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --prevfp --samples DoubleMuon_Run2016F_preVFP #SPLIT50                                                                                                        

##nanoAODv9 DATA (postVPF)
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples DoubleMuon_Run2016F #SPLIT50
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples DoubleMuon_Run2016G #SPLIT50
python postProcessing.py --skim dimuon --era v9 --year 2016 --ul --after_tuning --samples DoubleMuon_Run2016H #SPLIT50

