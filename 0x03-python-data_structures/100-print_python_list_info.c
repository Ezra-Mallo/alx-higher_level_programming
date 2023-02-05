#include "Python.h"

/**
 * print_python_list_info - This function prints some basic info about
 *              Python lists.
 * @p: is pointer of type PyObject
 */

void print_python_list_info(PyObject *p)
{
	int allocated, size, i;
	PyListObject *plo;

	plo = (PyListObject *)p;
	size = plo->ob_base.ob_size;
	allocated = plo->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		printf("%s\n", plo->ob_item[i]->ob_type->tp_name);
	}
}
