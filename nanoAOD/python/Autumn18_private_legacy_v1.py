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
dbFile = dbDir+"/samples/DB_Autumn18_private_legacy.sql"

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_LO        = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO",       "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=False, xSection=2075.14*3)

DY = [
    DYJetsToLL_M50_LO,
]

## ttbar
TTLep_pow       = Sample.nanoAODfromDAS("TTLep_pow",       "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762*((3*0.108)**2))

## single top
TToLeptons_sch_amcatnlo = Sample.nanoAODfromDAS("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v4_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=(7.20+4.16)*0.108*3)
T_tch_pow           = Sample.nanoAODfromDAS("T_tch_pow",        "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=136.02) # inclusive sample
TBar_tch_pow        = Sample.nanoAODfromDAS("TBar_tch_pow",     "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=80.95) # inclusive sample
T_tWch              = Sample.nanoAODfromDAS("T_tWch",           "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.85*(1-(1-3*0.108)**2))
TBar_tWch           = Sample.nanoAODfromDAS("TBar_tWch",        "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.85*(1-(1-3*0.108)**2))

top = [
    TTLep_pow,
    TToLeptons_sch_amcatnlo,
    T_tch_pow,
    TBar_tch_pow,
    T_tWch,
    TBar_tWch,
]

## di/multiboson
WWToLNuQQ           = Sample.nanoAODfromDAS("WWToLNuQQ",        "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=49.997)

ZZTo2L2Q            = Sample.nanoAODfromDAS("ZZTo2L2Q",             "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.28)

WZTo1L3Nu           = Sample.nanoAODfromDAS("WZTo1L3Nu"  ,          "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",          dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=(47.13)*(3*0.108)*(0.2) )
WZTo2L2Q            = Sample.nanoAODfromDAS("WZTo2L2Q"   ,          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.60)
WZTo3LNu_ext        = Sample.nanoAODfromDAS("WZTo3LNu_ext",         "/WZTo3LNu_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.42965)

VVTo2L2Nu           = Sample.nanoAODfromDAS("VVTo2L2Nu",            "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=14.00)

WGToLNuG                = Sample.nanoAODfromDAS("WGToLNuG", "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=463.9*1.295) # NLO xsec from TOP-17-016 for 2016 -> extract k-factor (compare with xsec analyzer for 2016) and apply k-factor to other years (xsec= analyser * k)
WGToLNuG_amcatnlo_ext1  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext1", "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=203.3)

WWW_4F              = Sample.nanoAODfromDAS("WWW_4F",               "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",            dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2086)
WWZ                 = Sample.nanoAODfromDAS("WWZ",                  "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1651)
WZZ                 = Sample.nanoAODfromDAS("WZZ",                  "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.05565)
ZZZ                 = Sample.nanoAODfromDAS("ZZZ",                  "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER ",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01398)

boson = [
    WWToLNuQQ,
    ZZTo2L2Q,
    WZTo1L3Nu,
    WZTo2L2Q,
    WZTo3LNu_ext,
    VVTo2L2Nu,
    WWW_4F,
    WWZ,
    WZZ,
    ZZZ,
    ]

allSamples = DY + top + boson

for s in allSamples:
    s.isData = False

from nanoMET.tools.AutoClass import AutoClass
samples = AutoClass( allSamples )

