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
dbFile = dbDir+'/DB_UL16_nanoAODv9_postVPF.sql'

logger.info("Using db file: %s", dbFile)

################################################################################
# DY

DYJetsToLL_M10to50       = Sample.nanoAODfromDAS("DYJetsToLL_M10to50_LO",   "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=18610)
DYJetsToLL_M50           = Sample.nanoAODfromDAS("DYJetsToLL_M50",     "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2075.14*3)
DYJetsToLL_M50_NLO       = Sample.nanoAODfromDAS("DYJetsToLL_M50_NLO", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2075.14*3)

# x-secs using runXSecAnalyzer
DYJetsToLL_M50_HT100to200 = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT100to200","/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=147.4*1.23)
DYJetsToLL_M50_HT200to400 = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400","/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=40.99*1.23)
DYJetsToLL_M50_HT400to600 = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600","/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.678*1.23)
DYJetsToLL_M50_HT600to800 = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT600to800","/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.367*1.23)
DYJetsToLL_M50_HT800to1200 = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT800to1200","/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.6304*1.23)
DYJetsToLL_M50_HT1200to2500 = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT1200to2500","/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1514*1.23)
DYJetsToLL_M50_HT2500toInf = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT2500toInf","/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003565*1.23)


DYJetsToLL_M4to50_HT100to200 = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT100to200","/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=204.0)#LO
DYJetsToLL_M4to50_HT200to400 = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT200to400","/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=54.39)#LO
DYJetsToLL_M4to50_HT400to600 = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT400to600","/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.697)#LO
DYJetsToLL_M4to50_HT600toInf = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT600toInf","/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.85)#LO


DY = [
    DYJetsToLL_M10to50,
    DYJetsToLL_M50,
    DYJetsToLL_M50_NLO,
    DYJetsToLL_M50_HT100to200,
    DYJetsToLL_M50_HT200to400,
    DYJetsToLL_M50_HT400to600,
    DYJetsToLL_M50_HT600to800,
    DYJetsToLL_M50_HT800to1200,
    DYJetsToLL_M50_HT1200to2500,
    DYJetsToLL_M50_HT2500toInf,
    DYJetsToLL_M4to50_HT100to200,
    DYJetsToLL_M4to50_HT200to400,
    DYJetsToLL_M4to50_HT400to600,
    DYJetsToLL_M4to50_HT600toInf
    ]




################################################################################
# ttbar

