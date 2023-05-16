#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: A PyObject list
 */

void print_python_list_info(PyObject *p)
{
	int size_list, allocation, i;
	PyObject *obj;

	size_list = Py_SIZE(p);
	allocation = ((PyListObject *)p)->allocated;

	printf("[*] Size of Python List = %d\n", size_list);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < size_list; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_getItem(p, i);
		printf("%s\n", PY_TYPE(obj)->tp_name);
	}
}
