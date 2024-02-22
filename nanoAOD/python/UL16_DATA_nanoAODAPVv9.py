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
dbFile = dbDir+'/DB_UL16_DATA_nanoAODAPVv9.sql'

logger.info("Using db file: %s", dbFile)


# Double Muon
DoubleMuon_Run2016Bver1_preVFP  = Sample.nanoAODfromDAS("DoubleMuon_Run2016Bver1_preVFP", "/DoubleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016Bver2_preVFP  = Sample.nanoAODfromDAS("DoubleMuon_Run2016Bver2_preVFP", "/DoubleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016C_preVFP      = Sample.nanoAODfromDAS("DoubleMuon_Run2016C_preVFP",     "/DoubleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016D_preVFP      = Sample.nanoAODfromDAS("DoubleMuon_Run2016D_preVFP",     "/DoubleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016E_preVFP      = Sample.nanoAODfromDAS("DoubleMuon_Run2016E_preVFP",     "/DoubleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016F_preVFP      = Sample.nanoAODfromDAS("DoubleMuon_Run2016F_preVFP",     "/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016_preVFP = [DoubleMuon_Run2016Bver1_preVFP, DoubleMuon_Run2016Bver2_preVFP, DoubleMuon_Run2016C_preVFP, DoubleMuon_Run2016D_preVFP, DoubleMuon_Run2016E_preVFP, DoubleMuon_Run2016F_preVFP]


allSamples = DoubleMuon_Run2016_preVFP 

for s in allSamples:
    s.isData = True
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt")

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
