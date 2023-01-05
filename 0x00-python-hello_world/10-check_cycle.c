#include "lists.h"

/**
 * check_cycle - Function in C that checks if a singly linked list
 *               has a cycle in it.
 * @list: head
 * Return: 1 if true and 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list->next;
	fast = list->next->next;
	while (slow && fast && fast->next)
	{
		/**
		 * Slow pointer will move one node per iteration whereas
		 * fast node will move two nodes per iteration
		 */
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
