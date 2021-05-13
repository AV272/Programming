#include <TPDF.h>
#include <TCanvas.h>
#include <TH1.h>

using namespace std;

void simpleReader()
{
    TCanvas* canvas = new TCanvas("canvas"); //то где бдуем рисовать и что записывать в файл

    TH1F* histo = new TH1F("histo","test 1",10,0.,10.); //просто какая-то гистограммка, которую выводим сначала на канвас

    //наводим красивости
    histo->SetFillColor(2);
    histo->Fill(2.);
    histo->Draw(); //рисуем гистограмму

    canvas->Print("plots.pdf(","Title:One bin filled"); //первый вызов Принт. После имени файла идёт открывающая скобочка

    histo->Fill(4.); //обновляем гистограмму добавляя новые данные
    histo->Draw(); //перерисовываем содержимое канваса, выводя обновлённую гистограмму
    canvas->Print("plots.pdf","Title:Two bins filled"); //записываем обновлённую гистограмму, скобочки уже не нужны

    //по аналогии создаём несколько страничек с различными рисунками внутри ПДФ файла
    //после запятой у функции принт текстовая строка используется в оглавлении внутри файла ПДФ
    histo->Fill(6.);
    histo->Draw();
    canvas->Print("plots.pdf","Title:Three bins filled");
    histo->Fill(8.);
    histo->Draw();
    canvas->Print("plots.pdf","Title:Four bins filled");
    histo->Fill(8.);
    histo->Draw();
    canvas->Print("plots.pdf)","Title:The fourth bin content is 2"); //в послденем вызове Принт не забываем закрыть скобочку, чтобы оглавление завершить
}
