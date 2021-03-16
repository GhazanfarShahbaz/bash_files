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

void traverse(fs::path path,  std::unordered_set<std::string> uselessExtensions,  std::unordered_set<std::string> uselessFiles, std::unordered_set<std::string> uselessFolders ){
    for (const auto & entry : fs::directory_iterator(path)){
        fs::path current= entry;
        if(fs::is_directory(current)){
            if(uselessFolders.count(current.filename())){
                fs::remove_all(string(path) + "/" + string(current.filename()));
            }
            else{
                traverse(current, uselessExtensions ,uselessFiles, uselessFolders);
            }
        }
        else if(uselessFiles.count(current.filename()) or extension(current.filename(), uselessExtensions)){
            fs::remove(string(path) + "/" + string(current.filename()));
        }
    }
}


int main(){
    std::unordered_set<std::string> uselessFiles = {".DS_Store", "a.out"};
    std::unordered_set<std::string>  uselessExtensions = {"aux", "ldb_matexmk", "fls", "log", "synctex.gz", "fdb_latexmk"};
    std::unordered_set<std::string> uselessFolders = {"__pycache__"};

    traverse(fs::current_path(), uselessExtensions ,uselessFiles, uselessFolders);
}

