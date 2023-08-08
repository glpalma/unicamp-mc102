#include <stdio.h>
#define elif else if //comando pode ser utilizado para substituir qualquer trecho de código

int main() {
    float num_A, num_B;
    float resultado;
    char operador;
    int n, i;

    scanf("%d", &n);

    for (i = 0; i < n; i++){ 
        printf("Digite a conta: ");
        scanf("%f %c %f", &num_A, &operador, &num_B);
    
        if (operador == '/') {
            if (num_B == 0){printf("Erro: divisão por 0.\n");}
            resultado = num_A / num_B;
            printf("Resultado: %.2f\n", resultado);
        } elif (operador == '+') {
            resultado = num_A + num_B;
            printf("Resultado: %.2f\n", resultado);
        } elif (operador == '-') {
            resultado = num_A - num_B;
            printf("Resultado: %.2f\n", resultado);
        } elif (operador == '*') {
            resultado = num_A * num_B;
            printf("Resultado: %.2f\n", resultado);
        } else {
            printf("Erro: operador não reconhecido.\n");
        }
    }
    return 0;
}