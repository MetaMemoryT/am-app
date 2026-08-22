vector<string> parseTemplateFile() {
    string line;
    string t2 = "";
    ifstream myfile("/Users/seanusick/p/am-app/src/templates.txt");
    vector<string> vtr;
    while ( getline (myfile,line) ) {
        // cout << "test2";
        // cout << line;
        if (line == "--") {
            vtr.push_back(t2);
            t2 = "";
        } else {
            if (t2 == "") {
                t2 += line;
            } else {
                t2 += '\n' + line;
            }
            
        }
    }
    vtr.push_back(t2);

    return vtr;
}

void buildTemplateMap() {
    // gives templates names
    vector<string> vtr = parseTemplateFile();
    tMap["page1"] = vtr[0];
    tMap["page2"] = vtr[1];
    tMap["webSocketsHelloWorld"] = vtr[2];
    tMap["loginForm"] = vtr[3];
    tMap["home"] = vtr[4];
    tMap["registerForm"] = vtr[5];
    tMap["editNameForm"] = vtr[6];
    tMap["deposit"] = vtr[7];
    tMap["grabOrder"] = vtr[8];
    tMap["tests"] = vtr[9];
    tMap["testImage"] = vtr[10];
    tMap["testMoney"] = vtr[11];
    tMap["verifyNameWithDrivers"] = vtr[12];
    tMap["addFriend"] = vtr[13];
    tMap["glassCrusher"] = vtr[14];
    tMap["amazonPurchases"] = vtr[15];
    tMap["creditLinePayments"] = vtr[16];
    tMap["gedExamSubjects"] = vtr[17];
    tMap["mathematics"] = vtr[18];
    tMap["login"] = "the login dialog 3";
    tMap["homeTitle"] = "Affiliate Marketing Ecommerce Order Grab App <br>";
    tMap["homeInformation"] = "Welcome to AME platform... Click here to begin tutorial. <br>";
    tMap["bottomIcons"] = "home / Grab order / withdraw / settings";
    tMap["logoutLink"] = "<a href='/login'>logout</a>";

    tMap["homeTotal"] = tMap["home"] + tMap["homeTitle"] +
                            tMap["homeInformation"] + tMap["logoutLink"];

}

void buildRouteMap() {
    // maps routes to templates
    rMap[""] = tMap["homeTotal"];
    rMap["page1"] = tMap["page1"];
    rMap["page2"] = tMap["page2"];
    rMap["login"] = tMap["loginForm"];
    rMap["webSocketsHelloWorld"] = tMap["webSocketsHelloWorld"];
    rMap["register"] = tMap["registerForm"];
    rMap["editName"] = tMap["editNameForm"];
    rMap["deposit"] = tMap["deposit"];
    rMap["grabOrder"] = tMap["grabOrder"];
    rMap["tests"] = tMap["tests"];
    rMap["testImage"] = tMap["testImage"];
    rMap["testMoney"] = tMap["testMoney"];
    rMap["verifyNameWithDrivers"] = tMap["verifyNameWithDrivers"];
    rMap["addFriend"] = tMap["addFriend"];
    rMap["glassCrusher"] = tMap["glassCrusher"];
    rMap["amazonPurchases"] = tMap["amazonPurchases"];
    rMap["creditLinePayments"] = tMap["creditLinePayments"];
    rMap["gedExamSubjects"] = tMap["gedExamSubjects"];
    rMap["mathematics"] = tMap["mathematics"];
}