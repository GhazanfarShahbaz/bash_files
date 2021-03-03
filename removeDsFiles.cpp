#include <iostream>
#include <filesystem>
#include <string>
#include <unordered_set>

namespace fs = std::__fs::filesystem;
using namespace std;

bool extension(std::string fileName, std::unordered_set<std::string> uselessExtensions ){
    int index = fileName.find(".");
    return (index >= 0 and uselessExtensions.count(fileName.substr(index+1)) == 1) ? true : false;
    
}

void traverse(fs::path path,  std::unordered_set<std::string> uselessExtensions,  std::unordered_set<std::string> uselessFiles ){
    for (const auto & entry : fs::directory_iterator(path)){
        fs::path current= entry;
        if(fs::is_directory(current)){
            traverse(current, uselessExtensions ,uselessFiles);
        }
        else if(uselessFiles.count(current.filename()) or extension(current.filename(), uselessExtensions)){
            fs::remove(string(path) + "/" + string(current.filename()));
        }
    }
}


int main(){
    std::unordered_set<std::string> uselessFiles = {".DS_Store", "a.out"};
    std::unordered_set<std::string>  uselessExtensions = {"aux", "ldb_matexmk", "fls", "log", "synctex.gz"};

    traverse(fs::current_path(), uselessExtensions ,uselessFiles);
}

