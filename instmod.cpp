// install modules for requiments.txt
#include <cstdlib>
#include <iostream>

int main(){
  std::string pipCommand = "pip install -r requirements.txt";
  int x=system(pipCommand.c_str());
  if (x != 0){
    std::cout << "Python is not installed" << std::endl;
  }
  else{
    std::cout << "Packages is installed" << std::endl;
  }
  return 0;
}
