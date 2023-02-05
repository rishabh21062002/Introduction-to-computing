/* Rishabh 21105114 ECE */
#include <iostream>
#include <stack>
using namespace std;

void reverseStack(stack<int> &input, stack<int> &extra) {
    //Write your code here
    if(input.size()==0){
        return;
    }
    int r = input.top();
    input.pop();
    reverseStack(input,extra);
    while( !input.empty() ){
        int a = input.top();
        input.pop();
        extra.push(a);
    }
    input.push(r);
    while(!extra.empty()){
        int b = extra.top();
        extra.pop();
        input.push(b);

    }
}

int main() {
    stack<int> input, extra;
    int size;
    cin >> size;

    for (int i = 0, val; i < size; i++) {
        cin >> val;
        input.push(val);
    }

    reverseStack(input, extra);

    while (!input.empty()) {
        cout << input.top() << " ";
        input.pop();
    }
}
