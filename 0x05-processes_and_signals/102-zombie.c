#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>


/**
 * infinite_while - infinite loop
 *
 * Return: always zero
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - entry point
 *
 * Return: always zero
 */
int main(void)
{
	int n_processes = 0, child_pid;

	while (n_processes < 5)
	{
		child_pid = fork();

		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			n_processes++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
