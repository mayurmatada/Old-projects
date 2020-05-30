#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	string Orignal, reversed;

	cout << "Enter the word which you would like to verify as a palindrome or not:"; 
	cin >> Orignal;
	cout << endl;

	reversed = Orignal;
	reverse(reversed.begin(), reversed.end());

	if (Orignal == reversed)
	{
		cout << "The given word is a palindrome" << endl;
	}
	if (Orignal != reversed)
	{
		cout << "The given word is not a palindrome" << endl;
	}

	system("pause");
	return 0;
}