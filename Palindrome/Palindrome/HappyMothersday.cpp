#include <iostream>
#include <string>
#include <Windows.h>

using namespace std;

int main()
{
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 2);
	string star = "**";
	
	/*s s ss .*/cout << star << "    " << star << "      "  << star << star << "       "  << star << star << star << star << "  " << star << star << star << star << endl;
	/*s s s s .*/cout << star << "    " << star << "     "  << star << "  " << star << "      "  << star << "    " << star << "  " << star << "    " << star << endl;
	/*ssss s s .*/cout << star << star << star << star << "    "  << star << "    "  << star << "     "  << star << star << star << star << "  " << star << star << star << star << endl;
	/*ssss sssss .*/cout << star << star << star << star << "   "  << star << star << star << star << star << "    "  << star << "        " << star << endl;
	/*s s s s .*/cout << star << "    " << star << "  " << star << "        "  << star << "   "  << star << "        " << star << endl;
	/*s s s s .*/cout << star << "    " << star << " "  << star << "          "  << star << "  "  << star << "        " << star << endl;

	cout << "Happy Mother's Day" << endl;

	system("pause");
	return 0;
}