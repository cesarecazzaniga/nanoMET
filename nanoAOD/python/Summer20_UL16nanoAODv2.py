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
dbFile = dbDir+"/samples/DB_Summer20_UL16nanoAODv2.sql"

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_LO_ext1   = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO_ext1",  "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=2075.14*3) #CZZ: updated (old: 5343.0)

DY = [
    DYJetsToLL_M50_LO_ext1,
]

## ttbar
TTLep_pow  = Sample.nanoAODfromDAS("TTLep_pow",       "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=687.1)  #CZZ: updated

## single top
TToLeptons_sch_amcatnlo = Sample.nanoAODfromDAS("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=3.74) #CZZ: updated
T_tch_pow           = Sample.nanoAODfromDAS("T_tch_pow",        "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=115.3) #CZZ: updated
TBar_tch_pow        = Sample.nanoAODfromDAS("TBar_tch_pow",     "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=69.09) #CZZ: updated
T_tWch_ext          = Sample.nanoAODfromDAS("T_tWch_ext",       "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=34.91) #CZZ: updated
TBar_tWch_ext       = Sample.nanoAODfromDAS("TBar_tWch_ext",    "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=34.97) #CZZ: updated

top = [
    TTLep_pow,
    TToLeptons_sch_amcatnlo,
    T_tch_pow,
    TBar_tch_pow,
    T_tWch_ext,
    TBar_tWch_ext,
]

## di/multiboson
WZTo3LNu        = Sample.nanoAODfromDAS("WZTo3LNu_ext",         "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=5.052)# CZZ: added
WWW_4F              = Sample.nanoAODfromDAS("WWW_4F",               "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",            dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=0.2086) #CZZ: updated
WWZ_4F                 = Sample.nanoAODfromDAS("WWZ_4F",            "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=0.1651)# CZZ: ONLY WWZ_4F RunIISummer20 is present! 
WZZ                 = Sample.nanoAODfromDAS("WZZ",                  "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=0.05565) #CZZ: updated
ZZZ                 = Sample.nanoAODfromDAS("ZZZ",                  "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, instance="global", overwrite=ov, xSection=0.01398) #CZZ: updated

boson = [
    WZTo3LNu,
    WWW_4F,
    WWZ_4F,
    WZZ,
    ZZZ,
    ]

allSamples = DY + top + boson

for s in allSamples:
    s.isData = False

from nanoMET.tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
