//Usando Scanner para solicitar ao input um valor
        Scanner tec = new Scanner(System.in);
        
        //Armazenando o tipo de "bixo" em uma variavel String
        String tipo;
        
        //Digitando a quantidade de pernas e armazenando o valor em uma variavel int
        System.out.print("Quantas pernas: ");
        int perna=tec.nextInt();
        
        //Resposta
        System.out.print("Isso é um(a): ");
        
        //Condição usando Switch
        switch(perna){
            case 1:
                tipo="Saci";
                break;
            case 2:
                tipo="Bipede";
                break;
            case 3:
                tipo="Tripé";
                break;
            case 4:
                tipo="Quadrupede";
                break;
            case 6:
                tipo="Aranha";
                break;
            default: //Default seria o ELSE, ou seja um valor padrão caso nenhum das regras acima se cumpre
                tipo="ET";
                break;
        }
        System.out.print(tipo);