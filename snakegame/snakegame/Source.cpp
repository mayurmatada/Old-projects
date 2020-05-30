#include <iostream>
#include <conio.h>
#include <stdio.h>
#include <cstdlib>
#include <ctime>
#include <Windows.h>


using namespace std;

int snakex, snakey, ratx, raty, width, height, score, dir = 0;

bool gameover = false, rangex, rangey, redo = true;

void setup()
{
	srand(time(NULL));
	int i, j;
	width = 40;
	height = 20;
	snakex = width / 2;
	snakey = height / 2;
	ratx = rand() % width-1;
	raty = rand() % height-1;
	score = 0;
	for (i = 0; i <= height; i++)
	{
		for (j = 0; j <= width; j++)
		{
			if (i == 0 || j == 0 || i == height || j == width)
			{
				cout << "^";
			}
			else if (i == snakey && j == snakex)
			{	
				SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 3);
				cout << "S";
				SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);

			}
			else if (i == raty && j == snakex)
			{
				cout << "R";
			}
			else
			{
				cout << " ";
			}
			
		}
		cout << endl;
	}
	
}

void input()
{
	if (_kbhit())
	{
		switch (_getch())
		{
			case 'w':
				dir = 1;
				break;
			case 's':
				dir = 3;
				break;
			case 'a':
				dir =4;
				break;
			case 'd':
				dir = 2;
				break;
		}
	}
}

void drawing()
{
	int i, j;
	system("cls");
	for (i = 0; i <= height; i++)
	{
		for (j = 0; j <= width; j++)
		{
			if (i == 0 || j == 0 || i == height || j == width)
			{
				SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 4);
				cout << "#";
				SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
			}
			else if (i == snakey && j == snakex)
			{
				SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 10);
				cout << "S";
				SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
			}
			else if (i == raty && j == ratx)
			{
				SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 14);
				cout << "R";
				SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
			}
			else
			{
				cout << " ";
			}

		}
		
		cout << endl;
	}
	cout << "Score:" << score << endl;
}

bool inRange(unsigned low, unsigned high, unsigned x)
{
	return (low <= x && x <= high);
}
void logic()
{
	if (snakex == ratx && snakey == raty)
	{
		score++;
		ratx = rand() % width-1;
		raty = rand() % height-1;
	}
	if (snakex == width || snakey == height || snakex == 0 || snakey == 0)
	{
		gameover = true;
	}
	
	switch (dir)
	{
		case 0:
			break;
		case 1:
			snakey--;
			break;
		case 2:
			snakex++;
			break;
		case 3:
			snakey++;
			break;
		case 4:
			snakex--;
			break;
	}
	rangex = inRange(0, width, ratx);
	rangey = inRange(0, height, raty);
	while (rangex == false || rangey == false)
	{
		ratx = rand() % width - 1;
		raty = rand() % height - 1;
		rangex = inRange(0, width, ratx);
		rangey = inRange(0, height, raty);
	}
}

int main()
{
	char choice;
	while (redo == true)
	{
		setup();
		while (gameover == false)
		{
			input();
			drawing();
			logic();

		}
		cout << "Game Over" << endl;
		cout << "If you wish to play the game again enter R if not enter anything" << endl;
		cin >> choice;
		if (choice == 'r' || choice == 'R')
		{
			redo = true;
			gameover = false;
		}
		else
		{
			redo = false;
		}
	}


	return 0;
}