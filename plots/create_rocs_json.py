import ROOT
import os
import sys
import copy
from tqdm import tqdm
import numpy as np


cwd = os.getcwd()

def drawCMSlogo(year):
    lumi_per_year = {
        "Run1": "4.9 fb^{-1} (7 TeV)",
        "2016": "35.92 fb^{-1} (13 TeV)",
        "2017": "41.53 fb^{-1} (13 TeV)",
        "2018": "59.8 fb^{-1} (13 TeV)",
        "Run2": "138 fb^{-1} (13 TeV)",
    }

    label_lumi = ROOT.TLatex()
    label_cms = ROOT.TLatex()
    label_preliminary = ROOT.TLatex()

    label_lumi.SetNDC()
    label_cms.SetNDC()
    label_preliminary.SetNDC()
    label_lumi.SetTextFont(42)
    label_cms.SetTextFont(60)
    label_preliminary.SetTextFont(52)
    label_lumi.SetTextAlign(31)  # align right                                                                                                                                                                      

    label_cms.SetTextAlign(11)  # align left                                                                                                                                                                        
    label_preliminary.SetTextAlign(11)  # align left                                                                                                                                                                
    
    top_margin = ROOT.gPad.GetTopMargin()
    right_margin = ROOT.gPad.GetRightMargin()
    label_lumi.SetTextSize(0.40 * top_margin)
    label_cms.SetTextSize(0.6 * top_margin)
    label_preliminary.SetTextSize(0.4 * top_margin)
    label_text_offset = 0.2
    label_lumi.DrawLatex(0.90, 1 - top_margin + label_text_offset * top_margin + 0.02, lumi_per_year[year])
    label_cms.DrawLatex(0.10, 1 - top_margin + label_text_offset * top_margin + 0.02, "CMS")
    label_preliminary.DrawLatex(0.22, 1 - top_margin + label_text_offset * top_margin + 0.02, "Simulation Preliminary")

def read_histos(input_dir,variables,signal,backgrounds):

    histos = {
        "signal" : {},
        "backgrounds" : {
                bkg : {} for bkg in backgrounds + ["all"]
        },

    }

    for var in variables:

        #Define input file
        input_file = input_dir + var + ".root"

        #Open input file
        f = ROOT.TFile.Open(input_file)

        #Get all the keys in the file
        keys = f.GetListOfKeys()

        #Get canvas from first key
        canvas = f.Get(keys[0].GetName())

        tpad_primitives = canvas.GetListOfPrimitives()
        top_tpad_primitives = []
        for primitive in tpad_primitives:
            if var in primitive.GetName():
                top_tpad_primitives.append(primitive)
        if len(top_tpad_primitives) > 0:
            top_tpad_primitives = tpad_primitives
        else:
            top_tpad_primitives = tpad_primitives[0].GetListOfPrimitives() 


        #Iterate over the list of primitives in the canvas
        for primitive in top_tpad_primitives:
                
                #Get the name of the primitive
                name = primitive.GetName()
    
                #Check if the primitive is a histogram
                if (isinstance(primitive,ROOT.TH1D)):

                    process_name = name.replace(var,"").split("_")[1]
    
                    #Check if the histogram is a signal
                    if (process_name in signal and "_copy" not in name):

                        print("Signal process: " + process_name)
                        print("Primitive: ", primitive)

                        #print the integral of the histogram
                        print("Integral " + process_name + " " + var + ": " + str(primitive.Integral()))

                        #Add histogram to dictionary
                        histos["signal"][var] = primitive
    
                    #Check if the histogram is a background
                    elif (process_name in backgrounds and "_copy" not in name):
    
                        print("Background process: " + process_name)
                        print("Primitive: ", primitive)

                        #Add histogram to dictionary
                        histos["backgrounds"][process_name][var] = primitive

                        #print the integral of the histogram
                        print("Integral " + process_name + " " + var + ": " + str(primitive.Integral()))
        


    #run over the dictionary, if signal subtract all the backgrounds , and then do the same following the order of backgrounds
    histos_norm = copy.deepcopy(histos)
    for var in variables:
            
            #Get signal histogram
            signal_histo = histos["signal"][var]

            #print content first bin
            print("Content first bin signal " + var + ": " + str(signal_histo.GetBinContent(1)))
    
            #Get background histograms
            backgrounds_histos = histos["backgrounds"]

            #print content first bin
            for bkg in backgrounds:
                print("Content first bin background " + bkg + " " + var + ": " + str(backgrounds_histos[bkg][var].GetBinContent(1)))

            #Add signal to the dictionary
            histos_norm["signal"][var] = signal_histo

            #Normalize signal histogram
            histos_norm["signal"][var].Scale(1/histos_norm["signal"][var].Integral())
    
            #Initailize the sum of all backgrounds
            histos_norm["backgrounds"]["all"][var] = copy.deepcopy(backgrounds_histos[backgrounds[0]][var])

            

            for i in range(0,len(backgrounds)):
                                    
                    #Get background histogram
                    background_histo = backgrounds_histos[backgrounds[i]][var]
        
                    #Add background to the dictionary
                    histos_norm["backgrounds"][backgrounds[i]][var] = background_histo   

                    if (i > 0):
                        #Subtract background from previous one
                        histos_norm["backgrounds"][backgrounds[i]][var].Add(background_histo,+1)

                    #Normalize background histogram
                    if (histos_norm["backgrounds"][backgrounds[i]][var].Integral() > 0):
                        histos_norm["backgrounds"][backgrounds[i]][var].Scale(1/histos_norm["backgrounds"][backgrounds[i]][var].Integral())
                    else:
                        histos_norm["backgrounds"][backgrounds[i]][var].Scale(1)


            #Normalize the sum of all backgrounds
            histos_norm["backgrounds"]["all"][var].Scale(1/histos_norm["backgrounds"]["all"][var].Integral())

        
    print(histos_norm["backgrounds"]["all"].keys())
    return histos_norm


