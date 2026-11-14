#define PY_SSIZE_T_CLEAN
// Name of program mainreturn.cpp
#include <iostream>
#include <Python.h>
#include <string>
#include "bigMap.h"
#include "bigMap.cpp"

using namespace std;
  
int runPy(char** argv) {
    PyStatus status;
    PyConfig config;
    
    // 1. Initialize default Python configuration
    PyConfig_InitPythonConfig(&config);
    
    // 2. Set program name (optional, but good practice)
    status = PyConfig_SetBytesString(&config, &config.program_name, argv[0]);
    if (PyStatus_Exception(status)) {
        PyConfig_Clear(&config);
        return 1;
    }
    
    // 3. Read the default configuration
    status = PyConfig_Read(&config);
    if (PyStatus_Exception(status)) {
        PyConfig_Clear(&config);
        return 1;
    }
    
    // 4. Override / set custom module search paths (sys.path)
    config.module_search_paths_set = 1; // Tell Python we are defining sys.path manually
    
    // Clear existing paths if you want a completely isolated path list,
    // or use PyWideStringList_Append to add paths
    status = PyWideStringList_Append(&config.module_search_paths, L"/usr/lib/python3.13/");
    if (PyStatus_Exception(status)) {
        PyConfig_Clear(&config);
        return 1;
    }

    status = PyWideStringList_Append(&config.module_search_paths, L"/usr/lib/python3.13/lib-dynload/");
    if (PyStatus_Exception(status)) {
        PyConfig_Clear(&config);
        return 1;
    }


    status = PyWideStringList_Append(&config.module_search_paths, L"/home/vboxuser/p/am-app/src/app/");
    if (PyStatus_Exception(status)) {
        PyConfig_Clear(&config);
        return 1;
    }

    // 5. Initialize Python with the custom configuration
    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        PyConfig_Clear(&config);
        return 1;
    }
    
    PyConfig_Clear(&config);

    // Run Python code or embedded logic here...
    return 0;


    /*
	if (PyImport_AppendInittab("low", PyInit_lowModule) == -1) {
        fprintf(stderr, "Error: could not extend in-built modules table\n");
        exit(1);
    }
    */
    // Py_SetPath(L"/Users/seanusick/p/python-embed/libs/cpython/Lib:/Users/seanusick/p/python-embed/libs/cpython/build/lib.macosx-11.5-x86_64-3.10:/Volumes/t3/am-app/src/app");


    /*
    Py_SetPath(L"/Users/seanusick/p/python-embed/libs/cpython/Lib:/Users/seanusick/p/python-embed/libs/cpython/build/lib.macosx-11.5-x86_64-3.10:/Users/seanusick/p/am-app/src/app");
    Py_SetPythonHome(L"/Users/seanusick/p/python-embed/libs/cpython/Lib:/Users/seanusick/p/python-embed/libs/cpython/build/lib.macosx-11.5-x86_64-3.10");

    if (!Py_IsInitialized()) {
        Py_Initialize();
    }
	
    if (!Py_IsInitialized()) {
        printf("Failed to initialize python interpreter.");
    }
    */
}

// prints the python error and exits instead of segfaulting on a NULL result
PyObject* check(PyObject *obj) {
    if (obj == NULL) {
        PyErr_Print();
        exit(1);
    }
    return obj;
}

int main(int argc, char** argv)
{
    if (argc < 2) {
        cout << "usage: " << argv[0] << " <command>" << "\n";
        return 1;
    }

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
        runPy(argv);
        PyObject *mymod = check(PyImport_ImportModule("simple"));
        PyObject *strfunc = check(PyObject_GetAttrString(mymod, "fun1"));
        PyObject *strargs = Py_BuildValue("si", "abc3", 4);
        PyObject *ret = check(PyObject_CallObject(strfunc, strargs));
        PyArg_Parse(ret, "i", &globalResult);
        cout << globalResult << "\n";
    }

    if (strcmp( argv[1], "-run-dict") == 0) {
        runPy(argv);
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

        PyObject *mymod = check(PyImport_ImportModule("dictDemo"));
        PyErr_Print();
        PyObject *strfunc = check(PyObject_GetAttrString(mymod, "dictFun"));
        PyObject *strargs = Py_BuildValue("(O)", d);
        PyErr_Print();
        PyObject *ret = check(PyObject_CallObject(strfunc, strargs));
        PyErr_Print();
        PyArg_Parse(ret, "i", &globalResult);
        cout << "return value: " << globalResult << "\n";
    }
    if (strcmp( argv[1], "-generate-seq") == 0) {
        runPy(argv);
        PyObject *mymod = check(PyImport_ImportModule("generateSeq"));
        PyErr_Print();
        PyObject *strfunc = check(PyObject_GetAttrString(mymod, "run"));
		PyObject *strargs = Py_BuildValue("()");
        check(PyObject_CallObject(strfunc, strargs));
        PyErr_Print();
        // Py_Finalize();

    }
    if (strcmp( argv[1], "-create-db") == 0) {
        runPy(argv);
        PyObject *mymod = check(PyImport_ImportModule("createDb"));
        PyErr_Print();
        // PyObject *strfunc = PyObject_GetAttrString(mymod, "run");
		// PyObject *strargs = Py_BuildValue("");
        // PyObject_CallObject(strfunc, strargs);
        PyErr_Print();

    }
    if (strcmp( argv[1], "-run-test-dict") == 0) {
        // based off test 17 in graphics-engine
        runPy(argv);

        PyObject *d = PyDict_New();

        buildTemplateMap();
        buildRouteMap();
        for( auto it = rMap.begin(); it != rMap.end(); ++it ) {
            PyObject *a = Py_BuildValue("s", it->first.c_str());
            PyObject *a_val = Py_BuildValue("s", it->second.c_str());
            cout << it->first.c_str();
            PyDict_SetItem(d, a, a_val);
        }
    }    
    if (strcmp( argv[1], "-run-websockets") == 0) {
        // based off test 17 in graphics-engine
        runPy(argv);

        PyObject *d = PyDict_New();

        buildTemplateMap();
        buildRouteMap();
        for( auto it = rMap.begin(); it != rMap.end(); ++it ) {
            PyObject *a = Py_BuildValue("s", it->first.c_str());
            PyObject *a_val = Py_BuildValue("s", it->second.c_str());
            PyDict_SetItem(d, a, a_val);
        }


        PyObject *mymod = check(PyImport_ImportModule("webSocketsServer"));
        PyErr_Print();
        PyObject *strfunc = check(PyObject_GetAttrString(mymod, "run"));
		PyObject *strargs = Py_BuildValue("(O)", d);
        check(PyObject_CallObject(strfunc, strargs));
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