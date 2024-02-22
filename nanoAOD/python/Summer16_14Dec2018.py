import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
    return argParser

# Logging                                                                                                                                                                        
if __name__=="__main__":
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
dbFile = dbDir+"/DB_Summer16_14Dec2018.sql"

logger.info("Using db file: %s", dbFile)

## DY
# NOTE: x-check xsecs (https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z)

DYJetsToLL_M50_LO_ext1   = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO_ext1", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=2075.14*3)
DYJetsToLL_M50_LO_ext2   = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO_ext2", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=2075.14*3)
DYJetsToLL_M50_ext2      = Sample.nanoAODfromDAS("DYJetsToLL_M50_ext2",    "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=2075.14*3)

DYJetsToLL_M10to50_LO    = Sample.nanoAODfromDAS("DYJetsToLL_M10to50_LO",  "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=18610)
DYJetsToLL_M10to50       = Sample.nanoAODfromDAS("DYJetsToLL_M10to50",     "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=18610)
DYJetsToLL_M10to50_ext   = Sample.nanoAODfromDAS("DYJetsToLL_M10to50_ext", "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=18610)

DY = [
    DYJetsToLL_M50_LO_ext1,
    DYJetsToLL_M50_LO_ext2,
    DYJetsToLL_M50_ext2,
    DYJetsToLL_M10to50,     # added
    DYJetsToLL_M10to50_ext, # added
    DYJetsToLL_M10to50_LO,
    ]

# DY HT bins, M_{ll} [50, inf]
#DYJetsToLL_M50_HT70to100      = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT70to100",      "/DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=169.9*1.23)
#DYJetsToLL_M50_HT100to200     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT100to200",     "/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=147.4*1.23)
#DYJetsToLL_M50_HT100to200_ext = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT100to200_ext", "/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=147.4*1.23)
#DYJetsToLL_M50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400",     "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=40.99*1.23)
#DYJetsToLL_M50_HT200to400_ext = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400_ext", "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=40.99*1.23)
#DYJetsToLL_M50_HT400to600     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600",     "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=5.678*1.23)
#DYJetsToLL_M50_HT400to600_ext = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600_ext", "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=5.678*1.23)
#DYJetsToLL_M50_HT600to800     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT600to800",     "/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.367*1.23)
#DYJetsToLL_M50_HT800to1200    = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT800to1200",    "/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.6304*1.23)
#DYJetsToLL_M50_HT1200to2500   = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT1200to2500",   "/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.1514*1.23)
#DYJetsToLL_M50_HT2500toInf    = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT2500toInf",    "/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.003565*1.23)
'''
DYJetsM50HT = [
    DYJetsToLL_M50_HT70to100,
    DYJetsToLL_M50_HT100to200,
    DYJetsToLL_M50_HT100to200_ext,
    DYJetsToLL_M50_HT200to400,
    DYJetsToLL_M50_HT200to400_ext,
    DYJetsToLL_M50_HT400to600,
    DYJetsToLL_M50_HT400to600_ext,
    DYJetsToLL_M50_HT600to800,
    DYJetsToLL_M50_HT800to1200,
    DYJetsToLL_M50_HT1200to2500,
    DYJetsToLL_M50_HT2500toInf,
    ]

# DY HT bins, M_{ll} [5, 50]
DYJetsToLL_M5to50_HT70to100      = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT70to100",      "/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=303.4) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT100to200     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT100to200",     "/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=224.2) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT100to200_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT100to200_ext", "/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=224.2) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT200to400",     "/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=37.2) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT200to400_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT200to400_ext", "/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=37.2) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT400to600     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT400to600",     "/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3.581) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT400to600_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT400to600_ext", "/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3.581) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT600toInf     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT600toInf",     "/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.124) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT600toInf_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT600toInf_ext", "/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.124) #LO without 1.23 k-factor

DYJetsM5to50HT = [
    DYJetsToLL_M5to50_HT70to100,
    DYJetsToLL_M5to50_HT100to200,
    DYJetsToLL_M5to50_HT100to200_ext,
    DYJetsToLL_M5to50_HT200to400,
    DYJetsToLL_M5to50_HT200to400_ext,
    DYJetsToLL_M5to50_HT400to600,
    DYJetsToLL_M5to50_HT400to600_ext,
    DYJetsToLL_M5to50_HT600toInf,
    DYJetsToLL_M5to50_HT600toInf_ext
    ]

DY += DYJetsM50HT + DYJetsM5to50HT
'''
### TTbar
TTbar        = Sample.nanoAODfromDAS("TTbar",        "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",                  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=831.762)
#TTbar_backup = Sample.nanoAODfromDAS("TTbar_backup", "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_backup_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",           dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=831.762) # NOTE: needed?
TTLep_pow    = Sample.nanoAODfromDAS("TTLep_pow",    "/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=831.762*((3*0.108)**2))

## TTbar+jets
TTJets_amcatnlo   = Sample.nanoAODfromDAS("TTJets_amcatnlo",   "/TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",          dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=831.762)

# leptonic
TTJets_DiLept     = Sample.nanoAODfromDAS("TTJets_DiLept",     "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=87.31483776) # NOTE: genMET-150 version exists
TTJets_DiLept_ext = Sample.nanoAODfromDAS("TTJets_DiLept_ext", "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=87.31483776)

TTJets_SingleLeptonFromT        = Sample.nanoAODfromDAS("TTJets_SingleLeptonFromT",        "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=182.17540224) # NOTE: genMET-150 version exists
TTJets_SingleLeptonFromT_ext    = Sample.nanoAODfromDAS("TTJets_SingleLeptonFromT_ext",    "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=182.17540224)
TTJets_SingleLeptonFromTbar     = Sample.nanoAODfromDAS("TTJets_SingleLeptonFromTbar",     "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=182.17540224) # NOTE: genMET-150 version exists
TTJets_SingleLeptonFromTbar_ext = Sample.nanoAODfromDAS("TTJets_SingleLeptonFromTbar_ext", "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=182.17540224)

TTJets = [
    TTJets_amcatnlo,
    TTJets_DiLept,
    TTJets_DiLept_ext,
    TTJets_SingleLeptonFromT,
    TTJets_SingleLeptonFromT_ext, # added
    TTJets_SingleLeptonFromTbar,
    TTJets_SingleLeptonFromTbar_ext,
    ]

### Single Top
# NOTE: x-check xsecs (https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma)
TToLeptons_sch_amcatnlo = Sample.nanoAODfromDAS("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",            dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=(7.20+4.16)*0.108*3)

T_tch_powheg            = Sample.nanoAODfromDAS("T_tch_powheg",    "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",     dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=136.02) # inclusive sample
TBar_tch_powheg         = Sample.nanoAODfromDAS("TBar_tch_powheg", "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=80.95) # inclusive sample

#T_tWch                  = Sample.nanoAODfromDAS("T_tWch",         "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",                 dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=35.85) # NOTE: NNLO xsec from twiki # NOTE: different tune - can combine with ext?
T_tWch_ext              = Sample.nanoAODfromDAS("T_tWch_ext",      "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",                 dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=35.85) # NOTE: NNLO xsec from twiki
#TBar_tWch               = Sample.nanoAODfromDAS("TBar_tWch",       "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",             dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=35.85) # NOTE: NNLO xsec from twiki # NOTE: different tune - can combine with ext?
TBar_tWch_ext           = Sample.nanoAODfromDAS("TBar_tWch_ext",   "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",             dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=35.85) # NOTE: NNLO xsec from twiki

## ttH
TTHbb_pow               = Sample.nanoAODfromDAS("TTHbb_pow",              "/ttHTobb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.5085*(0.577))
#TTHbb_pow               = Sample.nanoAODfromDAS("TTHbb_pow",              "/ttHTobb_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",                          dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.5085*(0.577))
#TTHbb_pow               = Sample.nanoAODfromDAS("TTHbb_pow",              "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",                  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.5085*(0.577))
#TTHbb                   = Sample.nanoAODfromDAS("TTHbb",                  "/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext3-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.5085*(0.577)) # NOTE: TTHJetTobb missing
TTHnobb_pow             = Sample.nanoAODfromDAS("TTHnobb_pow",            "/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.5085*(1-0.577))
#TTHnobb                 = Sample.nanoAODfromDAS("TTHnobb",                "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.5085*(1-0.577))
#TTHnobb_mWCutfix_ext    = Sample.nanoAODfromDAS("TTHnobb_mWCutfix_ext",   "/ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_mWCutfix/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector_global, xSection=0.5085*(1-0.577))

THQ = Sample.nanoAODfromDAS("THQ", "/THQ_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.07096)
#THW = Sample.nanoAODfromDAS("THW", "/THW_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.1472)

## ttV & TVV
TTW_LO              = Sample.nanoAODfromDAS("TTW_LO", "/ttWJets_13TeV_madgraphMLM/RunIISummer16NanoAODv4-Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.6105)
TTZ_LO              = Sample.nanoAODfromDAS("TTZ_LO", "/ttZJets_13TeV_madgraphMLM/RunIISummer16NanoAODv4-Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.5297/0.692)
#TTZ_LO              = Sample.nanoAODfromDAS("TTZ_LO", "/ttZJets_13TeV_madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.5297/0.692) # NOTE: difference?

#TGJets              = Sample.nanoAODfromDAS("TGJets",     "/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=2.967)
TGJets_ext          = Sample.nanoAODfromDAS("TGJets_ext", "/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=2.967)
#tZq_ll              = Sample.nanoAODfromDAS("tZq_ll",     "/tZq_ll_4f_13TeV-amcatnlo-herwigpp/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector_global, xSection=0.09418 ) #0.0758 )
tZq_ll_ext          = Sample.nanoAODfromDAS("tZq_ll_ext", "/tZq_ll_4f_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.09418 ) #0.0758 )
tWll                = Sample.nanoAODfromDAS("tWll",       "/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.01123)
tWnunu              = Sample.nanoAODfromDAS("tWnunu",     "/ST_tWnunu_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.01123*1.9822 )

TTWToLNu_ext        = Sample.nanoAODfromDAS("TTWToLNu_ext",  "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.2043)
TTWToLNu_ext2       = Sample.nanoAODfromDAS("TTWToLNu_ext2", "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.2043)
#TTWToQQ             = Sample.nanoAODfromDAS("TTWToQQ", "/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.40620)

TTZToQQ             = Sample.nanoAODfromDAS("TTZToQQ", "/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.5297)
TTZToLLNuNu_ext1    = Sample.nanoAODfromDAS("TTZToLLNuNu_ext1", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.2728)
TTZToLLNuNu_ext2    = Sample.nanoAODfromDAS("TTZToLLNuNu_ext2", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.2728)
TTZToLLNuNu_ext3    = Sample.nanoAODfromDAS("TTZToLLNuNu_ext3", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext3-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.2728)
#TTZToLLNuNu_m1to10  = Sample.nanoAODfromDAS("TTZToLLNuNu_m1to10", "/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.0493)
TTGJets             = Sample.nanoAODfromDAS("TTGJets",    "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3.697)
TTGJets_ext         = Sample.nanoAODfromDAS("TTGJets_ext", "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v2/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3.697)

#TTGHad              = Sample.nanoAODfromDAS("TTGHad",      "/TTGamma_Hadronic_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.794*3.062342569) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)
#TTGSemiTbar         = Sample.nanoAODfromDAS("TTGSemiTbar", "/TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.769*2.028673602) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)
#TTGSemiT            = Sample.nanoAODfromDAS("TTGSemiT",    "/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.769*2.028673602) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)
#TTGLep              = Sample.nanoAODfromDAS("TTGLep",      "/TTGamma_Dilept_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.607*1.574299835) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)
'''
TTV_LO = [
    TTW_LO,
    TTZ_LO,
    ]

TTV = [
#    TGJets,
    TGJets_ext,
#    TTGHad,
#    TTGSemiT,
#    TTGSemiTbar,
    TTGLep,
    tZq_ll_ext,
    tWll,
    tWnunu,
    TTWToLNu_ext,
    TTWToLNu_ext2,
#    TTWToQQ,
    TTZToQQ,
    TTZToLLNuNu_ext1,
    TTZToLLNuNu_ext2,
    TTZToLLNuNu_ext3,
#    TTZToLLNuNu_m1to10,
    TTGJets,
    TTGJets_ext
    ] + TTV_LO

ST = [
    TToLeptons_sch_amcatnlo,
    T_tch_powheg,
    TBar_tch_powheg,
#    T_tWch, # added
    T_tWch_ext,
#    TBar_tWch, # added
    TBar_tWch_ext,
    ]
'''
top = [
    TTbar,
    TTLep_pow,
#    TTHbb_pow, # added
    #TTHbb,
#    TTHnobb, # added
#    TTHnobb_pow,
#    TTHnobb_mWCutfix_ext,
#    THQ,
#    THW,
    ] + TTJets


### di/multiboson
# NOTE: x-check xsec (https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Diboson)

WWTo2L2Nu     = Sample.nanoAODfromDAS("WWTo2L2Nu",     "/WWTo2L2Nu_13TeV-powheg/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",                         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=12.178) # NOTE: NNLO x-sec from twiki
WWToLNuQQ     = Sample.nanoAODfromDAS("WWToLNuQQ",     "/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",                         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=49.997) # NOTE: NNLO x-sec from twiki
WWToLNuQQ_ext = Sample.nanoAODfromDAS("WWToLNuQQ_ext", "/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",                    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=49.997) # NOTE: NNLO x-sec from twiki
WWTo1L1Nu2Q   = Sample.nanoAODfromDAS("WWTo1L1Nu2Q",   "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=49.997)

WZTo1L3Nu         = Sample.nanoAODfromDAS("WZTo1L3Nu",    "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=(47.13)*(3*0.108)*(0.2))
WZTo1L1Nu2Q       = Sample.nanoAODfromDAS("WZTo1L1Nu2Q",  "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=10.71)
WZTo2L2Q          = Sample.nanoAODfromDAS("WZTo2L2Q",     "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",     dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=5.60)
WZTo3LNu          = Sample.nanoAODfromDAS("WZTo3LNu",     "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=4.42965)
WZTo3LNu_ext      = Sample.nanoAODfromDAS("WZTo3LNu_ext", "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=4.42965)

WZTo3LNu_mllmin01     = Sample.nanoAODfromDAS("WZTo3LNu_mllmin01",     "/WZTo3LNu_mllmin01_13TeV-powheg-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",           dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=58.59)
WZTo3LNu_mllmin01_ext = Sample.nanoAODfromDAS("WZTo3LNu_mllmin01_ext", "/WZTo3LNu_mllmin01_13TeV-powheg-pythia8_ext1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=58.59)
WZTo3LNu_amcatnlo     = Sample.nanoAODfromDAS("WZTo3LNu_amcatnlo",     "/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=4.666)

#WZJToLLLNu = Sample.nanoAODfromDAS("WZJToLLLNu", "/WZJToLLLNu_TuneCUETP8M1_13TeV-amcnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=4.708)

ZZTo2L2Nu      = Sample.nanoAODfromDAS("ZZTo2L2Nu",      "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",               dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.564)
ZZTo2L2Nu_ext  = Sample.nanoAODfromDAS("ZZTo2L2Nu_ext",  "/ZZTo2L2Nu_13TeV_powheg_pythia8_ext1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",          dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.564)
ZZTo2L2Q       = Sample.nanoAODfromDAS("ZZTo2L2Q",       "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3.28)
#ZZTo2L2Q_pow   = Sample.nanoAODfromDAS("ZZTo2L2Q_pow",   "/ZZTo2L2Q_13TeV_powheg_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",                dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3.28)
ZZTo2Q2Nu      = Sample.nanoAODfromDAS("ZZTo2Q2Nu",      "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=4.04)
ZZTo2Q2Nu_pow  = Sample.nanoAODfromDAS("ZZTo2Q2Nu_pow",  "/ZZTo2Q2Nu_13TeV_powheg_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",               dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=4.04)
ZZTo4L         = Sample.nanoAODfromDAS("ZZTo4L",         "/ZZTo4L_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.256*1.1)
ZZTo4L_pow     = Sample.nanoAODfromDAS("ZZTo4L_pow",     "/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",                  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.256*1.1)
ZZTo4L_pow_ext = Sample.nanoAODfromDAS("ZZTo4L_pow_ext", "/ZZTo4L_13TeV_powheg_pythia8_ext1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",             dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.256*1.1)

VVTo2L2Nu     = Sample.nanoAODfromDAS("VVTo2L2Nu",     "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=11.95)
VVTo2L2Nu_ext = Sample.nanoAODfromDAS("VVTo2L2Nu_ext", "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=11.95)

#WGToLNuG                = Sample.nanoAODfromDAS("WGToLNuG",               "/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=557.46) # NLO xsec from TOP-17-016 * NNLO scale factor from Tom Cornelis 489 (NLO) * 1.14
WGToLNuG_amcatnlo_ext1  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext1", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=585.8) # cross section copied from MLM sample above, to be checked
WGToLNuG_amcatnlo_ext2  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext2", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=585.8) # cross section copied from MLM sample above, to be checked
WGToLNuG_amcatnlo_ext3  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext3", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext3-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=585.8) # cross section copied from MLM sample above, to be checked

WGJets           = Sample.nanoAODfromDAS("WGJets",       "/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",     dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.6637)
WGJets_40130     = Sample.nanoAODfromDAS("WGJets_40130", "/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.6637)

#ZNuNuGJets       = Sample.nanoAODfromDAS("ZNuNuGJets",       "/ZNuNuGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.1903)
ZNuNuGJets_40130 = Sample.nanoAODfromDAS("ZNuNuGJets_40130", "/ZNuNuGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=2.816)

ZGTo2NuG    = Sample.nanoAODfromDAS("ZGTo2NuG",    "/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v2/NANOAODSIM",     dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=28.05)
ZGTo2LG_ext = Sample.nanoAODfromDAS("ZGTo2LG_ext", "/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=131.3)
#ZGToLLG     = Sample.nanoAODfromDAS("ZGToLLG",     "/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=50.2) # NOTE: missing

WWDoubleTo2L = Sample.nanoAODfromDAS("WWDoubleTo2L", "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",     dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.1729)
WpWpJJ       = Sample.nanoAODfromDAS("WpWpJJ", "/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.03711)

# inclusive
WW      = Sample.nanoAODfromDAS("WW",     "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=63.21*1.82)
WW_ext  = Sample.nanoAODfromDAS("WW_ext", "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=63.21*1.82)
WZ      = Sample.nanoAODfromDAS("WZ",     "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=47.13)
WZ_ext  = Sample.nanoAODfromDAS("WZ_ext", "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=47.13)
ZZ      = Sample.nanoAODfromDAS("ZZ",     "/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=16.523)
ZZ_ext  = Sample.nanoAODfromDAS("ZZ_ext", "/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=16.523)

WWW_4F  = Sample.nanoAODfromDAS("WWW_4F", "/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.2086)
#WWZ     = Sample.nanoAODfromDAS("WWZ",    "/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.1651)
#WZG     = Sample.nanoAODfromDAS("WZG",    "/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.04123)
WZZ     = Sample.nanoAODfromDAS("WZZ",    "/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.05565)
ZZZ     = Sample.nanoAODfromDAS("ZZZ",    "/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.01398)

VV_NLO = [
    WWTo2L2Nu,
    WWToLNuQQ,
    WWToLNuQQ_ext,
    WWTo1L1Nu2Q,

    WZTo1L3Nu,
    WZTo1L1Nu2Q,
    WZTo2L2Q,
    WZTo3LNu,
    WZTo3LNu_ext,
    
    ZZTo2L2Nu,
    ZZTo2L2Nu_ext, # added
    ZZTo2L2Q,
    ZZTo2Q2Nu,
    ZZTo2Q2Nu_pow, # added
    ZZTo4L,
    ZZTo4L_pow, # added
    ZZTo4L_pow_ext, # added
    ]


boson = [
    WZTo3LNu_mllmin01, # added
    WZTo3LNu_mllmin01_ext, # added
    WZTo3LNu_amcatnlo,
#    WZJToLLLNu,
    VVTo2L2Nu,
    VVTo2L2Nu_ext,
#    WGToLNuG,
    WGToLNuG_amcatnlo_ext1,
    WGToLNuG_amcatnlo_ext2, # added
    WGToLNuG_amcatnlo_ext3,
    WGJets_40130, # added
    WGJets,
    ZNuNuGJets_40130,
    ZGTo2NuG,
    ZGTo2LG_ext,
#    ZGToLLG, # missing
    WWDoubleTo2L,
    WpWpJJ,
    WW,WW_ext,
    WZ,WZ_ext,
    ZZ,ZZ_ext,
    WWW_4F,
#    WWZ,
#    WZG,
    WZZ,
    ZZZ,
    ] + VV_NLO

### W+jets

## inclusive
# LO
WJetsToLNu     = Sample.nanoAODfromDAS("WJetsToLNu",     "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3*20508.9)
WJetsToLNu_ext = Sample.nanoAODfromDAS("WJetsToLNu_ext", "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3*20508.9)

# NLO
WJetsToLNu_amcatnlo      = Sample.nanoAODfromDAS("WJetsToLNu_amcatnlo",     "/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3* 20508.9)
WJetsToLNu_amcatnlo_ext  = Sample.nanoAODfromDAS("WJetsToLNu_amcatnlo_ext", "/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3* 20508.9)

wjets_inc = [
    WJetsToLNu,
    WJetsToLNu_ext,
    WJetsToLNu_amcatnlo,
    WJetsToLNu_amcatnlo_ext,
    ]

'''
## HT-binned
WJetsToLNu_HT70to100        = Sample.nanoAODfromDAS("WJetsToLNu_HT70to100",        "/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1637.13)
WJetsToLNu_HT100to200       = Sample.nanoAODfromDAS("WJetsToLNu_HT100to200",       "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1627.45)
WJetsToLNu_HT100to200_ext   = Sample.nanoAODfromDAS("WJetsToLNu_HT100to200_ext",   "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1627.45)
WJetsToLNu_HT100to200_ext2  = Sample.nanoAODfromDAS("WJetsToLNu_HT100to200_ext2",  "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1627.45)
WJetsToLNu_HT200to400       = Sample.nanoAODfromDAS("WJetsToLNu_HT200to400",       "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=435.237)
WJetsToLNu_HT200to400_ext   = Sample.nanoAODfromDAS("WJetsToLNu_HT200to400_ext",   "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=435.237)
WJetsToLNu_HT200to400_ext2  = Sample.nanoAODfromDAS("WJetsToLNu_HT200to400_ext2",  "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=435.237)
WJetsToLNu_HT400to600       = Sample.nanoAODfromDAS("WJetsToLNu_HT400to600",       "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=59.1811)
WJetsToLNu_HT400to600_ext   = Sample.nanoAODfromDAS("WJetsToLNu_HT400to600_ext",   "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=59.1811)
WJetsToLNu_HT600to800       = Sample.nanoAODfromDAS("WJetsToLNu_HT600to800",       "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=14.5805)
WJetsToLNu_HT600to800_ext   = Sample.nanoAODfromDAS("WJetsToLNu_HT600to800_ext",   "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=14.5805)
WJetsToLNu_HT800to1200      = Sample.nanoAODfromDAS("WJetsToLNu_HT800to1200",      "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=6.65621)
WJetsToLNu_HT800to1200_ext  = Sample.nanoAODfromDAS("WJetsToLNu_HT800to1200_ext",  "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=6.65621)
WJetsToLNu_HT1200to2500     = Sample.nanoAODfromDAS("WJetsToLNu_HT1200to2500",     "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.60809)
WJetsToLNu_HT1200to2500_ext = Sample.nanoAODfromDAS("WJetsToLNu_HT1200to2500_ext", "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.60809)
WJetsToLNu_HT2500toInf      = Sample.nanoAODfromDAS("WJetsToLNu_HT2500toInf",      "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.0389136)
WJetsToLNu_HT2500toInf_ext  = Sample.nanoAODfromDAS("WJetsToLNu_HT2500toInf_ext",  "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.0389136)

wjets_ht = [
    WJetsToLNu_HT70to100,
    WJetsToLNu_HT100to200,
    WJetsToLNu_HT100to200_ext,
    WJetsToLNu_HT100to200_ext2,
    WJetsToLNu_HT200to400,
    WJetsToLNu_HT200to400_ext,
    WJetsToLNu_HT200to400_ext2,
    WJetsToLNu_HT400to600,
    WJetsToLNu_HT400to600_ext,
    WJetsToLNu_HT600to800,
    WJetsToLNu_HT600to800_ext,
    WJetsToLNu_HT800to1200,
    WJetsToLNu_HT800to1200_ext,
    WJetsToLNu_HT1200to2500,
    WJetsToLNu_HT1200to2500_ext,
    WJetsToLNu_HT2500toInf,
    WJetsToLNu_HT2500toInf_ext,
    ]

## pt-binned #NOTE: for now unused
#WJetsToLNu_Pt100to250      = Sample.nanoAODfromDAS("WJetsToLNu_Pt100to250",      "/WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=626.3)
#WJetsToLNu_Pt100to250_ext  = Sample.nanoAODfromDAS("WJetsToLNu_Pt100to250_ext",  "/WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=626.3)
#WJetsToLNu_Pt100to250_ext4 = Sample.nanoAODfromDAS("WJetsToLNu_Pt100to250_ext4", "/WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext4-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=626.3)
#WJetsToLNu_Pt250to400      = Sample.nanoAODfromDAS("WJetsToLNu_Pt250to400",      "/WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v2/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=21.82)
#WJetsToLNu_Pt250to400_ext  = Sample.nanoAODfromDAS("WJetsToLNu_Pt250to400_ext",  "/WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=21.82)
#WJetsToLNu_Pt250to400_ext4 = Sample.nanoAODfromDAS("WJetsToLNu_Pt250to400_ext4", "/WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext4-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=21.82)
#WJetsToLNu_Pt400to600      = Sample.nanoAODfromDAS("WJetsToLNu_Pt400to600",      "/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v2/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=2.68)
#WJetsToLNu_Pt400to600_ext  = Sample.nanoAODfromDAS("WJetsToLNu_Pt400to600_ext",  "/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v2/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=2.68)
#WJetsToLNu_Pt600toInf      = Sample.nanoAODfromDAS("WJetsToLNu_Pt600toInf",      "/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v2/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.4109)
#WJetsToLNu_Pt600toInf_ext  = Sample.nanoAODfromDAS("WJetsToLNu_Pt600toInf_ext",  "/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v2/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.4109)
#
#wjets_pt = [
#    WJetsToLNu_Pt100to250,
#    WJetsToLNu_Pt100to250_ext,
#    WJetsToLNu_Pt100to250_ext4, # added
#    WJetsToLNu_Pt250to400, 
#    WJetsToLNu_Pt250to400_ext,
#    WJetsToLNu_Pt250to400_ext4, # added
#    WJetsToLNu_Pt400to600,
#    WJetsToLNu_Pt400to600_ext,
#    WJetsToLNu_Pt600toInf,
#    WJetsToLNu_Pt600toInf_ext,
#    ]

wjets = wjets_inc + wjets_ht #+ wjets_pt
'''
## rare
TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.009103)
#TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.009103)
#TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCUETP8M2T4_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.009103)
#TTWW = Sample.nanoAODfromDAS("TTWW", "/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", "CMS", ".*root", 0.007829)
#TTWZ = Sample.nanoAODfromDAS("TTWZ", "/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", "CMS", ".*root", 0.002919)
#TTZZ = Sample.nanoAODfromDAS("TTZZ", "/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", "CMS", ".*root", 0.001573)

rare = [
    TTTT,
    ]

'''
GluGluToContinToZZTo2e2mu   = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.005423)
GluGluToContinToZZTo2e2tau  = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.005423)
GluGluToContinToZZTo2e2nu   = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2nu",   "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.005423)
GluGluToContinToZZTo2mu2tau = Sample.nanoAODfromDAS("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.005423)
GluGluToContinToZZTo2mu2nu  = Sample.nanoAODfromDAS("GluGluToContinToZZTo2mu2nu",  "/GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.005423)
GluGluToContinToZZTo4e      = Sample.nanoAODfromDAS("GluGluToContinToZZTo4e",      "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.0027)
GluGluToContinToZZTo4mu     = Sample.nanoAODfromDAS("GluGluToContinToZZTo4mu",     "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",     dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.0027)
GluGluToContinToZZTo4tau    = Sample.nanoAODfromDAS("GluGluToContinToZZTo4tau",    "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.0027)

gluglu = [
    GluGluToContinToZZTo2e2mu,
    GluGluToContinToZZTo2e2tau,
    GluGluToContinToZZTo2e2nu, # added
    GluGluToContinToZZTo2mu2tau,
    GluGluToContinToZZTo2mu2nu, # added
    GluGluToContinToZZTo4e,
    GluGluToContinToZZTo4mu,
    GluGluToContinToZZTo4tau,
    ]

### QCD

## QCD HT bins (cross sections from McM)
QCD_HT50to100        = Sample.nanoAODfromDAS("QCD_HT50to100",        "/QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=246400000.0)
QCD_HT100to200       = Sample.nanoAODfromDAS("QCD_HT100to200",       "/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=27850000.0)
QCD_HT200to300       = Sample.nanoAODfromDAS("QCD_HT200to300",       "/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1717000)
QCD_HT200to300_ext   = Sample.nanoAODfromDAS("QCD_HT200to300_ext",   "/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1717000)
QCD_HT300to500       = Sample.nanoAODfromDAS("QCD_HT300to500",       "/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=351300)
QCD_HT300to500_ext   = Sample.nanoAODfromDAS("QCD_HT300to500_ext",   "/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=351300)
QCD_HT500to700       = Sample.nanoAODfromDAS("QCD_HT500to700",       "/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=31630)
QCD_HT500to700_ext   = Sample.nanoAODfromDAS("QCD_HT500to700_ext",   "/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=31630)
QCD_HT700to1000      = Sample.nanoAODfromDAS("QCD_HT700to1000",      "/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=6802)
QCD_HT700to1000_ext  = Sample.nanoAODfromDAS("QCD_HT700to1000_ext",  "/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=6802)
QCD_HT1000to1500     = Sample.nanoAODfromDAS("QCD_HT1000to1500",     "/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1206)
QCD_HT1000to1500_ext = Sample.nanoAODfromDAS("QCD_HT1000to1500_ext", "/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1206)
QCD_HT1500to2000     = Sample.nanoAODfromDAS("QCD_HT1500to2000",     "/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=120.4)
QCD_HT1500to2000_ext = Sample.nanoAODfromDAS("QCD_HT1500to2000_ext", "/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=120.4)
QCD_HT2000toInf      = Sample.nanoAODfromDAS("QCD_HT2000toInf",      "/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=25.25)
QCD_HT2000toInf_ext  = Sample.nanoAODfromDAS("QCD_HT2000toInf_ext",  "/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=25.25)

QCD = [
    QCD_HT50to100,
    QCD_HT100to200,
    QCD_HT200to300,
    QCD_HT200to300_ext,
    QCD_HT300to500,
    QCD_HT300to500_ext,
    QCD_HT500to700,
    QCD_HT500to700_ext,
    QCD_HT700to1000,
    QCD_HT700to1000_ext,
    QCD_HT1000to1500,
    QCD_HT1000to1500_ext,
    QCD_HT1500to2000,
    QCD_HT1500to2000_ext,
    QCD_HT2000toInf,
    QCD_HT2000toInf_ext,
    ]

### Zinv
# NOTE: x-check xsecs (https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#DY_Z)

ZJetsToNuNu_HT100to200       = Sample.nanoAODfromDAS("ZJetsToNuNu_HT100to200",       "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=344.9781)
ZJetsToNuNu_HT100to200_ext   = Sample.nanoAODfromDAS("ZJetsToNuNu_HT100to200_ext",   "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=344.9781)
ZJetsToNuNu_HT200to400       = Sample.nanoAODfromDAS("ZJetsToNuNu_HT200to400",       "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=96.3828)
ZJetsToNuNu_HT200to400_ext   = Sample.nanoAODfromDAS("ZJetsToNuNu_HT200to400_ext",   "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=96.3828)
ZJetsToNuNu_HT400to600       = Sample.nanoAODfromDAS("ZJetsToNuNu_HT400to600",       "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=13.4562)
ZJetsToNuNu_HT400to600_ext   = Sample.nanoAODfromDAS("ZJetsToNuNu_HT400to600_ext",   "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=13.4562)
ZJetsToNuNu_HT600to800       = Sample.nanoAODfromDAS("ZJetsToNuNu_HT600to800",       "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3.96183)
ZJetsToNuNu_HT800to1200      = Sample.nanoAODfromDAS("ZJetsToNuNu_HT800to1200",      "/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.81302)
ZJetsToNuNu_HT1200to2500     = Sample.nanoAODfromDAS("ZJetsToNuNu_HT1200to2500",     "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.441078)
ZJetsToNuNu_HT1200to2500_ext = Sample.nanoAODfromDAS("ZJetsToNuNu_HT1200to2500_ext", "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.441078)
ZJetsToNuNu_HT2500toInf      = Sample.nanoAODfromDAS("ZJetsToNuNu_HT2500toInf",      "/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.01008969)

Zinv = [
    ZJetsToNuNu_HT100to200,
    ZJetsToNuNu_HT100to200_ext,
    ZJetsToNuNu_HT200to400,
    ZJetsToNuNu_HT200to400_ext,
    ZJetsToNuNu_HT400to600,
    ZJetsToNuNu_HT400to600_ext,
    ZJetsToNuNu_HT600to800,
    ZJetsToNuNu_HT800to1200,
    ZJetsToNuNu_HT1200to2500, # added
    ZJetsToNuNu_HT1200to2500_ext,
    ZJetsToNuNu_HT2500toInf,
    ]

### Signals

# FastSim
T2tt_dM_10to80     = Sample.nanoAODfromDAS("T2tt_dM-10to80",     "/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUSummer16v3Fast_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",     dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)
T2bW_X05_dM_10to80 = Sample.nanoAODfromDAS("T2bW_X05_dM-10to80", "/SMS-T2bW_X05_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUSummer16v3Fast_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)

N2C1_higgsino      = Sample.nanoAODfromDAS("N2C1-higgsino",      "/SMS-N2C1-higgsino_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_GridpackScan_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)
N2N1_higgsino      = Sample.nanoAODfromDAS("N2N1-higgsino",      "/SMS-N2N1-higgsino_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_GridpackScan_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)


# FullSim
T2tt_mStop_850_mLSP_100 = Sample.nanoAODfromDAS("T2tt_mStop_850_mLSP_100", "/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)
#T2tt_mStop_650_mLSP_350 = Sample.nanoAODfromDAS("T2tt_mStop_650_mLSP_350", "/SMS-T2tt_mStop-650_mLSP-350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)
T2tt_mStop_500_mLSP_325 = Sample.nanoAODfromDAS("T2tt_mStop_500_mLSP_325", "/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)
#T2tt_mStop_325_mLSP_150 = Sample.nanoAODfromDAS("T2tt_mStop_325_mLSP_150", "/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)

scans = [
    T2tt_dM_10to80,
    T2bW_X05_dM_10to80,
    N2C1_higgsino,
    N2N1_higgsino,
    ]

signals = [
    T2tt_mStop_850_mLSP_100,
#    T2tt_mStop_650_mLSP_350,
    T2tt_mStop_500_mLSP_325,
#    T2tt_mStop_325_mLSP_150,
    ]

### Other
other = [
    ]
'''
allSamples = DY + top + boson + wjets_inc + rare 

for s in allSamples:
    s.isData = False

from nanoMET.tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
