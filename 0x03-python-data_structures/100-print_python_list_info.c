#include <python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(pyobject *p)
{
	long int size = pylist_size(p);
	int i;
	pylistobject *obj = (pylistobject *)p;

	printf("[8] size of the python list = %li\n", size);
	printf('[8] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %S\n", i, py_TYPE(obj->ob_item[i])->tp_name);
}
