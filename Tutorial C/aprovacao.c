#include <stdio.h>

/*
implemente as funções restantes
e o código da função main
*/

#define MAX_ALUNOS 100

float ler_media(int m) {
    int i;
    float media, nota;
    media = 0;
    for (i = 0; i < m; i++) {
        scanf("%f", &nota);
        media += nota;
    }
    media = media / m;
    return media;
}

void ler_notas(float vetor[MAX_ALUNOS], int n, int m) {
    int i; /* índice da posição do vetor */
    for (i = 0; i < n; i++) {
        vetor[i] = ler_media(m);
    }
}

float obter_maximo(float vetor[MAX_ALUNOS], int n) {
    int i;
    float maximo = vetor[0];
    for (i = 0; i < n; i++) {
        if (maximo < vetor[i])
            maximo = vetor[i];
    }
    return maximo;
}

void mutiplicar_fator(float vetor[MAX_ALUNOS], int n, float fator) {
    int i;
    for (i = 0; i < n; i++) {
        vetor[i] = vetor[i] * fator;
    }
}

void imprimir_notas(float P[], float T[], int n) {
    int i;
    float soma, media;

    for (i = 0; i < n; i++) {
        soma = P[i] + T[i];
        media = soma / 2;
        printf("%f\n", media);
    }
}

float obter_media(float vetor[], int n) {
    float soma, media;
    int i;
    for (i = 0; i < n; i++) {
        soma += vetor[i];
    }
    media = soma / n;
    return media;
}

int main() {
    int n;
    float P[MAX_ALUNOS], T[MAX_ALUNOS];
    float maximo_teorica, maximo_pratica, media_pratica, media_teorica;
    scanf("%d", &n);
    ler_notas(P, n, 3);
    ler_notas(T, n, 2);

    mutiplicar_fator(P, n, 1.1);

    maximo_teorica = obter_maximo(T, n);
    mutiplicar_fator(T, n, 10.0/maximo_teorica);

    imprimir_notas(P, T, n);

    maximo_pratica = obter_maximo(P, n);
    maximo_teorica = obter_maximo(T, n);
    media_pratica = obter_media(P, n);
    media_teorica = obter_media(T, n);

    printf("Max P: %.1f\n", maximo_pratica);
    printf("Max T: %.1f\n", maximo_teorica);
    printf("Media P: %.1f\n", media_pratica);
    printf("Media T: %.1f\n", media_teorica/2);
}
