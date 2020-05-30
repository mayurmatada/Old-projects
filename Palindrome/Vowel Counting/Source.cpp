#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int strlength, vowels, loop;
	string word;

	cout << "Please enter the word in which you would like to check the number of vowels and consonents" << endl;
	cin >> word;

	cout << word << endl;

	strlength = word.length();
	vowels = 0;
	cout << strlength << endl;

	for (loop = 0; loop <= strlength; loop = loop + 1)
	{
		cout << word.at(loop);
		if (word.at(loop) == 'a' || word.at(loop) == 'e' || word.at(loop) == 'i' || word.at(loop) == 'o' || word.at(loop) == 'u' || word.at(loop) == 'A' || word.at(loop) == 'E' || word.at(loop) == 'I' || word.at(loop) == 'O' || word.at(loop) == 'U')
		{
			vowels = vowels + 1;
		}
	}


	system("pause");
	return 0;
}