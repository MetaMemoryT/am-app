// Name of program mainreturn.cpp
#include <iostream>
#include <Python.h>
#include <string>
#include "bigMap.h"
#include "bigMap.cpp"

using namespace std;
  
void runPy() {

    /*
	if (PyImport_AppendInittab("low", PyInit_lowModule) == -1) {
        fprintf(stderr, "Error: could not extend in-built modules table\n");
        exit(1);
    }
    */
    // Py_SetPath(L"/Users/seanusick/p/python-embed/libs/cpython/Lib:/Users/seanusick/p/python-embed/libs/cpython/build/lib.macosx-11.5-x86_64-3.10:/Volumes/t3/am-app/src/app");

    Py_SetPath(L"/Users/seanusick/p/python-embed/libs/cpython/Lib:/Users/seanusick/p/python-embed/libs/cpython/build/lib.macosx-11.5-x86_64-3.10:/Users/seanusick/p/am-app/src/app");
    Py_SetPythonHome(L"/Users/seanusick/p/python-embed/libs/cpython/Lib:/Users/seanusick/p/python-embed/libs/cpython/build/lib.macosx-11.5-x86_64-3.10");

    if (!Py_IsInitialized()) {
        Py_Initialize();
    }
	
    if (!Py_IsInitialized()) {
        printf("Failed to initialize python interpreter.");
    }
}

int main(int argc, char** argv)
{
    /*
    cout << "You have entered " << argc
         << " arguments:" << "\n";
   

    for (int i = 0; i < argc; ++i)
        cout << argv[i] << "\n";
   */



    // cout << argv[1] << "\n";
    if (strcmp( argv[1], "-print-foo") == 0) {
        cout << "foo" << "\n";
    }

    int globalResult;
    if (strcmp( argv[1], "-run-py") == 0) {
        runPy();
        PyObject *mymod = PyImport_ImportModule("simple");
        PyObject *strfunc = PyObject_GetAttrString(mymod, "fun1");
        PyObject *strargs = Py_BuildValue("si", "abc3", 4);
        PyObject *ret = PyEval_CallObject(strfunc, strargs);
        PyArg_Parse(ret, "i", &globalResult);
        cout << globalResult << "\n";
    }

    if (strcmp( argv[1], "-run-dict") == 0) {
        runPy();
        PyObject *d = PyDict_New();
        PyObject *a = Py_BuildValue("s", "a");
        PyObject *a_val = Py_BuildValue("s", "a_val");

        PyObject *b = Py_BuildValue("s", "b");
        PyObject *b_val = Py_BuildValue("s", "b_val");
        PyDict_SetItem(d, a, a_val);
        PyDict_SetItem(d, b, b_val);
        
        PyObject* objectsRepresentation = PyObject_Repr(d);
        const char* s = PyUnicode_AsUTF8(objectsRepresentation);
        cout << "python object" << s << "\n";

        PyObject *mymod = PyImport_ImportModule("dictDemo");
        PyErr_Print();
        PyObject *strfunc = PyObject_GetAttrString(mymod, "dictFun");
        PyObject *strargs = Py_BuildValue("(O)", d);
        PyErr_Print();
        PyObject *ret = PyEval_CallObject(strfunc, strargs);
        PyErr_Print();
        PyArg_Parse(ret, "i", &globalResult);
        cout << "return value: " << globalResult << "\n";
    }
    if (strcmp( argv[1], "-generate-seq") == 0) {
        runPy();
        PyObject *mymod = PyImport_ImportModule("generateSeq");
        PyErr_Print();
        // PyObject *strfunc = PyObject_GetAttrString(mymod, "run");
		// PyObject *strargs = Py_BuildValue("");
        // PyEval_CallObject(strfunc, strargs);
        PyErr_Print();

    }
    if (strcmp( argv[1], "-create-db") == 0) {
        runPy();
        PyObject *mymod = PyImport_ImportModule("createDb");
        PyErr_Print();
        // PyObject *strfunc = PyObject_GetAttrString(mymod, "run");
		// PyObject *strargs = Py_BuildValue("");
        // PyEval_CallObject(strfunc, strargs);
        PyErr_Print();

    }    
    if (strcmp( argv[1], "-run-websockets") == 0) {
        // based off test 17 in graphics-engine
        runPy();

        PyObject *d = PyDict_New();

        buildTemplateMap();
        buildRouteMap();
        for( auto it = rMap.begin(); it != rMap.end(); ++it ) {
            PyObject *a = Py_BuildValue("s", it->first.c_str());
            PyObject *a_val = Py_BuildValue("s", it->second.c_str());
            PyDict_SetItem(d, a, a_val);
        }


        PyObject *mymod = PyImport_ImportModule("webSocketsServer");
        PyErr_Print();
        PyObject *strfunc = PyObject_GetAttrString(mymod, "run");
		PyObject *strargs = Py_BuildValue("(O)", d);
        PyEval_CallObject(strfunc, strargs);
        PyErr_Print();
    }

    if (strcmp( argv[1], "-test-template") == 0) {
        // cout << "test1\n";
        vector<string> vtr = parseTemplateFile();
        cout << vtr.size() << "\n"; 
        for (int i = 0; i<vtr.size(); i++) {
            cout << vtr[i] << '\n';
            cout << "-- test \n";
        }
    }
    

    return 0;
}