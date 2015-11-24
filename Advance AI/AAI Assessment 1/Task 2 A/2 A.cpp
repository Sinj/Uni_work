#include <iostream>
using namespace std;

int main()
{
	//Transition		  0		1
	//double Transition[2][2] = { { 0.75, 0.25 },
	//{ 0.25, 0.75 } };

	////Emissions	
	//double S[2][2] = { { 0.45, 0 },
	//{ 0, 0.05 } };

	//double P[2][2] = { { 0, 0.45 },
	//{ 0.05, 0 } };

	//double T[2][2] = { { 0.05, 0 },
	//{ 0, 0.45 } };

	//double O[2][2] = { { 0, 0.05 },
	//{ 0.45, 0 } };

	//Transition
	double T[2][2] = {
		{ 0.5, 0.5 },
		{ 0.8, 0.2 } };

	//Emissions	
	double Omama[2][2] = {
		{ 0.4, 0 },
		{ 0, 0.1 } };

	double Opapa[2][2] = {
		{ 0.4, 0 },
		{ 0, 0.1 } };

	double Opee[2][2] = {
		{ 0.1, 0 },
		{ 0, 0.4 } };

	double Opoo[2][2] = {
		{ 0.1, 0 },
		{ 0, 0.4 } };


	double s0[1][2] = { { 0.5, 0.5 } };



	return 0;
}