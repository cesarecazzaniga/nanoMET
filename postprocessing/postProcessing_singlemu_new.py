'''
Post-processing based on nanoAOD tools
'''

import os
import ROOT

# Import tools
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor   import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel       import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop       import Module

# Import modules
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import puWeightProducer, pufile_data2016, pufile_mc2016, pufile_data2017, pufile_data2018, pufile_mc2017, pufile_mc2018
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.METSigProducer      import METSigProducer
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2    import *

# private modules
from METSigTools           import METSigTools
from lumiWeightProducer    import lumiWeightProducer
from nanoMET.tools.user    import postprocessing_output_directory

# argparser
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")
argParser.add_argument('--logLevel',    action='store', nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )
argParser.add_argument('--samples',     action='store', nargs='*', type=str, default=['TTZToLLNuNu_ext'], help="List of samples to be post-processed, given as CMG component name" )
argParser.add_argument('--skim',        action='store', nargs='?', type=str, default='dimuon', help="Skim conditions to be applied for post-processing" )
argParser.add_argument('--job',         action='store', type=int, default=0, help="Run only jobs i" )
argParser.add_argument('--nJobs',       action='store', nargs='?', type=int,default=1, help="Maximum number of simultaneous jobs.")
argParser.add_argument('--prepare',     action='store_true', help="Prepare, don't acutally run" )
argParser.add_argument('--overwrite',   action='store_true', help="Overwrite" )
argParser.add_argument('--year',        action='store', default=None, help="Which year? Important for json file.")
argParser.add_argument('--era',         action='store', default="v1", help="Which era/subdirectory?")
argParser.add_argument('--ul',          action='store_true', help="Ultra legacy?")
argParser.add_argument('--prevfp',          action='store_true', help="preVFP for UL16?")
argParser.add_argument('--after_tuning',    action='store_true', help="after MET Sig tuning?")
argParser.add_argument('--tuning_era',   action='store', type=str, default="", help="after MET Sig tuning, give tuning string (this is needed to recomute systematics branches)")

options = argParser.parse_args()

# Logger
import nanoMET.tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   options.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None)

# from RootTools
from RootTools.core.standard            import *

# Make samples, will be searched for in the postProcessing directory
from tunes import tuneParams

def nonEmptyFile(f, treeName='Events'):
    logger.info("Checking file: %s"%f)
    rf = ROOT.TFile.Open(f)
    if not rf: return False
    tree = getattr(rf, treeName)
    nonEmpty = True if tree.GetEntries() else False
    if not nonEmpty: logger.info("File is empty")
    rf.Close()
    return nonEmpty

def extractEra(sampleName):
    return sampleName[sampleName.find("Run"):sampleName.find("Run")+len('Run2000A')]

# Import samples
year = int(options.year)

allSamples = []
if year == 2016:
    if options.prevfp:
        from nanoMET.nanoAOD.UL16_nanoAODAPVv9 import allSamples as UL16_nanoAODAPVv9
        from nanoMET.nanoAOD.UL16_DATA_nanoAODAPVv9 import allSamples as UL16_DATA_nanoAODAPVv9
        allSamples =  UL16_nanoAODAPVv9 + UL16_DATA_nanoAODAPVv9
    else:
        from nanoMET.nanoAOD.UL16_nanoAODv9 import allSamples as UL16_nanoAODv9
        from nanoMET.nanoAOD.UL16_DATA_nanoAODv9 import allSamples as UL16_DATA_nanoAODv9
        allSamples =  UL16_nanoAODv9 + UL16_DATA_nanoAODv9

elif year == 2017:

    #check if era is v2 or v9
    if options.era == "v2":
        from nanoMET.nanoAOD.Summer19_UL17nanoAODv2 import allSamples as UL17_nanoAODv2
        from nanoMET.nanoAOD.Run2017_ULnanoAODv2 import allSamples as UL17_DATA_nanoAODv2
        allSamples =  UL17_nanoAODv2 + UL17_DATA_nanoAODv2
    elif options.era == "v9":
        from nanoMET.nanoAOD.UL17_nanoAODv9 import allSamples as UL17_nanoAODv9
        from nanoMET.nanoAOD.UL17_DATA_nanoAODv9 import allSamples as UL17_DATA_nanoAODv9
        allSamples =  UL17_nanoAODv9 + UL17_DATA_nanoAODv9

