#include <stdio.h>
#include <stdlib.h>

#define MEM_SIZE 256
#define NUM_REGS 8

// Definição das instruções
typedef enum {
    ADD, SUB, LOAD, STORE, JMP, HALT
} Instruction;

// Estrutura de uma instrução
typedef struct {
    Instruction instr;
    int reg1;
    int reg2;
    int reg3;
    int address;
} InstructionSet;

// Registradores e memória
int registers[NUM_REGS];
int memory[MEM_SIZE];

// Função para executar as instruções
void execute(InstructionSet *program, int program_size) {
    int pc = 0; // Program Counter
    while (pc < program_size) {
        InstructionSet instr = program[pc];
        switch (instr.instr) {
            case ADD:
                registers[instr.reg1] = registers[instr.reg2] + registers[instr.reg3];
                break;
            case SUB:
                registers[instr.reg1] = registers[instr.reg2] - registers[instr.reg3];
                break;
            case LOAD:
                registers[instr.reg1] = memory[instr.address];
                break;
            case STORE:
                memory[instr.address] = registers[instr.reg1];
                break;
            case JMP:
                pc = instr.address - 1; // -1 porque o pc será incrementado no final do loop
                break;
            case HALT:
                return;
        }
        pc++;
    }
}

int main() {
    // Exemplo de programa em linguagem de montagem
    InstructionSet program[] = {
        {LOAD, 0, 0, 0, 10}, // LOAD R0, 10
        {LOAD, 1, 0, 0, 20}, // LOAD R1, 20
        {ADD, 2, 0, 1, 0},   // ADD R2, R0, R1
        {STORE, 2, 0, 0, 30},// STORE R2, 30
        {HALT, 0, 0, 0, 0}   // HALT
    };

    // Inicializa a memória
    memory[10] = 5;
    memory[20] = 10;

    // Executa o programa
    execute(program, sizeof(program) / sizeof(InstructionSet));

    // Imprime o resultado
    printf("Resultado: %d\n", memory[30]);

    return 0;
}
