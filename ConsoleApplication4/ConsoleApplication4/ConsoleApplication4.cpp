// ConsoleApplication4.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include<iostream>

using namespace std;

int main()
{
	int n, i, sum;
	cout << "Which 2 numbers which you like to add" << endl;
	cin >> n;
	cin >> i;
	sum = i + n;
	cout << "The number " << sum << " is the sum of the 2 numbers you have given" << endl;	
	return 0;
}
