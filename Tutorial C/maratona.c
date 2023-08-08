#include <stdio.h>

int main() {
    int i, n, duracao, limite, maximo;
    int velocidades[100];

    scanf("%d", &n);

    /* guardamos as velocidades */
    for (i = 0; i < n; i++) {
        scanf("%d", &velocidades[i]);
    }

    scanf("%d", &duracao);

    if (duracao == 1) {
      limite = 100;
    } else if (duracao == 2) {
      limite = 20;
    } else {
      limite = 10;
    }
    maximo = 0;

    for (i = 0; i < n; i++) {
      if (velocidades[i] > maximo && velocidades[i] <= limite) {
        maximo = velocidades[i];
      }
    }
    printf("%d", maximo);
}
