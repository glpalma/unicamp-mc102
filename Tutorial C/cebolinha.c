#include <stdio.h>
#include <string.h>

#define MAX_PALAVRA 20

int comprimento_str(char string[]) {
    int comprimento = 0;
    while (string[comprimento] != '\0') {
        comprimento += 1;
    }
    return comprimento;
}

void cebolinha(char palavra[MAX_PALAVRA], char palavra_cebolinha[MAX_PALAVRA]) {
    int i, anterior_eh_R = 0, contador = 0;
    int n = comprimento_str(palavra);
    char letra;

    for (i = 0; i < n; i++) {
        letra = palavra[i];
        if (letra == 'R') {
            if (!(anterior_eh_R)) {
                letra = 'L';
            } else {
                contador++;
                continue;
            }
            anterior_eh_R = 1;
        } else {
            anterior_eh_R = 0;
        }
        palavra_cebolinha[i - contador] = letra;
        /*printf("%d %c %d\n", i, letra, anterior_eh_R);*/
    }
}

void copiar_inverso(char palavra[], char inverso[]) {
    int i, j;
    i = comprimento_str(palavra) - 1;  /* índice da última letra de palavra */
    j = 0;                             /* índice da primeira posição de inverso */
    while (i >= 0) {
        /* copia a i-ésima letra de palavra para a j-ésima posição de inverso */
        inverso[j] = palavra[i];
        i = i - 1;
        j = j + 1;
    }
    /* adicionamos o '\0' para indicar que a string inverso terminou */
    inverso[j] = '\0';
}

int main() {
    char palavra[MAX_PALAVRA], palavra_cebo[MAX_PALAVRA];
    scanf("%s", palavra);
    cebolinha(palavra, palavra_cebo);
    printf("%s\n", palavra_cebo);
}
