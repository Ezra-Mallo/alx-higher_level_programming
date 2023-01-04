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
	listint_t *newNode, *copy = *head, *copy2 = *head;
	int num, i, index = 0;

	if (head == NULL)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	/*get the index */
	while (copy->next != NULL)
	{
		num = copy->n;
		if (num < number)
			copy = copy->next;
		else
			break;
		index++;
	}
	/* point to the correct = index - 1 */
	for (i = 0; i < (index - 1); i++)
	{
		if (copy2 == NULL || copy2->next == NULL)
			return (NULL);

		copy2 = copy2->next;
	}
	/* perform this if this is the only record*/
	if (index == 0)
	{
		newNode->next = copy2;
		*head = newNode;
		return (newNode);
	}
	newNode->next = copy2->next;
	copy2->next = newNode;
	return (newNode);
}
