//#include <iostream>
//using namespace std;
//
//int main()
//{
//	//Transition		  0		1
//	//double Transition[2][2] = { { 0.75, 0.25 },
//	//{ 0.25, 0.75 } };
//
//	////Emissions	
//	//double S[2][2] = { { 0.45, 0 },
//	//{ 0, 0.05 } };
//
//	//double P[2][2] = { { 0, 0.45 },
//	//{ 0.05, 0 } };
//
//	//double T[2][2] = { { 0.05, 0 },
//	//{ 0, 0.45 } };
//
//	//double O[2][2] = { { 0, 0.05 },
//	//{ 0.45, 0 } };
//
//	//Transition
//	double T[2][2] = {
//		{ 0.5, 0.5 },
//		{ 0.8, 0.2 } };
//
//	//Emissions	
//	double Omama[2][2] = {
//		{ 0.4, 0 },
//		{ 0, 0.1 } };
//
//	double Opapa[2][2] = {
//		{ 0.4, 0 },
//		{ 0, 0.1 } };
//
//	double Opee[2][2] = {
//		{ 0.1, 0 },
//		{ 0, 0.4 } };
//
//	double Opoo[2][2] = {
//		{ 0.1, 0 },
//		{ 0, 0.4 } };
//
//
//	double s0[1][2] = { { 0.5, 0.5 } };
//
//
//
//	return 0;
//}



#include<iostream>
using namespace std;

void calculate_transpose(int matrix[5][5], int rows, int cols);
int main()
{

	int matrix[5][5];
	int i, j, rows, cols;
	// Taking Input In Array

	cout << "Enter Number of ROWS :";
	cin >> rows;

	cout << "Enter Number Of COLS  :";
	cin >> cols;
	for (i = 0; i<rows; i++){
		for (j = 0; j<cols; j++)
		{
			cin >> matrix[i][j];
		}
	}

	cout << "\n Matrix You Entered\n";

	for (i = 0; i<rows; i++){
		for (j = 0; j<cols; j++)
		{
			cout << matrix[i][j] << "     ";
		}
		cout << endl;
	}


	//**********CALLING FUNCTION************//
	calculate_transpose(matrix, rows, cols);


	return 0;
}

void calculate_transpose(int matrix[5][5], int rows, int cols)
{
	int i, j;
	int transpose_matrix[5][5];
	cout << "\n\n\nTranspose of Entered Matrix\n";
	for (i = 0; i<rows; i++){
		for (j = 0; j<cols; j++)
		{
			transpose_matrix[j][i] = matrix[i][j];
		}
		cout << endl;
	}

	for (i = 0; i<cols; i++){
		for (j = 0; j<rows; j++)
		{
			cout << transpose_matrix[i][j] << "   ";
		}
		cout << endl;
	}

}