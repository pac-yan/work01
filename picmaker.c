#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>


int main(){
   int fd = open("pic.ppm", O_WRONLY | O_TRUNC | O_CREAT, 0644);
   int height = 500;
   int width = 500;
   
}