elif year == 2018:
    #check if era is v2 or v9
    if options.era == "v2":
        from nanoMET.nanoAOD.Summer19_UL18nanoAODv2 import allSamples as Summer19_UL18nanoAODv2
        from nanoMET.nanoAOD.Run2018_ULnanoAODv2 import allSamples as Run2018_ULnanoAODv2
        allSamples = Summer19_UL18nanoAODv2 + Run2018_ULnanoAODv2
    elif options.era == "v9":
        from nanoMET.nanoAOD.UL18_nanoAODv9 import allSamples as UL18_nanoAODv9
        from nanoMET.nanoAOD.UL18_DATA_nanoAODv9 import SingleMuon_Run2018 as UL18_DATA_nanoAODv9
        allSamples =  UL18_nanoAODv9 + UL18_DATA_nanoAODv9
   

logger.info("Searching for sample %s"%options.samples[0])

samples = []
for selectedSample in options.samples:
    for sample in allSamples:
        if selectedSample == sample.name:
            samples.append(sample)
            logger.info("Adding sample %s", sample.name)
            logger.info("Sample has normalization %s", sample.normalization)
            sample.normalization = float(sample.normalization)


if len(samples)==0:
    logger.info( "No samples found. Was looking for %s. Exiting" % options.samples )
    sys.exit(-1)

if len(samples)>1:
    sample_name =  samples[0].name+"_comb"
    logger.info( "Combining samples %s to %s.", ",".join(s.name for s in samples), sample_name )
    sample = Sample.combine(sample_name, samples, maxN = None)
    # Clean up
    for s in samples:
        sample.clear()
    logger.info("Final normalization is %s", sample.normalization)
elif len(samples)==1:
    sample = samples[0]
else:
    raise ValueError( "Need at least one sample. Got %r",samples )

logger.info("Sample contains %s files", len(sample.files))
sample.files = sorted(sample.files) # in order to avoid some random ordered file list, different in each job

#era = None #Lor added this line to use JER V19
if sample.isData:
    era = extractEra(samples[0].name)[-1]
else:
    era = None
logger.info("######### Era %s ########"%era)

# calculate the lumi scale factor for the weight
targetLumi = 1000.
if sample.isData:
    lumiScaleFactor = 1
else:
    lumiScaleFactor = sample.xSection * targetLumi / float(sample.normalization)

print sample.name
keepSampleName = sample.name # to mitigate Mateusz change of naming convention

# filebased job splitting
len_orig = len(sample.files)
logger.info("Sample has %s files", len_orig)
json = sample.json # pickup json from sample, as defined in the Sample repository
sample = sample.split( n=options.nJobs, nSub=options.job)
sample.name = keepSampleName

logger.info("Will run over %s files", len(sample.files))

# Put together skim
isSingleMu     = options.skim.lower().startswith('singlemu')
isDiMuon        = options.skim.lower().startswith('dimuon')
isDiMuonMod     = options.skim.lower().startswith('dimuon_mod')
isDiElectron    = options.skim.lower().startswith('dielectron')
isDiLep         = options.skim.lower().startswith('dilep')
isTriLep        = options.skim.lower().startswith('trilep')
isSingleLep     = options.skim.lower().startswith('singlelep')

skimConds = []
if isSingleMu:
    skimConds.append( "Sum$(Muon_pt>15&&abs(Muon_eta)<2.4)>=2" )
if isDiMuon:
    skimConds.append( "Sum$(Muon_pt>15&&abs(Muon_eta)<2.5)>=2" )
if isDiMuonMod:
    skimConds.append( "Sum$(Muon_pt>15&&abs(Muon_eta)<2.5)>=2  + Sum$(Jet_pt>30&&Jet_jetId&&abs(Jet_eta)<2.4)>0" )
elif isDiElectron:
    skimConds.append( "Sum$(Electron_pt>15&&abs(Electron_eta)<2.5)>=2" )
elif isDiLep:
    skimConds.append( "Sum$(Electron_pt>20&&abs(Electron_eta)<2.5) + Sum$(Muon_pt>20&&abs(Muon_eta)<2.5)>=2" )
elif isTriLep:
    skimConds.append( "Sum$(Electron_pt>20&&abs(Electron_eta)&&Electron_pfRelIso03_all<0.4) + Sum$(Muon_pt>20&&abs(Muon_eta)<2.5&&Muon_pfRelIso03_all<0.4)>=2 && Sum$(Electron_pt>10&&abs(Electron_eta)<2.5)+Sum$(Muon_pt>10&&abs(Muon_eta)<2.5)>=3" )
