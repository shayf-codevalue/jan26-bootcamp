#include <iostream>

int main()
{
    int N=20;
    int i=2;
    int tmp=0;
    bool p=true;
    while(i<N){
	    for(int k=2;k<i;k++){
		    if(i%k==0){
			    p=false;
		    }
	    }
	    if(p==true){
		    std:std::cout << i << std::endl;
	    }
	    i++;
	    p=true;
    }
}