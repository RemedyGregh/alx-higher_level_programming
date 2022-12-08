#include <stdio.h>
#include "lists.h"

/**
* check_cycle - Checks if a singly linked list has a cycle in it
* @list : Pointer to node of the list
* Return: 0 if there is no cycle, 1 if there's a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}