TTLep_pow_CP5       = Sample.nanoAODfromDAS("TTLep_pow_CP5",            "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",             dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*((3*0.108)**2))
#TTSingleLep_pow_CP5 = Sample.nanoAODfromDAS("TTSingleLep_pow_CP5",      "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*(3*0.108)*(1-3*0.108)*2)
TTHad_pow_CP5       = Sample.nanoAODfromDAS("TTHad_pow_CP5",            "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*((1-3*0.108)**2))
TTbb                = Sample.nanoAODfromDAS("TTbb",     "/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.59)

TTJets_fxfx         = Sample.nanoAODfromDAS("TTJets_fxfx", "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762)

TTbar = [
    TTLep_pow_CP5,
    #TTSingleLep_pow_CP5,
    TTHad_pow_CP5,
    TTbb,
    TTJets_fxfx,
]

################################################################################
# TTX

TTHTobb         = Sample.nanoAODfromDAS("TTHTobb",   "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5085*(0.577))
TTHnobb         = Sample.nanoAODfromDAS("TTHnobb",   "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5085*(1-0.577))
# THQ                 = Sample.nanoAODfromDAS("THQ",           "THQ_4f_Hincl_13TeV_madgraph_pythia8",                     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.07096)
# THW                 = Sample.nanoAODfromDAS("THW",           "THW_5f_Hincl_13TeV_madgraph_pythia8",                     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1472)
TTWToLNu            = Sample.nanoAODfromDAS("TTWToLNu",      "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2043)
TTWToQQ             = Sample.nanoAODfromDAS("TTWToQQ",       "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.40620)
TTZToQQ             = Sample.nanoAODfromDAS("TTZToQQ",          "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5297)
TTZToLLNuNu         = Sample.nanoAODfromDAS("TTZToLLNuNu",        "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2728)
TTZToLLNuNu_m1to10  = Sample.nanoAODfromDAS("TTZToLLNuNu_m1to10", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0493)
TTZ_LO              = Sample.nanoAODfromDAS("TTZ_LO",           "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5297/0.692)
TTW_LO              = Sample.nanoAODfromDAS("TTW_LO","/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.4611)

TTX = [
    TTHTobb,
    TTHnobb,
    # THQ,
    # THW,
    TTWToLNu,
    TTWToQQ,
    TTZToQQ,
    TTZToLLNuNu,
    TTZToLLNuNu_m1to10,
    TTZ_LO,
    TTW_LO
]

################################################################################
# single top

T_tch_pow           = Sample.nanoAODfromDAS("T_tch_pow",        "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=136.02) # inclusive sample
TBar_tch_pow        = Sample.nanoAODfromDAS("TBar_tch_pow",     "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=80.95) # inclusive sample
T_tWch              = Sample.nanoAODfromDAS("T_tWch",           "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
TBar_tWch           = Sample.nanoAODfromDAS("TBar_tWch",        "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect

tZq_ll              = Sample.nanoAODfromDAS("tZq_ll",           "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.09418 ) #0.0758 )

tWll_thad_Wlept_DR  = Sample.nanoAODfromDAS("tWll_thad_Wlept_DR",  "/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_thad_Wlept_DS  = Sample.nanoAODfromDAS("tWll_thad_Wlept_DS",  "/TWZToLL_thad_Wlept_5f_DS_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_tlept_Whad_DR  = Sample.nanoAODfromDAS("tWll_tlept_Whad_DR",  "/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_tlept_Whad_DS  = Sample.nanoAODfromDAS("tWll_tlept_Whad_DS",  "/TWZToLL_tlept_Whad_5f_DS_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_tlept_Wlept_DR = Sample.nanoAODfromDAS("tWll_tlept_Wlept_DR", "/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001501 )
tWll_tlept_Wlept_DS = Sample.nanoAODfromDAS("tWll_tlept_Wlept_DS", "/TWZToLL_tlept_Wlept_5f_DS_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001501 )


SingleTop = [
    T_tch_pow,
    TBar_tch_pow,
    T_tWch,
    TBar_tWch,
    tZq_ll,
    tWll_thad_Wlept_DR,
    tWll_thad_Wlept_DS,
    tWll_tlept_Whad_DR,
    tWll_tlept_Whad_DS,
    tWll_tlept_Wlept_DR,
    tWll_tlept_Wlept_DS,
]

################################################################################
# multiboson

# VVTo2L2Nu           = Sample.nanoAODfromDAS("VVTo2L2Nu",            "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/",                  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=14.00)
WW                  = Sample.nanoAODfromDAS("WW",                   "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=63.21 * 1.82)
WZ                  = Sample.nanoAODfromDAS("WZ",                   "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=47.13)
ZZ                  = Sample.nanoAODfromDAS("ZZ",                   "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=16.523)
WWW_4F              = Sample.nanoAODfromDAS("WWW_4F",               "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",            dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2086)
WWZ_4F              = Sample.nanoAODfromDAS("WWZ_4F",               "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1651)
WZZ                 = Sample.nanoAODfromDAS("WZZ",                  "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.05565)
ZZZ                 = Sample.nanoAODfromDAS("ZZZ",                  "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.01398)
WZTo3LNu            = Sample.nanoAODfromDAS("WZTo3LNu",             "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.42965)


WWTo2L2Nu           = Sample.nanoAODfromDAS("WWTo2L2Nu","/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=12.178)
WWDoubleTo2L        = Sample.nanoAODfromDAS("WWDoubleTo2L","/WWTo2L2Nu_TuneCP5_DoubleScattering_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2094)
WWTo1L1Nu2Q         = Sample.nanoAODfromDAS("WWTo1L1Nu2Q","/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=49.997)
WWTo4Q              = Sample.nanoAODfromDAS("WWTo4Q","/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=51.723)

ZZTo2L2Nu           = Sample.nanoAODfromDAS("ZZTo2L2Nu","/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.564)
ZZTo2L2Q            = Sample.nanoAODfromDAS("ZZTo2L2Q","/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3.28)
ZZTo2Q2Nu           = Sample.nanoAODfromDAS("ZZTo2Q2Nu","/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.04)
ZZTo4L              = Sample.nanoAODfromDAS("ZZTo4L","/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.256*1.1)

WZTo1L3Nu             = Sample.nanoAODfromDAS("WZTo1L3Nu", "/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=(47.13)*(3*0.108)*(0.2))
WZTo1L1Nu2Q           = Sample.nanoAODfromDAS("WZTo1L1Nu2Q","/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=10.71)
WZTo2L2Q              = Sample.nanoAODfromDAS("WZTo2L2Q","/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.60)

SSWW                = Sample.nanoAODfromDAS("SSWW", "/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.02794)

multiboson = [
    # VVTo2L2Nu,
    WW,
    WZ,
    ZZ,
    WWW_4F,
    WWZ_4F,
    WZZ,
    ZZZ,
    WZTo3LNu,
    WWTo2L2Nu,
    WWDoubleTo2L,
    WWTo1L1Nu2Q,
    WWTo4Q,
    ZZTo2L2Nu,
    ZZTo2L2Q,
    ZZTo2Q2Nu,
    ZZTo4L,
    WZTo1L3Nu,
    WZTo1L1Nu2Q,
    WZTo2L2Q,
    SSWW
]

################################################################################
## rare
TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.009103)
TTWW = Sample.nanoAODfromDAS("TTWW", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.007829)
TTWZ = Sample.nanoAODfromDAS("TTWZ", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.002919)
TTZZ = Sample.nanoAODfromDAS("TTZZ", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001573)

TTHH = Sample.nanoAODfromDAS("TTHH", "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0006655)
TTWH = Sample.nanoAODfromDAS("TTWH", "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001141)
TTZH = Sample.nanoAODfromDAS("TTZH", "/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.00113)

TTTJ = Sample.nanoAODfromDAS("TTTJ", "/TTTJ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0003974)
TTTW = Sample.nanoAODfromDAS("TTTW", "/TTTW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0007314)

rareTop = [
    TTTT,
    TTWW,
    TTWZ,
    TTZZ,
    TTHH,
    TTWH,
    TTZH,
    TTTJ,
    TTTW
]


################################################################################
# QCD
QCD_HT100to200   = Sample.nanoAODfromDAS("QCD_HT100to200",   "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",                    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=27849880)
QCD_HT200to300   = Sample.nanoAODfromDAS("QCD_HT200to300",   "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",                    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1716997)
QCD_HT300to500   = Sample.nanoAODfromDAS("QCD_HT300to500",   "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",                    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=351302)
QCD_HT500to700   = Sample.nanoAODfromDAS("QCD_HT500to700",   "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",                    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=31630)
QCD_HT700to1000  = Sample.nanoAODfromDAS("QCD_HT700to1000",  "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",                   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=6802)
QCD_HT1000to1500 = Sample.nanoAODfromDAS("QCD_HT1000to1500", "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",                  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1206)
QCD_HT1500to2000 = Sample.nanoAODfromDAS("QCD_HT1500to2000", "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",                  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=98.71)
QCD_HT2000toInf  = Sample.nanoAODfromDAS("QCD_HT2000toInf",  "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",                   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=20.2)

QCD = [
    QCD_HT100to200,
    QCD_HT200to300,
    QCD_HT300to500,
    QCD_HT500to700,
    QCD_HT700to1000,
    QCD_HT1000to1500,
    QCD_HT1500to2000,
    QCD_HT2000toInf,
    ]

################################################################################
# W+jets
WJetsToLNu = Sample.nanoAODfromDAS("WJetsToLNu", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=61500)

################################################################################
# wjets

## HT-binned
WJetsToLNu_HT70to100        = Sample.nanoAODfromDAS("WJetsToLNu_HT70to100",        "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",     dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1292.0)
WJetsToLNu_HT100to200       = Sample.nanoAODfromDAS("WJetsToLNu_HT100to200",       "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1395.0)
WJetsToLNu_HT200to400       = Sample.nanoAODfromDAS("WJetsToLNu_HT200to400",       "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=407.9)
WJetsToLNu_HT400to600       = Sample.nanoAODfromDAS("WJetsToLNu_HT400to600",       "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=57.48)
WJetsToLNu_HT600to800       = Sample.nanoAODfromDAS("WJetsToLNu_HT600to800",       "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=12.87)
WJetsToLNu_HT800to1200      = Sample.nanoAODfromDAS("WJetsToLNu_HT800to1200",      "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=5.366)
WJetsToLNu_HT1200to2500     = Sample.nanoAODfromDAS("WJetsToLNu_HT1200to2500",     "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.074)
WJetsToLNu_HT2500toInf      = Sample.nanoAODfromDAS("WJetsToLNu_HT2500toInf",      "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.0389136)      


wjets_ht = [
    WJetsToLNu_HT70to100,
    WJetsToLNu_HT100to200,
    WJetsToLNu_HT200to400,   
    WJetsToLNu_HT400to600,
    WJetsToLNu_HT600to800,
    WJetsToLNu_HT800to1200,
    WJetsToLNu_HT1200to2500,
    WJetsToLNu_HT2500toInf,
    ]


################################################################################

allSamples = DY + TTbar + SingleTop + multiboson + TTX + rareTop + QCD + [WJetsToLNu] + wjets_ht    

for s in allSamples:
    s.isData = False

from nanoMET.tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
