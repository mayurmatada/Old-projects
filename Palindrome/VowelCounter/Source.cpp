#include <iostream>
#include <string>

using namespace std;

int main()
{
	int strlength, vowels, loop;
	char singlechar;
	string word;

	cout << "Please enter the word in which you would like to check the number of vowels and consonents" << endl;
	cin >> word;

	cout << word << endl;

	strlength = word.length();
	vowels = 0;
	cout << strlength << endl;
	cout << word.at(1) << endl;

	for (loop = 0; loop <= strlength; loop = loop + 1)
	{
		singlechar = word.at(loop);
		cout << word.at(loop);
		//if (singlechar == 'a' || singlechar == 'e' || singlechar == 'i' || singlechar == 'o' || singlechar == 'u' || singlechar == 'A' || singlechar == 'E' || singlechar == 'I' || singlechar == 'O' || singlechar == 'U')
		if ( 1 == 1 )
		{
			vowels = vowels + 1;
		}
	}


	system("pause");
	return 0;
}