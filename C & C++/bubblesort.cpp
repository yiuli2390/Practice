#include<iostream>
using namespace std;

int bubblesort(int A[], int N) {
	int sw = 0, i, j;
	bool flag = 1;
	for (i = 0; flag; i++)
	{
		flag = 0;
		for (j = N-1; j>=i+1; j--) {
			if(A[j] < A[j-1]){
                swap(A[j], A[j-1]);
                flag = 1;
                sw++;
			}
		}
	}
	return sw;
}

int main() {
	int N, sw;
	int A[100];

	cin >> N;
	for (int i = 0; i < N; i++) cin >> A[i];

	sw = bubblesort(A, N);

	for(int j = 0; j < N; j++){
        if(j) cout << " ";
        cout << A[j];
	}
	cout << endl;
	cout << sw << endl;

	return 0;
}
