#include<stdio.h>
#include<time.h>
#include<string.h>
#include<assert.h>
#include<stdlib.h>
int pvs(int plose1,int plose2,int slose1,int slose2){
	int m=0,n=0;
	if(plose1==1||slose1==1){
		m=1;
	}
	if(plose2==1||slose2==1){
		n=1;
	}
	if(m==0&&n==1){
		printf("le gagnant est le 1er joueur\n");
		return 1;
	}
	if(m==1&&n==0){
			printf("le gagnant est le 2eme joueur\n");
			return 1;
	}
	if(m==1&&n==1){
		printf("tous sont perdus\n");return 1;
	}
	return 0;
}/*resultat du jugement*/ /*0 est victoire,1 est perdu*/
void svs(char mot1[],char mot2[]){
	int n,m;
	n=strlen(mot1);
	m=strlen(mot2);
	if(n>m){
		printf("le gagnant est le 1er joueur\n");
	}
	else if(n<m){
		printf("le gagnant est le 2eme joueur\n");
	}
	else printf("tous sont les gagnants\n");
}/*determiner la longueur du mot*/
int  jugerdic1(char mot1[],char dic[][50]){
	int i;
	for(i=0;i<50;i++){
	if(strcmp(dic[i],mot1)==0){
	
	return 0;
}
}return 1;
}
int jugerdic2(char mot2[],char dic[][50]){
	int i;
	for(i=0;i<50;i++){
	if(strcmp(dic[i],mot2)==0){
	
	return 0;
}
}return 1;
}/*determinez s'il est dans le dictionnaire*/
int jugerneuf1(char mot1[],char neuf[]){
	char neuf1[9];
	int i;
	for(i=0;i<9;i++){
		neuf1[i]=neuf[i];
	}
	int j,n;
	n=strlen(mot1);
	for(i=0;i<n;i++){
		for(j=0;j<9;j++){
			if(mot1[i]==neuf1[j]){
				neuf1[j]='/';
				break;
			}
			
		}
		if(j==9){
			return 1;
		}
	}
	return 0;
}/*determinez si elle est dans les 9 lettres*/
int jugerneuf2(char mot2[],char neuf[]){
	char neuf2[9];
	int i;
	for(i=0;i<9;i++){
		neuf2[i]=neuf[i];
	}
	int j,n;
	n=strlen(mot2);
	for(i=0;i<n;i++){
		for(j=0;j<9;j++){
			if(mot2[i]==neuf2[j]){
				neuf2[j]='/';
				break;
			}
			
		}
		if(j==9){
			return 1;
		}
	}
	return 0;
}/*determinez si elle est dans les 9 lettres*/
void fscanf1(char mot1[]){
	printf("S'il 1er vous plait entrer votre mot\n");
	scanf("%s",mot1);
}
void fscanf2(char mot2[]){
	printf("S'il 2eme vous plait entrer votre mot\n");
	scanf("%s",mot2);
}
void tprintf(char neuf[]){
	int b;
	for(b=0;b<9;b++){
		if(neuf[b]=='/'){
			break;
		}
		printf("%c ",neuf[b]);
	}
	int i,n=9-b;
	for(i=0;i<n;i++){
		printf("_ ");
	}
	printf("\n");
}
/*afficher le soulignement*/

void tirerConsonne(char neuf[],int i){
 
 
  int n;
  n=rand()%55;
  n++;
 int k[20]={2,2,3,2,2,2,1,1,5,3,6,2,1,6,6,6,2,1,1,1};
 int x,min=0,max=0;
 for(x=0;x<20;x++){
 	max+=k[x];
 	if(min<n&&max>=n){
 		n=x;
 		break;
	}
	min=max;
 }
  switch (n) {
  case 0:{neuf[i]='b';break;}
  case 1:{neuf[i]='c';break;}
  case 2:{neuf[i]='d';break;}
  case 3:{neuf[i]='f';break;}
  case 4:{neuf[i]='g';break;}
  case 5:{neuf[i]='h';break;}
  case 6:{neuf[i]='j';break;}
  case 7:{neuf[i]='k';break;}
  case 8:{neuf[i]='l';break;}
  case 9:{neuf[i]='m';break;}
  case 10:{neuf[i]='n';break;}
  case 11:{neuf[i]='p';break;}
  case 12:{neuf[i]='q';break;}
  case 13:{neuf[i]='r';break;}
  case 14:{neuf[i]='s';break;}
  case 15:{neuf[i]='t';break;}
  case 16:{neuf[i]='v';break;}
  case 17:{neuf[i]='w';break;}
  case 18:{neuf[i]='x';break;}
  case 19:{neuf[i]='z';break;}
 
  }
  tprintf(neuf);
}
/*consonnes*/



void tirerVoyelle(char neuf[],int i){
    int m;
   
 
    m=rand()%45;
    if(m<9){
    	m=0;
	}
	if(m>=9&&m<24){
		m=1;
	}
	if(m>=24&&m<32){
		m=2;
	}
	if(m>=32&&m<38){
		m=3;
	}
	if(m>=38&&m<44){
		m=4;
	}
	if(m>=44&&m<45){
		m=5;
	}
    switch (m){
        case 0:{neuf[i]='a';}break;
        case 1:{neuf[i]='e';}break;
        case 2:{neuf[i]='i';}break;
        case 3:{neuf[i]='o';}break;
        case 4:{neuf[i]='u';}break;
        case 5:{neuf[i]='y';}break;
       
    }
tprintf(neuf);
}

/*voyelles*/




void select1(char neuf[],int i,char t){

	
	if(t=='v'){
		tirerVoyelle(neuf,i);
		
	}else{
		if(t=='c'){
			tirerConsonne(neuf,i);
		}else {
			printf("error\n");
		}
	}
	
}


/*eviter une saisie incorrecte des lettres*/



int main(){
	srand(time(NULL));
	char p[10];
	char a[10];
char dic[][50]={"ee","a","bien","bleu","continuer","comme",
"dans","document","etudiant","ecole","faire","gravement","gris","heure",
"hero","il","iteration","justement","jungle","kilometre","kilo","lendemain","loisir",
"madame","messieurs","nous","niece","occasion","orange","pour",
"pres","quoi","quelle","reunion","revision","sourire","sous","terre",
"termine","unique","un","vrai","vacances","weekend","wagon","yaourt","zero","zoo","voisin","facon"};

/*dictionnaire*/

int i;
char t;
char ch;

char neuf[9];
for(i=0;i<9;i++){
	neuf[i]='/';
}
for(i=0;i<9;i++){
		printf("la joueur tire une lettre : voyelle ou consonne? (v/c)\n ");
	loop:
scanf("%c",&a[i]);
scanf("%c",&p[i]);
if(a[i]!='v'&&a[i]!='c'){
	printf("Le format que vous avez entre est incorrect,veuillez refinir a nouveau.\n");
		while((ch = getchar()) != '\n' && ch != EOF);
	goto loop;
}
	t=a[i];
	select1(neuf,i,t);
	
}
int plose1,plose2,slose1,slose2;


char mot1[10],mot2[10];

fscanf1(mot1);
fscanf2(mot2);
plose1=jugerneuf1(mot1,neuf);
plose2=jugerneuf2(mot2,neuf);

slose1=jugerdic1(mot1,dic);
slose2=jugerdic2(mot2,dic);
int result;
result=pvs(plose1,plose2,slose1,slose2);
if(result==0){
	svs(mot1,mot2);
}
	return 0;
}
