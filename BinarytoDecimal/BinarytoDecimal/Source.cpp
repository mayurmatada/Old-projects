#include <iostream>
#include <string.h>
#include <math.h>

using namespace std;

int main()
{
	int Base, i, j, length, total;
	char Binary[20];
	int Decimal[20];



	//---------------------------Execution Part---------------------------//

	cout << "Enter The Binary string you would like to convert to decimal" << endl;
	cin >> Binary;
	length = strlen(Binary);
	Base = length-1;
	for (i = 0; i <= length; i++)
	{
		if (Binary[length - i] == '1')
		{
			Decimal[i] = pow(2, Base);
		}
		else
		{
			Decimal[i] = 0;
		}
		Base--;
	}
	total = 0;
	for (j = 0; j <= length; j++)
	{
		total = total + Decimal[j];
	}
	cout << "The Decimal value is : " << total << endl;
	system("pause");
	return 0;
}