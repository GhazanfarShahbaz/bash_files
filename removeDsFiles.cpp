#include <iostream>
#include <filesystem>
#include <string>

namespace fs = std::filesystem;
using namespace std;

void traverse(fs::path path){
    for (const auto & entry : fs::directory_iterator(path)){
        fs::path current= entry;
        if(fs::is_directory(current)){
            traverse(current);
        }
        else if(current.filename() == ".DS_Store"){
            fs::remove(current);
        }
    }
}


int main(){
    traverse(fs::current_path());
}

