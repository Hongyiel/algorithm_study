#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
using namespace std;

void c_style_tokenizer(string inp, char* delim) {
    // Tokenizes the input string and prints the output
    // It does not return anything, since this is just for
    // illustration
    int temp;
    const char* c_string = inp.c_str();
 
    // Tokenize the C string using the delimiter
    char* token = strtok((char*)c_string, delim);
 
    while (token) {
        temp = atoi(token);
        // Get next token
        cout << temp << endl;

        printf("Token: %s\n", token);

        token = strtok(NULL, delim);
    }
}

int main(int argc, char *argv[]){
    // 
    int matrix_num, times_num;
    int arr[matrix_num][matrix_num];
    // get line first 
    // chop into space 
    // and push in array

    string str;
    getline(cin,str);
    c_style_tokenizer(str, (char*) " ");
    
// srand(time(NULL));
// print array
    //  for (int i = 0; i < matrix_num; i++)
    // {
    //     for (int j = 0; j < matrix_num; j++)
    //     {
            
    //     }
    //     printf("\n");
    // }
// recursive in times
    // for (int i = 0; i < matrix_num; i++){
    //     for (int j = 0; j < matrix_num; j++){
    //             // arr[i][j] = rand()%1001;
    //         while (times_num){
    //             arr[i][j] = arr[i][j] * arr[i][j];
    //             times_num--;
    //         }
    //         div_t output = div(arr[i][j],1001);
    //         printf("%d ",output.rem);
    //     }
    //     printf("\n");
    // }

    return 0;
}