elif isSingleLep:
    skimConds.append( "Sum$(Electron_pt>20&&abs(Electron_eta)<2.5) + Sum$(Muon_pt>20&&abs(Muon_eta)<2.5)>=1" )

if options.skim.lower().count('met'):
    skimConds.append( "MET_pt>100" )

cut = '&&'.join(skimConds)

logger.info("Using selection: %s", cut)

# Main part
ul_string = ""
vfp_string = "" 
tuning_string = ""  
if options.ul:
    ul_string = "UL"
if options.after_tuning:
    tuning_string = "_afterTuning"
    if options.tuning_era != "":
        tuning_string = "_"+options.tuning_era
    else:
        #throw error message if tuning era is not given, and break the code
        raise Exception("Tuning era is not given, please provide the tuning era if running after tuning!")
if (year == 2016) and (options.prevfp) and (options.ul):
    vfp_string = "preVFP"
    directory = os.path.join( postprocessing_output_directory, "%s_%s_%s_%s"%(options.year, ul_string, vfp_string ,options.era) )
else:
    directory = os.path.join( postprocessing_output_directory, "%s_%s_%s"%(options.year, ul_string ,options.era) )
output_directory = os.path.join( directory, options.skim + tuning_string, sample.name )


#print output_directory
print "Output directory: %s"%output_directory

fileNames = [ ('/'.join(x.split('/')[:-1]), x.split('/')[-1]) for x in sample.files if nonEmptyFile(x)  ]

if not options.overwrite:
    allFiles = []
    for f in fileNames:
        outfile = f[1].replace('.root','_Skim.root')
        if os.path.isfile(output_directory+'/'+outfile):
            try:
                a = helpers.checkRootFile(output_directory+'/'+outfile)
                if a:
                    logger.info('Found file %s, skipping.', outfile)
                    continue
                else:
                    logger.info("Found file %s, but need to rerun.", outfile)
                    allFiles.append(f)
            except:
                logger.info("Found file %s, but need to rerun.", outfile)
                allFiles.append(f)
        else:
            logger.info('No files found for %s, will produce them', outfile)
            allFiles.append(f)
else:
    allFiles = fileNames
        


sample.files = [ f[0] + '/' + f[1] for f in allFiles ]

logger.info("Loading modules.")

if year == 2016:

    puwProducer = puWeightProducer("auto",pufile_data2016,"pu_mc","pileup",verbose=False)

    #default from LOR
    metSigParamsMC      = [1.6789559564013943, 1.543666136735388, 1.4728342034302846, 1.4983602533711493, 1.4758351625239376, 0.008039429222660197, 0.6698834337575063]
    metSigParamsData    = [1.9034557745999647, 1.704569089762286, 1.5854229036413823, 1.4974876665993915, 1.673074548622476, 0.0015993706020479338, 0.6288393591242573]


    #latest version JER - changing according to preVFP or not
    if options.prevfp:

        #default
        metSigParamsMC      = [1.7233640933703651, 1.2691390420006226, 1.5375532736223367, 1.117583454841452, 1.3866901907564293, 1.0982546759948832, 1.3167826276317613, 1.1675469353582268, 0.8686258199233032, 1.1482926088244734, -2.811553978468071, 0.5731002212373926]
        metSigParamsData    = [1.7580656620935375, 1.2070220617924559, 1.5814815279080778, 1.1650782764189878, 1.3580916199834423, 1.1545976315251152, 1.3517938828110463, 1.2310412386048015, 1.6861196003866394, 1.3949528242997369, -2.76995128200754, 0.5734561571452332]

        JER                 = "Summer20UL16APV_JRV3_MC"          if not sample.isData else "Summer20UL16APV_JRV3_DATA"
    else:
        #default
        metSigParamsMC      = [1.8134640795782824, 1.3049913474511203, 1.5412316999582703, 1.1499924604629634, 1.4713894892246735, 1.1394791198883047, 1.4408581772571318, 1.1233727260593565, 0.8985494003108268, 1.0785717392318772, -2.7896110793175093, 0.567584527886775]
        metSigParamsData    = [1.722705456620946, 1.1854411872324149, 1.6668258139467005, 1.1704968669701603, 1.4411842518222444, 1.0642895186507995, 1.4111396382049157, 1.0682471341930553, 1.6203662703781965, 1.3050002474637155, -3.556212288464914, 0.5608989926783028]

        JER                 = "Summer20UL16_JRV3_MC"          if not sample.isData else "Summer20UL16_JRV3_DATA"

    if options.after_tuning:
        metSigParamsMC      = tuneParams[year][options.tuning_era]['mc']
        metSigParamsData    = tuneParams[year][options.tuning_era]['data']
        
        
    jetThreshold = 15      #CZZ: this is the pT threhsold for the cleaned jets for the MET significance calculation

