#include "lists.h"

/**
 * check_cycle - Write a function in C that checks if 
 * a singly linked list has a cycle in it.
 *
 * @list: The pointer to the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *currentS = list;
	listint_t *currentF = list;

	while(currentS && currentF && currentF->next)
	{
		currentS = currentS->next;
		currentF = currentF->next->next;
		if (currentF == currentS)
			return (1);
	}

	return (0);
}
