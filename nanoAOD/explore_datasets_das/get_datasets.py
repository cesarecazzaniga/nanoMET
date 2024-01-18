import os
import time
import argparse
import pandas as pd
import optparse
import ROOT

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)


parser = optparse.OptionParser(description="Option parser")
parser.add_option('--dataset_query', dest='dataset_query', default = "", help='DAS query for datasets')
parser.add_option('--output_dir', dest='output_dir', default = "", help='Output directory path')
parser.add_option('--add_redirector', dest='add_redirector', default = "", help='Add redirector to file names')

(opt, args) = parser.parse_args()

cwd = os.getcwd()




def main():

    #Start counting time
    start_time = time.time()

    #execute command : voms-proxy-init --rfc --voms cms -valid 192:00 - necessary to access grid storage element
    proxy_info_time = os.popen("voms-proxy-info").read().splitlines()[6]
    #look for string "timeleft" in proxy_info
    if "timeleft" not in proxy_info_time:
        print "==> Proxy is not valid. Now execute command: voms-proxy-init --rfc --voms cms -valid 192:00"
        os.system("voms-proxy-init --rfc --voms cms -valid 192:00")


    #make directory for output files
    if not os.path.exists(opt.output_dir):
        os.makedirs(opt.output_dir)

    #Get datasets from DAS
    print "==> Getting dataset/s from DAS"
    print("DAS command used: " + "dasgoclient -query='" + opt.dataset_query + "'")

    #Execute DAS command
    datasets = os.popen("dasgoclient -query='" + opt.dataset_query + "'").read().splitlines()

    print("==> Datasets found: ")
    #loop over datasets and print them
    for dataset in datasets:
        print dataset

    #loop over datasets and save files name contained in them to output directory
    for dataset in datasets:

        #get files name contained in dataset
        files = os.popen("dasgoclient -query='file dataset=" + dataset + "'").read().splitlines()

        #create file with name dataset_name.txt
        f = open(opt.output_dir + "/dataset_" + dataset.replace("/", "_") + ".txt", "w+")

        #loop over files and save them to file
        for file in files:
            #if add_redirector option is set, add redirector to file name at the beginning
            if opt.add_redirector != "":
                f.write(opt.add_redirector + file + "\n")
            else:
                f.write(file + "\n")

        f.close()

        print "==> File " + "dataset_" + dataset.replace("/", "_") + ".txt" + " saved to " + opt.output_dir + " directory"


    #End counting time
    end_time = time.time()
    print "==> Total time taken to run the script: ", end_time - start_time, " seconds" 

if (__name__ == "__main__"):

    main()