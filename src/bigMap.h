#include <string>
#include <map>
#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>

using namespace std;

map<string, string> tMap;
map<string, string> rMap;
vector<string> parseTemplateFile();
void buildTemplateMap();
void buildRouteMap();