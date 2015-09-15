#include "TStyle.h"
#include "RooGlobalFunc.h"
#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooPlot.h"
#include "RooAbsPdf.h"
#include "RooFitResult.h"
#include "RooMCStudy.h"
#include "RooGaussian.h"
#include "RooProdPdf.h"
#include "RooPolynomial.h"
#include "RooExponential.h"
#include "RooAddPdf.h"
#include "TH1.h"
#include "TH2.h"
#include "TFile.h"
#include "TTree.h"
#include "TPad.h"
#include "TCanvas.h"

using namespace RooFit;

void first_plots(){
  //First we open the input dataset.root file:
  TFile* inputFile = TFile::Open("dataset.root");
  //Now we attach to the TTree containing the data:
  TTree* inputTree = (TTree*)inputFile->Get("modelData");
  
  //Define the observables and ranges over which the PDFs will be made 
  //based on the two columns in the ntuple:
  RooRealVar obs_mass("mass","mass",5300,5400,"MeV/c^{2}");
  RooRealVar obs_time("time","time",0.0,12.0,"ps");
  
  //And create a RooDataSet object containing these observables:
  RooDataSet *data = new RooDataSet("data","data",inputTree,RooArgList(obs_mass,obs_time));
  
  //Next, let's plot the RooDataSet in each dimension to see what 
  //the distributions look like:
  
  //Create a TCanvas
  TCanvas *c = new TCanvas("data","data",1024,512);
  //Chop it in two to show both dimensions:
  c->Divide(2);
  
  //First we'll plot the mass on the left hand side
  c->cd(1);
  //Adjust the margins as the root default is terrible
  gPad->SetLeftMargin(0.15); gPad->SetBottomMargin(0.15);
  //Now the important bit: A RooPlot is made in the mass dimension:
  RooPlot *massplot = obs_mass.frame();
  
  //We plot the data on this RooPlot:
  data->plotOn(massplot);
  massplot->GetYaxis()->SetTitleOffset(1.6);
  massplot->Draw();
  
  //Now we plot the time distribution on the RHS: 
  c->cd(2);
  gPad->SetLeftMargin(0.15); gPad->SetBottomMargin(0.15);
  //Logarithmic axis as this looks better:
  gPad->SetLogy();
  RooPlot *timeplot = obs_time.frame();
  data->plotOn(timeplot);
  timeplot->GetYaxis()->SetTitleOffset(1.6);
  timeplot->Draw();
  c->Draw();
  c->SaveAs("dataplot.png");
}
