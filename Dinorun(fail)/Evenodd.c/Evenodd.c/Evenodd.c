// Evenodd.c.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <stdio.h>
#include <conio.h>
#include <time.h>
#include <Windows.h>

int main()
{
	int n;
	printf("Enter the number you would like to check for even or odd\n");
	scanf_s("%d", &n);
	if (n % 2 == 0)
	{
		printf("The number you have given is even");
	}
	else
	{
		printf("The number you have given is odd");
	}
	Sleep (10000);
	return 0;
}

