#include<iostream>
using namespace std;

struct Card{
	char suit,
	value;
};

void bubble(struct Card A[], int N){
	for (int i = 0; i < N; ++i)
	{
		for (int j = N-1; j >=i+1; ++j)
		{
			if (A[j].value < A[j-1].value)
			{
				Card t = A[j];
				A[j] = A[j-1];
				A[j-1] = t;
			}
		}
	}
}

void selection(struct Card A[], int N){
	for (int i = 0; i < N; ++i)
	{
		/* code */
		int minj = i;
		for (int j = i; j < N; ++j)
		{
			/* code */
			if(A[j].value < A[minj].value) minj=j;
		}
		Card t = A[i];
		A[i] = A[minj];
		A[minj] = t;
	}
}


void print(struct Card A[], int N){
	for (int i = 0; i < N; ++i)
	{
		/* code */
		if(i>0) cout<<" ";
		cout << A[i].suit << A[i].value;
	}
	cout<<endl;
}

bool isStable(struct Card c1[], struct Card c2[], int N){
    for(int i=0; i<N; i++){
        if(c1[i].suit != c2[i].suit) return false;
    }
    return true;
}

int main(){
	Card c1[100], c2[100];
	int N;
	char ch;

	cin>>N;
	for (int i = 0; i < N; i++)
	{
		/* code */
		cin>>c1[i].suit>>c1[i].value;
	}

	for (int i = 0; i < N; i++) c2[i]=c1[i];

	bubble(c1,N);
	selection(c2,N);

	print(c1,N);
	cout<<"stable"<<endl;
	print(c2,N);
	if(isStable(c1,c2,N)){
		cout<<"Stable"<<endl;
	} else {
		cout<<"Not stable"<<endl;
	}

	return 0;
}
