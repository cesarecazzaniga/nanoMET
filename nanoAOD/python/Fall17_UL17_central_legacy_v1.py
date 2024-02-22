import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
    return argParser

if __name__=="__main__":
    # Logging
    import nanoMET.tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite
    if options.update:
        ov = 'update'
else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

# Redirector
from nanoMET.tools.user import redirector_global as redirector

# DB
from nanoMET.tools.user import dbDir
dbFile = dbDir+"/samples/DB_Fall17_UL17_central_legacy.sql"

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_LO      = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO",      "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=2075.14*3)

DY = [
    DYJetsToLL_M50_LO,
]

## ttbar
TTLep_pow       = Sample.nanoAODfromDAS("TTLep_pow",       "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=831.762*((3*0.108)**2))

## single top
TToLeptons_sch_amcatnlo = Sample.nanoAODfromDAS("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=(7.20+4.16)*0.108*3)
T_tch_pow               = Sample.nanoAODfromDAS("T_tch_pow",               "/ST_t-channel_top_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=136.02) # inclusive sample #LOR COMM BEFORE WITHOUT InclusiveDecays
TBar_tch_pow            = Sample.nanoAODfromDAS("TBar_tch_pow",            "/ST_t-channel_antitop_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=80.95) # inclusive sample #LOR COMM BEFORE WITHOUT InclusiveDecays
T_tWch_ext              = Sample.nanoAODfromDAS("T_tWch_ext",              "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=35.85*(1-(1-3*0.108)**2))
TBar_tWch_ext           = Sample.nanoAODfromDAS("TBar_tWch_ext",           "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=35.85*(1-(1-3*0.108)**2))

top = [
    TTLep_pow,
    TToLeptons_sch_amcatnlo,
    T_tch_pow,
    TBar_tch_pow,
    T_tWch_ext,
    TBar_tWch_ext,
]

## di/multiboson
#WWToLNuQQ     = Sample.nanoAODfromDAS("WWToLNuQQ",     "/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/schoef-crab_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1_legacy_nano_v3-f82d502d908e8d321edd6873d261cf31/USER", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=49.997)#LOR COMM! IT IS NOT AVAILABLE!!!!!!!
#WWTo1L1Nu2Q   = Sample.nanoAODfromDAS("WWTo1L1Nu2Q",   "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/schoef-crab_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1_legacy_nano_v3-f82d502d908e8d321edd6873d261cf31/USER", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=49.997)#LOR COMM! IT IS NOT AVAILABLE!!!!!!!

#ZZTo2L2Q  = Sample.nanoAODfromDAS("ZZTo2L2Q",  "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/schoef-crab_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1_legacy_nano_v3-f82d502d908e8d321edd6873d261cf31/USER", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=3.28)#LOR COMM! IT IS NOT AVAILABLE!!!!!!!

#WZTo1L3Nu         = Sample.nanoAODfromDAS("WZTo1L3Nu",         "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/schoef-crab_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1_legacy_nano_v3-f82d502d908e8d321edd6873d261cf31/USER", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=(47.13)*(3*0.108)*(0.2) ) #LOR COMM! IT IS NOT AVAILABLE!!!!!!!
#WZTo1L1Nu2Q       = Sample.nanoAODfromDAS("WZTo1L1Nu2Q",       "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/schoef-crab_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2_legacy_nano_v3-f82d502d908e8d321edd6873d261cf31/USER", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=10.71) #LOR COMM! IT IS NOT AVAILABLE!!!!!!!
#WZTo2L2Q          = Sample.nanoAODfromDAS("WZTo2L2Q",          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/schoef-crab_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1_legacy_nano_v3-f82d502d908e8d321edd6873d261cf31/USER", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=5.60) #LOR COMM! IT IS NOT AVAILABLE!!!!!!!
#WZTo3LNu          = Sample.nanoAODfromDAS("WZTo3LNu",      "/WZTo3LNu_13TeV-powheg-pythia8/schoef-crab_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2_legacy_nano_v4-f82d502d908e8d321edd6873d261cf31/USER", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=4.42965)  #LOR COMM! IT IS NOT AVAILABLE!!!!!!!

#VVTo2L2Nu = Sample.nanoAODfromDAS("VVTo2L2Nu", "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/schoef-crab_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1_legacy_nano_v3-f82d502d908e8d321edd6873d261cf31/USER", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=14.00) #LOR COMM! IT IS NOT AVAILABLE!!!!!!!

WWW_4F = Sample.nanoAODfromDAS("WWW_4F", "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=0.2086)#LOR COMM! ONLY RunIISummer20 IS AVAILABLE!!!!
WWZ_4F = Sample.nanoAODfromDAS("WWZ_4F", "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=0.1651)#LOR COMM! ONLY RunIISummer20 IS AVAILABLE!!!!  
#WZZ    = Sample.nanoAODfromDAS("WZZ",    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/schoef-crab_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1_legacy_nano_v3-f82d502d908e8d321edd6873d261cf31/USER", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=0.05565)#LOR COMM! IT IS NOT AVAILABLE!!!!!!! 
ZZZ    = Sample.nanoAODfromDAS("ZZZ",    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=0.01398) #LOR COMM! ONLY RunIISummer20 IS AVAILABLE!!!!  




boson = [
    #WWToLNuQQ,
    #WWTo1L1Nu2Q,
    #ZZTo2L2Q,
    #WZTo1L3Nu,
    #WZTo1L1Nu2Q,
    #WZTo2L2Q,
    #WZTo3LNu,
    #VVTo2L2Nu,
    WWW_4F,
    WWZ_4F,
    #WZZ,
    ZZZ,
]

allSamples = DY + top + boson

for s in allSamples:
    s.isData = False

from nanoMET.tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
