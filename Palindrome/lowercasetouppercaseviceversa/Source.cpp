#include <iostream>
#include <string>

using namespace std;

int main()
{
	string input;
	int loop;

	cout << "Please enter the string in which you would like to convert the case sensitivity" << endl;
	cin >> input;

	for (loop = 0; loop <= input.length(); loop = loop + 1)
	{
		if (input.at(loop) >= 97 && input.at(loop) <= 122)
		{
			input.at(loop) = input.at(loop) - 32;
		}
		if (input.at(loop) >= 65 && input.at(loop) <= 92)
		{
			input.at(loop) = input.at(loop) + 32;
		}
		if (input.at(loop) < 65 && input.at(loop) > 92 && input.at(loop) < 97 && input.at(loop) > 122)
		{
			input.at(loop) = input.at(loop);
		}
	}

	system("pause");
	return 0;
}
