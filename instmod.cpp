// install modules for requiments.txt
#include <cstdlib>
#include <iostream>

int main(){
  std::string pipCommand = "pip install -r requirements.txt";
  int x=system(pipCommand.c_str());
  if (x != 0){
    std::cout << "Python is not installed" << std::endl;
    #ifdef _WIN32
      std::string installPythonCommand = "winget install -e --id Python.Python.3";
    #else
      std::string installPythonCommand = "sudo apt-get install python3";
    #endif
      int y = system(installPythonCommand.c_str());
      if (y != 0) {
        std::cout << "Failed to install Python" << std::endl;
        return 1;
      } else {
        std::cout << "Python installed successfully" << std::endl;
        return 0;
      }
      }
      else{
    std::cout << "Packages is installed" << std::endl;
    return 0;
  }
}
