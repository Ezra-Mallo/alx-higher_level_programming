#include "lists.h"

/**
 * insert_node - Function in C that inserts a number into a
 *               sorted singly linked list.
 * @head: 1st parameter
 * @number: 2nd parameter
 *
 * Return: returns the listing
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *copy = *head;
	int num, i = 0, j;

	newNode = malloc(sizeof(listint_t));

	if (newNode == NULL)
	{
		*head = NULL;
		return (NULL);
	}

	newNode->n = number;

	while (copy->next != NULL)
	{
		num = copy->n;
		if (num != number)
			copy = copy->next;
		else
			break;
		i++;
	}

	for (j = 0; j < (i - 1); j++)
	{
		if (copy == NULL || copy->next == NULL)
			return (NULL);

		copy = copy->next;
	}

	if (i == 0)
	{
		new_node->next = copy;
		*head = new_node;
		return (new_node);
	}

	new_node->next = copy->next;
	copy->next = new_node;

	return (new_node);
}