def compute_ROCs(histos,variables,signal,backgrounds,output_dir):
    
    rocs = {
         bkg : {"eff_s":{} , "eff_b":{}} for bkg in backgrounds + ["all"]
    }

    print("All background keys: ",histos["backgrounds"]["all"].keys())

    #loop over variables
    for var in tqdm(variables):

        #Get signal histogram
        signal_histo = histos["signal"][var]

        #Get background histograms
        backgrounds_histos = histos["backgrounds"]

        #Initialize lists of signal and background efficiencies
        rocs["all"]["eff_s"][var] = []
        rocs["all"]["eff_b"][var] = []

        #Loop over backgrounds
        for bkg in backgrounds:
                rocs[bkg]["eff_s"][var] = []
                rocs[bkg]["eff_b"][var] = []

        print(backgrounds_histos["all"].keys())

        #Compute integral of signal histogram
        signal_integral = signal_histo.Integral()
        print("Signal integral " + var + ": " + str(signal_integral))

        #Loop over backgrounds
        for bkg in backgrounds:
            #Compute integral of background histogram
            background_integral = backgrounds_histos[bkg][var].Integral()
            print("Background integral " + var + ": " + str(background_integral))

        #Loop over signal bins
        for i in range(1,signal_histo.GetNbinsX()+1):

            #Get signal integral
            signal_integral = signal_histo.Integral(i,signal_histo.GetNbinsX())

            #Get total background integral
            print(list(backgrounds_histos["all"].keys()))
            print(backgrounds_histos['Top'].keys())
            total_background_integral = backgrounds_histos["all"][var].Integral(i,signal_histo.GetNbinsX())

            #Compute signal efficiency
            #signal_efficiency = signal_integral/signal_histo.Integral()
            signal_efficiency = signal_integral/signal_histo.Integral()

            #Compute total background efficiency
            total_background_efficiency =  total_background_integral/backgrounds_histos["all"][var].Integral()

            #Add signal efficiency to dictionary
            rocs["all"]["eff_s"][var].append(signal_efficiency)

            #Add total background efficiency to dictionary
            rocs["all"]["eff_b"][var].append(total_background_efficiency)


            #Loop over backgrounds
            for bkg in backgrounds:

                #Get background integral
                background_integral = backgrounds_histos[bkg][var].Integral(i,signal_histo.GetNbinsX())

                #Compute background efficiency
                background_efficiency = 0

                if (backgrounds_histos[bkg][var].Integral() > 0):        
                    background_efficiency = background_integral/backgrounds_histos[bkg][var].Integral()

                #Add background efficiency to dictionary
                rocs[bkg]["eff_b"][var].append(background_efficiency)

                #Add signal efficiency to dictionary
                rocs[bkg]["eff_s"][var].append(signal_efficiency)



    #save rocs in a json file
    import json
    with open(output_dir + "rocs.json", "w") as f:
        json.dump(rocs, f, indent=4)

    return rocs





def main():

    print("==> Starting ROCs analysis from histograms <==")

    #double muon dataset
    input_dir="/afs/cern.ch/user/p/piedra/work/public/forMetSignificance/analysisPlots/2018/UL_2018_v9_small_tuneDoubleMuALL_UL_2018_v9_norm_sumPt15_pTdep/diMuon-looseLeptonVeto-onZ-zeroGoodJetVeto/mumu/lin/"
    output_dir = cwd + "/ROC_dir/preliminary_an_met_sigDY_perf_DoubleMuon_results_NEW_jetveto/"

    #Create output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    

    #Define variables to be plotted
    variables = ["MET_T1_pt","MET_significance"]
    line_colors = [ROOT.kCyan+1,ROOT.kMagenta-7,ROOT.kOrange-3,ROOT.kRed-4]
    legend_labels = ["E_{T}^{miss} (T1)","E_{T}^{miss} Significance (T1)"]

    #Define signal and backgrounds - keep same naming as for histograms script
    signal = ["DY"]
    backgrounds = ["diboson", "Top", "rare" ]

    #Define year
    year = "Run2"

    #Read from input directory the histograms
    print("==> Reading histograms from input directory: " + input_dir)
    histos = read_histos(input_dir,variables,signal,backgrounds)
    print("==> Done reading histograms from input directory: " + input_dir)


    #Compute ROCs
    print("==> Computing ROCs")
    rocs = compute_ROCs(histos,variables,signal,backgrounds,output_dir)
    print("==> Done computing ROCs")




if (__name__ == "__main__"):

    main()
