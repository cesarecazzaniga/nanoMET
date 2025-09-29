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
dbFile = dbDir+'/DB_UL16_DATA_nanoAODAPVv9_preVPF.sql'

logger.info("Using db file: %s", dbFile)


################################################################################
# Single Muon
SingleMuon_Run2016Bver1_preVFP  = Sample.nanoAODfromDAS("SingleMuon_Run2016Bver1_preVFP", "/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016Bver2_preVFP  = Sample.nanoAODfromDAS("SingleMuon_Run2016Bver2_preVFP", "/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016C_preVFP      = Sample.nanoAODfromDAS("SingleMuon_Run2016C_preVFP",     "/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016D_preVFP      = Sample.nanoAODfromDAS("SingleMuon_Run2016D_preVFP",     "/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016E_preVFP      = Sample.nanoAODfromDAS("SingleMuon_Run2016E_preVFP",     "/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016F_preVFP      = Sample.nanoAODfromDAS("SingleMuon_Run2016F_preVFP",     "/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016_preVFP = [SingleMuon_Run2016Bver1_preVFP, SingleMuon_Run2016Bver2_preVFP, SingleMuon_Run2016C_preVFP, SingleMuon_Run2016D_preVFP, SingleMuon_Run2016E_preVFP, SingleMuon_Run2016F_preVFP]

################################################################################
# SingleElectron
SingleElectron_Run2016Bver1_preVFP  = Sample.nanoAODfromDAS("SingleElectron_Run2016Bver1_preVFP", "/SingleElectron/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016Bver2_preVFP  = Sample.nanoAODfromDAS("SingleElectron_Run2016Bver2_preVFP", "/SingleElectron/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016C_preVFP      = Sample.nanoAODfromDAS("SingleElectron_Run2016C_preVFP",     "/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016D_preVFP      = Sample.nanoAODfromDAS("SingleElectron_Run2016D_preVFP",     "/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016E_preVFP      = Sample.nanoAODfromDAS("SingleElectron_Run2016E_preVFP",     "/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016F_preVFP      = Sample.nanoAODfromDAS("SingleElectron_Run2016F_preVFP",     "/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016_preVFP = [SingleElectron_Run2016Bver1_preVFP, SingleElectron_Run2016Bver2_preVFP, SingleElectron_Run2016C_preVFP, SingleElectron_Run2016D_preVFP, SingleElectron_Run2016E_preVFP, SingleElectron_Run2016F_preVFP]

################################################################################
# Double Muon
DoubleMuon_Run2016Bver1_preVFP  = Sample.nanoAODfromDAS("DoubleMuon_Run2016Bver1_preVFP", "/DoubleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016Bver2_preVFP  = Sample.nanoAODfromDAS("DoubleMuon_Run2016Bver2_preVFP", "/DoubleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016C_preVFP      = Sample.nanoAODfromDAS("DoubleMuon_Run2016C_preVFP",     "/DoubleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016D_preVFP      = Sample.nanoAODfromDAS("DoubleMuon_Run2016D_preVFP",     "/DoubleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016E_preVFP      = Sample.nanoAODfromDAS("DoubleMuon_Run2016E_preVFP",     "/DoubleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016F_preVFP      = Sample.nanoAODfromDAS("DoubleMuon_Run2016F_preVFP",     "/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016_preVFP = [DoubleMuon_Run2016Bver1_preVFP, DoubleMuon_Run2016Bver2_preVFP, DoubleMuon_Run2016C_preVFP, DoubleMuon_Run2016D_preVFP, DoubleMuon_Run2016E_preVFP, DoubleMuon_Run2016F_preVFP]

################################################################################
# Double EG
DoubleEG_Run2016Bver1_preVFP  = Sample.nanoAODfromDAS("DoubleEG_Run2016Bver1_preVFP", "/DoubleEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016Bver2_preVFP  = Sample.nanoAODfromDAS("DoubleEG_Run2016Bver2_preVFP", "/DoubleEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v3/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016C_preVFP      = Sample.nanoAODfromDAS("DoubleEG_Run2016C_preVFP",     "/DoubleEG/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016D_preVFP      = Sample.nanoAODfromDAS("DoubleEG_Run2016D_preVFP",     "/DoubleEG/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016E_preVFP      = Sample.nanoAODfromDAS("DoubleEG_Run2016E_preVFP",     "/DoubleEG/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016F_preVFP      = Sample.nanoAODfromDAS("DoubleEG_Run2016F_preVFP",     "/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016_preVFP = [DoubleEG_Run2016Bver1_preVFP, DoubleEG_Run2016Bver2_preVFP, DoubleEG_Run2016C_preVFP, DoubleEG_Run2016D_preVFP, DoubleEG_Run2016E_preVFP, DoubleEG_Run2016F_preVFP]

################################################################################
# MuonEG
MuonEG_Run2016Bver1_preVFP  = Sample.nanoAODfromDAS("MuonEG_Run2016Bver1_preVFP", "/MuonEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016Bver2_preVFP  = Sample.nanoAODfromDAS("MuonEG_Run2016Bver2_preVFP", "/MuonEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016C_preVFP      = Sample.nanoAODfromDAS("MuonEG_Run2016C_preVFP",     "/MuonEG/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016D_preVFP      = Sample.nanoAODfromDAS("MuonEG_Run2016D_preVFP",     "/MuonEG/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016E_preVFP      = Sample.nanoAODfromDAS("MuonEG_Run2016E_preVFP",     "/MuonEG/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016F_preVFP      = Sample.nanoAODfromDAS("MuonEG_Run2016F_preVFP",     "/MuonEG/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016_preVFP = [MuonEG_Run2016Bver1_preVFP, MuonEG_Run2016Bver2_preVFP, MuonEG_Run2016C_preVFP, MuonEG_Run2016D_preVFP, MuonEG_Run2016E_preVFP, MuonEG_Run2016F_preVFP]

################################################################################

allSamples = SingleMuon_Run2016_preVFP + SingleElectron_Run2016_preVFP + DoubleMuon_Run2016_preVFP + DoubleEG_Run2016_preVFP + MuonEG_Run2016_preVFP

for s in allSamples:
    s.isData = True
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt")


from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