elif year == 2017:
    puwProducer = puWeightProducer("auto",pufile_data2017,"pu_mc","pileup",verbose=False)
    
    #default from LOR 
    metSigParamsMC      = [1.7037614210331564, 1.7166071080686363, 1.6701114323915047, 1.502876236941622, 1.5780611987345947, -0.00012634174329968426, 0.6834329126092852]
    metSigParamsData    = [1.9410724258735805, 1.878895369894863, 1.9122297708165825, 1.7090755971750793, 2.0004413703111146, -0.0001347239857148459, 0.6732736907156339]
    
    if options.after_tuning:
        metSigParamsMC      = tuneParams[year][options.tuning_era]['mc']
        metSigParamsData    = tuneParams[year][options.tuning_era]['data']

    #latest version JER
    JER                 = "Summer19UL17_JRV2_MC"                if not sample.isData else "Summer19UL17_JRV2_DATA"
    
    jetThreshold = 15     #CZZ: this is the pT threhsold for the cleaned jets for the MET significance calculation

elif year == 2018:
    puwProducer = puWeightProducer("auto",pufile_data2018,"pu_mc","pileup",verbose=False)
    
    #default from LOR
    metSigParamsMC      = [1.613165342723556, 1.5745879445558884, 1.636304135309313, 1.3234572369718391, 1.149196560879823, 0.000064832431405, 0.6052764471230091]
    metSigParamsData    = [1.6920121335793759, 1.6857326368531307, 1.5616058777682056, 1.354644121361604, 1.540213907405874, 0.0002222321882632476, 0.6423649298838915]

    if options.after_tuning:
        metSigParamsMC      =  tuneParams[year][options.tuning_era]['mc']
        metSigParamsData    =  tuneParams[year][options.tuning_era]['data']
        
    #latest version JER
    JER                 = "Summer19UL18_JRV2_MC" if not sample.isData else "Summer19UL18_JRV2_DATA"

    jetThreshold = 15    #CZZ: this is the pT threhsold for the cleaned jets for the MET significance calculation

if len(metSigParamsMC) == 12 and len(metSigParamsData) == 12:
    pTdependent = True
elif len(metSigParamsMC) == 7 and len(metSigParamsData) == 7:
    pTdependent = False
else:
    raise Exception("Wrong input parameter settings!" )


unclEnThreshold = 15
metSigParams    = metSigParamsMC if not sample.isData else metSigParamsData
METCollection   = "MET" 
vetoEtaRegion = (2.65, 3.14) if year == 2017 else (10,10)
METBranchName = 'MET'


#create JMECorrector (takes into account JME corrections)
JMECorrector = createJMECorrector(isMC=(not sample.isData), dataYear=year, ultraLegacy=options.ul, preVFP=options.prevfp,runPeriod=era, jesUncert="Total", jetType = "AK4PFchs", metBranchName=METBranchName, isFastSim=False)
modules = [
    JMECorrector()
]


# add METSigProducer
if sample.isData:
    modules += [
        METSigTools(),
        lumiWeightProducer(1, isData=True),
        METSigProducer(JER, metSigParams, useRecorr=False, jetThreshold=jetThreshold, METCollection=METCollection, vetoEtaRegion=vetoEtaRegion, pTdependent=pTdependent),
    ]

else:
    modules += [
        puwProducer,
        lumiWeightProducer(lumiScaleFactor),
        METSigTools(),
        METSigProducer(JER, metSigParams, useRecorr=False, calcVariations=True, jetThreshold=jetThreshold, METCollection=METCollection, vetoEtaRegion=vetoEtaRegion, pTdependent=pTdependent),
    ]

logger.info("Preparing post-processor.")

p = PostProcessor(output_directory,sample.files,cut=cut, modules=modules, jsonInput=(json if sample.isData else None) ) # could make use of hadd to reduce number of files in the future.
if not options.prepare:
    logger.info("Running ... ")
    p.run()
    logger.info("Done.")

