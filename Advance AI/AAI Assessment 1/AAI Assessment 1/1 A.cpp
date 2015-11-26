#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	/*
	Bayes rule:
	P(A|B)=P(B|A)*P(A)/P(B)

	For Disease/Test
	P(D|T)=P(T|D)*P(D)/P(T)
	*/


	double Disease = 1 / 10000; //P(D)
	double n_Disease = 1 - Disease; //P(¬D)
	double t_d = 0.99; //P(T|D)
	double nt_d = 0.01; //P(¬T|D)
	double nt_nd = 0.95; //P(¬T|¬D)
	double t_nd = 0.05; //P(T|¬D)
	double Test; //P(T)
	double n_Test; //P(¬T)
	cout << setprecision(6);
	//Get the missing value P(T).
	//P(T)=P(T|D)*P(D)+P(T|¬D)*(¬D)
	Test = t_d * Disease + t_nd * n_Disease;
	n_Test = 1 - Test;
	cout << "The value of P(t) = " << Test << endl;


	cout << fixed << "P(D|T) = " << t_d * Disease / Test << endl;
	cout << "The Probibity that the Disease is true give that the test is true = : " << (t_d * Disease / Test) * 100;


	return 0;
}
