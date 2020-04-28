#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * list - linked list
 * Return: 0 if cycle, 1 if no cycle
 */

int check_cycle(listint_t *list)
{
    listint_t *first, *second;

    first = list;
    second = list;

    while (first != NULL && second != NULL && second->next != NULL)
    {
        first = first->next->next;
        second = second->next;

        if (first == second)
        {
            return (1);
        }
    }
    return (0);
}