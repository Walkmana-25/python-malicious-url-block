#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

bool comment(const std::string& s){
    if(s.at(0) == '#'){
        return true;
    }else{
        return false;
    }
}


bool search(const std::string& target, const std::string& path){
    std::ifstream file(path);
    std::string line;
    std::vector<std::string> source;

    while (std::getline(file, line)){
        if(comment(line) == false){
            source.push_back(line);
        }

    }

    if(std::binary_search(source.begin(), source.end(), target)){
        return true;
    }else{
        return false;
    }



}

int main(){
    std::string input, path;
    std::cin >> input >> path;
    if(search(input, path)){
        std::cout << "Yes" << std::endl;
    }else{
        std::cout << "No" << std::endl;
    }
    return 0;
}

PYBIND11_MODULE(_utils, m){
    m.def("search", &search, "A function that discrimination url is in list");
}
