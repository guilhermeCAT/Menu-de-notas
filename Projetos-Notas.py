alunos1= [[], []] 
i = 0 

def main():
    while True:
        print('-' * 20)
        print('Menu Interativo')
        print('-' * 20)
        print()
        print('Opções:')
        print('[1] Lançar Notas')
        print('[2] Lista de Aprovados')
        print('[3] Lista de Reprovados')
        
        resposta = input('Sua Opção: ')
        resposta = int(resposta)

        if resposta == 1:
            alunos = input('Digite o nome do aluno:')
            matricula = input('digite sua matricula: ')
            av1 = input('Digite a nota da avaliação 1:')
            av2 = input('Digite a nota da avaliação 2:')
            av3 = input('Digite a nota da avaliação 3:')
            av1 = int(av1)
            av2 = int(av2)
            av3 = int(av3)
            matricula = int(matricula)

            somaNotas = (av1 + av2 + av3)
            media = somaNotas/3
            if media >= 7:
                alunos1[0].append([alunos,matricula ,media])
            else:
                alunos1[1].append([alunos,matricula ,media])

        elif resposta == 2:
          print(f'Alunos Aprovado')
          print(f'{"No.":<4}{"NOME":<10}{"Matricula":>10}{"MEDIA":>8}')
          print('-' * 26)
          for n, a, in enumerate(alunos1[0]):
            print(f'{n:<4}{a[0]:<10}{a[1]:>10}{a[2]:>8.1f}')
            

        elif resposta == 3:
            print(f'Alunos Reprovado')
            print(f'{"No.":<4}{"NOME":<10}{"Matricula":>10}{"MEDIA":>8}')
            print('-' * 26)
            for n, a, in enumerate(alunos1[1]):
                print(f'{n:<4}{a[0]:<10}{a[1]:>10}{a[2]:>8.1f}')
                break

        else:
            print('Opção invalida')

main()          

        


            

                


