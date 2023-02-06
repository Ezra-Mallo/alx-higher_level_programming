#include "Python.h"

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_list - This function prints some basic info about
 *              Python lists.
 * @p: is pointer of type PyObject
 */

void print_python_list(PyObject *p)
{
	int allocated, size, i;
	PyListObject *plo;

	plo = (PyListObject *)p;
	size = plo->ob_base.ob_size;
	allocated = plo->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		printf("%s\n", plo->ob_item[i]->ob_type->tp_name);
		print_python_bytes(plo->ob_item[i]);
	}
}

void print_python_bytes(PyObject *p)
{
	int size, byte_size = 0, j;
	PyBytesObject *pbo;

	pbo = (PyBytesObject *)p;
	size = pbo->ob_base.ob_size;

	printf("[.] bytes object info\n");
	if (size >= 10)
		byte_size = 10;
	else
		byte_size = size + 1;

	printf("   size: %d\n", size);
	printf("   trying string: %s\n", pbo->ob_sval);
	printf("   first %d bytes: ", byte_size);

	for (j = 0; j < byte_size; j++)
		printf("%02hhx ", pbo->ob_sval[j]);
	printf("\n");
}
