
function showExample() {
    const language = document.getElementById('language').value;
    let exampleCode = '';

    switch (language) {
        case 'c':
            exampleCode = `
#include <stdio.h>

int main() {
int number = 10;  
// Variable declaration and initialization
printf("Value of number: %d", number);
return 0;
}
            `;
            break;
        case 'cpp':
            exampleCode = `
#include <iostream>
using namespace std;

int main() {
int number = 10;  
// Variable declaration and initialization
cout << "Value of number: " << number << endl;
return 0;
}
            `;
            break;
        case 'java':
            exampleCode = `
public class Main {
public static void main(String[] args) {
int number = 10;  
// Variable declaration and initialization
System.out.println("Value of number: " + number);
}
}
            `;
            break;
        case 'javascript':
            exampleCode = `
let number = 10; 
// Variable declaration and initialization
console.log("Value of number:", number);
            `;
            break;
        case 'python':
            exampleCode = `
number = 10 
# Variable declaration and initialization
print("Value of number:", number)
            `;
            break;
        default:
            exampleCode = 'Select a programming language.';
    }

    document.getElementById('codeExample').textContent = exampleCode;
    document.getElementById('codeExample').style.display="inline";
}
