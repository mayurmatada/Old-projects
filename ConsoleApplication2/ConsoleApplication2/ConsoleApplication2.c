// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <conio.h>
#include <Windows.h>

int main()
{
	int factNum,  iteration, factorial;
	printf("Enter the number you would like to perform a factorial on:\n");
	scanf_s("%d", &factNum);
	factorial = factNum;
	for (iteration = factNum - 1; iteration >= 1; iteration--)
	{
		
		factorial = factorial * iteration;
	
	}
	printf("\nThe factorial of %d is %d\n", factNum, factorial);
	Sleep (3000);
	
}

