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
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));

	if (newNode == NULL)
	{
		*head = NULL;
		return (NULL);
	}

	if (number >= 0)
	{
		newNode->n = number;
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		*head = NULL;
		return (NULL);
	}

	return (*head);
}
