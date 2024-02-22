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
from nanoMET.tools.user import redirector_global as redirector


# DB
from nanoMET.tools.user import dbDir
dbFile = dbDir+'/DB_UL18_DATA_nanoAODAPVv9.sql'

logger.info("Using db file: %s", dbFile)

################################################################################
# Single Muon
SingleMuon_Run2018A  = Sample.nanoAODfromDAS("SingleMuon_Run2018A", "/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2018B  = Sample.nanoAODfromDAS("SingleMuon_Run2018B", "/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2018C  = Sample.nanoAODfromDAS("SingleMuon_Run2018C", "/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2018D  = Sample.nanoAODfromDAS("SingleMuon_Run2018D", "/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2018 = [SingleMuon_Run2018A, SingleMuon_Run2018B, SingleMuon_Run2018C, SingleMuon_Run2018D]

################################################################################
# EGamma
EGamma_Run2018A = Sample.nanoAODfromDAS("EGamma_Run2018A", "/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
EGamma_Run2018B = Sample.nanoAODfromDAS("EGamma_Run2018B", "/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
EGamma_Run2018C = Sample.nanoAODfromDAS("EGamma_Run2018C", "/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
EGamma_Run2018D = Sample.nanoAODfromDAS("EGamma_Run2018D", "/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v3/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
EGamma_Run2018 = [EGamma_Run2018A, EGamma_Run2018B, EGamma_Run2018C, EGamma_Run2018D]

################################################################################
# Double Muon
DoubleMuon_Run2018A = Sample.nanoAODfromDAS("DoubleMuon_Run2018A", "/DoubleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2018B = Sample.nanoAODfromDAS("DoubleMuon_Run2018B", "/DoubleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2018C = Sample.nanoAODfromDAS("DoubleMuon_Run2018C", "/DoubleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2018D = Sample.nanoAODfromDAS("DoubleMuon_Run2018D", "/DoubleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2018 = [DoubleMuon_Run2018A, DoubleMuon_Run2018B, DoubleMuon_Run2018C, DoubleMuon_Run2018D]

################################################################################
# MuonEG
MuonEG_Run2018A = Sample.nanoAODfromDAS("MuonEG_Run2018A", "/MuonEG/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2018B = Sample.nanoAODfromDAS("MuonEG_Run2018B", "/MuonEG/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2018C = Sample.nanoAODfromDAS("MuonEG_Run2018C", "/MuonEG/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2018D = Sample.nanoAODfromDAS("MuonEG_Run2018D", "/MuonEG/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2018 = [MuonEG_Run2018A, MuonEG_Run2018B, MuonEG_Run2018C, MuonEG_Run2018D]

################################################################################

allSamples = SingleMuon_Run2018 + EGamma_Run2018 + DoubleMuon_Run2018 + MuonEG_Run2018

for s in allSamples:
    s.isData = True
    s.json = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt")

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
