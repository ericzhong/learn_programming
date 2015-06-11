#include<stdio.h>
#include<Python.h>



int inc(int n) {
	return ++n;
}


int add(int a, int b) {
	return a + b;
}


int main() {
	printf("Test:\n");
	printf("add(1,2) = %d\n", add(1,2));
	printf("add(5,2) = %d\n", add(5,2));
	printf("inc(1) = %d\n", inc(1));
	printf("inc(7) = %d\n", inc(7));
	return 0;
}


static PyObject * 
Extest_hello(PyObject *self) {
	return (PyObject *)Py_BuildValue("s", "Hello, Python extensions!");
}


static PyObject * 
Extest_inc(PyObject *self, PyObject *args) {
	int n;
	if(!PyArg_ParseTuple(args, "i", &n))
		return NULL;
	return (PyObject *)Py_BuildValue("i", inc(n));
}


static PyObject * 
Extest_add(PyObject *self, PyObject *args) {
	int a,b;
	if(!PyArg_ParseTuple(args, "ii", &a, &b))    // ii = int,int
		return NULL;
	return (PyObject *)Py_BuildValue("i", add(a,b));
}


static PyMethodDef
ExtestMethods[] = {
	{"hello", Extest_hello, METH_NOARGS},
	{"inc", Extest_inc, METH_VARARGS},
	{"add", Extest_add, METH_VARARGS},
	{NULL, NULL},
};


void initExtest() {
	Py_InitModule("Extest", ExtestMethods);
}




