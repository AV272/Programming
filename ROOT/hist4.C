TH1F *h[10];
TH1F *hh;

int Nevents =100000;
float h_mean;

TRandom *r = new TRandom();

float pdf(float x){
  if(x<3 || x>7){return 0;} // if(!(x>3 && x<7)){return0;}
  if(x<=5){return x-3;}
  return pdf(5)-x+5;
  }

float gen_event(){
  float x,y;
  do{
   x = 10.*r->Rndm();
   y = 2.*r->Rndm();
   }while(y>pdf(x));
  return x;
}

void hist3() {
   int s[10];
   TString h_name;
   TCanvas *canv = new TCanvas("canv", "MyCanv", 600,600);
   hh = new TH1F("hh", "Histo", 50, 0, 10);
   float mean = 0.;
   float xx;
   for(int i=0; i<Nevents; i++){
       xx = gen_event();
       hh->Fill(xx );
       mean += xx;
   }
   mean /= float(Nevents);
   cout << mean << " " << hh->GetMean() << endl;
   for(int k =1; k<11; k++){h_mean += hh->GetBinContent(k)*hh->GetBinCenter(k);}
   
   
   h_mean /= float(Nevents);
   cout << mean << " " << hh->GetMean() << "  " << h_mean << endl;
   hh->Draw("E");
 //  gSystem->Exit(0);
}