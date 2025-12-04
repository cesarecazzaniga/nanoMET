import pickle, os, time
import ROOT


def main():

    #input path to the pickle file
    input_path = "/afs/cern.ch/user/c/cazzanig/MET_studies/MET_significance/PLOT_dir/systematicsPlots/2018/SingleMuALLComplete_UL_2018_v9_zeroGoodJetVeto_onZ/TunegoodIsoMuons18-onZ-zeroGoodJetVeto/mumu/results.pkl"

    #output_dir = os.getcwd() + "/histos_systematics/2016_postVPF/"
    #output_dir = os.getcwd() + "/histos_systematics/2017/"
    output_dir = os.getcwd() + "/histos_systematics_met/2018/" #histos_systematics_met_sig
    scale_mc_to_data = True

    with open(input_path, "rb") as f:
        results = pickle.load(f)

    variable_sys_mc = "MET_fine_mc"  #this is the key in the dictionary _significance
    variable_nom = "MET_fine"  #this is the key in the dictionary
    variable_data = "MET_fine_data"  #this is the key in the dictionary
    processes = ["DY_LO", "Top" ,"diboson", "rare", "QCD", "WJets","SingleMuon_Run2018"] #last must be data
    sys = ['jesTotalUp', 'jesTotalDown','jerUp', 'jerDown', 'unclustEnUp', 'unclustEnDown']

    new_dict = {}
    #initialise the dicitonary with the processes as keys
    for process in processes:
        new_dict[process] = []

    #loop over the keys of the dictionary
    for key in results.keys():
        #loop over the list of given key
        for histo in list(results[key][0]):
            print("Histo name: ", histo.GetName())
            #check if histo is an histogram and check if the name of the histogram contains the variable
            if "TH1" in str(type(histo)) and ((variable_sys_mc in histo.GetName()) or (variable_data in histo.GetName())) or (variable_nom in histo.GetName()):
                    #check if one of the processes is in the name of the histogram
                    for process in processes:
                        if process in histo.GetName():
                            
                            sys_histo = False
                            for s in sys:
                                if s in histo.GetName():
                                    sys_histo = True
                                    break

                            if sys_histo:
                                histo.SetName(key)
                            else:
                                #rename the histogram as the key of the dictionary + process
                                histo.SetName(key + "_nominal")
                            new_dict[process].append(histo)

    
    print ("Number of histograms in the dictionary: ", new_dict)
    #if scale_mc_to_data is True, scale the MC histograms to the data histogram
    if scale_mc_to_data:
        data_histos = new_dict[processes[-1]]
        for process in processes:
            if process != processes[-1]:
                mc_histos = new_dict[process]
                for i in range(len(mc_histos)):
                    if data_histos[0].Integral() != 0 and mc_histos[i].Integral() != 0:
                        mc_histos[i].Scale(data_histos[0].Integral()/mc_histos[i].Integral())
                new_dict[process] = mc_histos
    
    #create the output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #loop over the new dictionary and save the histograms in a root file
    for key in new_dict.keys():
        if len(new_dict[key]) > 0:
            output_path = output_dir + key + ".root"
            print("Saving histograms in: ", output_path)
            f = ROOT.TFile(output_path, "RECREATE")
            for histo in new_dict[key]:
                histo.Write()
            f.Close()




if (__name__ == "__main__"):

    main()