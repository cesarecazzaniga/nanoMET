import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',          action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',             action='store_true',    help="Update current entry in db?")
    argParser.add_argument('--check_completeness', action='store_true',    help="Check competeness?")
    return argParser
    
# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
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
try:
    redirector = sys.modules['__main__'].redirector
except:
    if "clip" in os.getenv("HOSTNAME").lower():
        if __name__ == "__main__" and not options.check_completeness:
            from Samples.Tools.config import redirector_global as redirector
        else:
            from Samples.Tools.config import redirector_clip as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_Run2018_ULnanoAODv2.sql'
logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2018A_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2018A_UL",        "/DoubleMuon/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2018B_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_UL",        "/DoubleMuon/Run2018B-UL2018_MiniAODv1_NanoAODv2-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2018C_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2018C_UL",        "/DoubleMuon/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2018D_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2018D_UL",        "/DoubleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2018A_UL,
    DoubleMuon_Run2018B_UL,
    DoubleMuon_Run2018C_UL,
    DoubleMuon_Run2018D_UL,

]

# MuonEG
MuonEG_Run2018A_UL       = Sample.nanoAODfromDAS("MuonEG_Run2018A_UL",        "/MuonEG/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2018B_UL       = Sample.nanoAODfromDAS("MuonEG_Run2018B_UL",        "/MuonEG/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2018C_UL       = Sample.nanoAODfromDAS("MuonEG_Run2018C_UL",        "/MuonEG/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2018D_UL       = Sample.nanoAODfromDAS("MuonEG_Run2018D_UL",        "/MuonEG/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

MuonEG = [
    MuonEG_Run2018A_UL,
    MuonEG_Run2018B_UL,
    MuonEG_Run2018C_UL,
    MuonEG_Run2018D_UL,
    
]

## DoubleEG
#DoubleEG_Run2018A_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2018A_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#DoubleEG_Run2018B_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2018B_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#DoubleEG_Run2018C_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2018C_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#DoubleEG_Run2018D_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2018D_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#DoubleEG_Run2018E_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2018E_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#DoubleEG_Run2018F_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2018F_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#
#DoubleEG = [
#    DoubleEG_Run2018A_UL,
#    DoubleEG_Run2018B_UL,
#    DoubleEG_Run2018C_UL,
#    DoubleEG_Run2018D_UL,
#    DoubleEG_Run2018E_UL,
#    DoubleEG_Run2018F_UL,
#
#]

# SingleMuon
SingleMuon_Run2018A_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2018A_UL",        "/SingleMuon/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2018B_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2018B_UL",        "/SingleMuon/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2018C_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2018C_UL",        "/SingleMuon/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2018D_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2018D_UL",        "/SingleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

SingleMuon = [
    SingleMuon_Run2018A_UL,
    SingleMuon_Run2018B_UL,
    SingleMuon_Run2018C_UL,
    SingleMuon_Run2018D_UL,
    
]

## SingleElectron
#SingleElectron_Run2018A_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2018A_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#SingleElectron_Run2018B_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2018B_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#SingleElectron_Run2018C_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2018C_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#SingleElectron_Run2018D_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2018D_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#SingleElectron_Run2018E_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2018E_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#SingleElectron_Run2018F_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2018F_UL",        "", dbFile=dbFile, redirector=redirector, overwrite=ov)
#
#SingleElectron = [
#    SingleElectron_Run2018A_UL,
#    SingleElectron_Run2018B_UL,
#    SingleElectron_Run2018C_UL,
#    SingleElectron_Run2018D_UL,
#    SingleElectron_Run2018E_UL,
#    SingleElectron_Run2018F_UL,
#
#]

# JetHT
JetHT_Run2018A_UL       = Sample.nanoAODfromDAS("JetHT_Run2018A_UL",        "/JetHT/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2018B_UL       = Sample.nanoAODfromDAS("JetHT_Run2018B_UL",        "/JetHT/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2018C_UL       = Sample.nanoAODfromDAS("JetHT_Run2018C_UL",        "/JetHT/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2018D_UL       = Sample.nanoAODfromDAS("JetHT_Run2018D_UL",        "/JetHT/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

JetHT = [
    JetHT_Run2018A_UL,
    JetHT_Run2018B_UL,
    JetHT_Run2018C_UL,
    JetHT_Run2018D_UL,

]

# MET
MET_Run2018A_UL       = Sample.nanoAODfromDAS("MET_Run2018A_UL",        "/MET/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2018B_UL       = Sample.nanoAODfromDAS("MET_Run2018B_UL",        "/MET/Run2018B-UL2018_MiniAODv1_NanoAODv2-v4/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2018C_UL       = Sample.nanoAODfromDAS("MET_Run2018C_UL",        "/MET/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2018D_UL       = Sample.nanoAODfromDAS("MET_Run2018D_UL",        "/MET/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

MET = [
    MET_Run2018A_UL,
    MET_Run2018B_UL,
    MET_Run2018C_UL,
    MET_Run2018D_UL,

]

#allSamples = DoubleMuon + MuonEG + DoubleEG + SingleMuon + SingleElectron + JetHT + MET
allSamples = DoubleMuon + MuonEG + SingleMuon + JetHT + MET

for s in allSamples:
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt")
    s.isData    = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 ) 
