//OBSERVAÇÃO: 'torus' é elemento BABYLON, e 'toro' é recipiente de coordenadas xy.

/*SEÇÃO: DECLARAÇÃO DE VARIÁVEIS IMPORTANTES*/

var matriz_pos = [
    /*Matriz de posição dos toros. Cada número diz respeito a um toro.
    Esta matriz está preenchida com zeros e será posteriormente preenchida
    com outros números.
    */
  [0,0,0,0,0,0,0], //Poste 1
  [0,0,0,0,0,0,0], //Poste 2
  [0,0,0,0,0,0,0]  //Poste 3
];

/* Abaixo: variável que mapeia uma posição da matriz de posição para uma
coordenada cartesiana. Por exemplo: se eu estou no segundo poste e o toro mais
em cima, então as minhas coordenadas são x[1](ou seja, poste 2) e y[0](ou seja,
na primeira posição da matriz_pos de cima pra baixo!)
*/
var coordenadas_possiveis = {x:{0:-6,
                                1:0,
                                2:6},
                             y:{0:2.8,
                                1:2.1,
                                2:1.4,
                                3:0.7,
                                4:0,
                                5:-0.7,
                                6:-1.2}
                            }

// Coordenadas iniciais dos toros, todos no mesmo poste.
for (i = 0; i < qtd; i++){
    toro_atual = 'toro' + (i+1);
    altura = (7 - qtd) + i;
    eval(`${toro_atual} = {x:${coordenadas_possiveis.x[0]}, y:${coordenadas_possiveis.y[altura]}}`)
    // A linha a seguir popula a variável matriz_pos.
    matriz_pos[0][altura] = i+1;
}
// pegando o elemento CANVAS
var canvas = document.getElementById('renderCanvas');

// carregando a engine 3D que importamos do BABYLON
var engine = new BABYLON.Engine(canvas, true);

/*FIM SEÇÃO*/

/* SEÇÃO: MAIN*/

window.addEventListener('DOMContentLoaded', function(){
    // construindo a cena
    var scene = createScene();

    // renderiza o loop para a cena aparecer
    engine.runRenderLoop(function(){
        scene.render();
    });

    //criando um evento para mudar a posição do toro quando o botão de id=muda for clicado
    $("#muda").click(function(){
        de = $("#de_field").val() - 1
        para = $("#para_field").val() - 1
        movimentar_toro(de,para);
        atualizar_coordenadas();
        scene = createScene();
       });

});

/* FIM SEÇÃO */

/* SEÇÃO: FUNÇÕES*/

function movimentar_toro(poste_origem, poste_destino) {
    /*Busca o toro de cima do poste_origem e o posiciona no topo
    do poste_destino. Os postes são 0, 1 e 2!
    Vou criar uma cópia de  matriz_pos.
    */
    var copia = [
      [0,0,0,0,0,0,0], //Poste 1
      [0,0,0,0,0,0,0], //Poste 2
      [0,0,0,0,0,0,0]  //Poste 3
    ];
    for (poste = 0; poste < 3; poste++){
        for (nivel = 0; nivel < 7; nivel++){
            copia[poste][nivel] = matriz_pos[poste][nivel];
        }
    }


    meu_toro = 0;
    //1º: encontrar o toro
    for (i = 0; i < 7; i++){
        if (copia[poste_origem][i] != 0){
            meu_toro = copia[poste_origem][i];
            copia[poste_origem][i] = 0;
            break;
        }
        if (i == 6){
            console.log("Aviso: toro não encontrado. O poste está vazio.");
        }}
    //2º: sua posição final
    if (meu_toro != 0){
        for (i = 0; i < 7; i++){
            if (copia[poste_destino][i] != 0){
                copia[poste_destino][i-1] = meu_toro;
                break;
            }
            if (i == 6){
                copia[poste_destino][i] = meu_toro;
            }}}

    if (estado_atual(copia) != -1){
        // Se a copia da matriz não for uma matriz impossível (com alguma Jogada
        // inválida), então deixaremos a jogada ser efetuada.
        for (poste = 0; poste < 3; poste++){
            for (nivel = 0; nivel < 7; nivel++){
                matriz_pos[poste][nivel] = copia[poste][nivel];
            }}}
}

function atualizar_coordenadas(){
    /*Analisa a matriz de posições e atualiza as coordenadas de cada toro
    encontrado.
    Escolhi usar vários laços ao invés de vários IFs pois é mais organizado.
    */
    for (i = 1; i <= qtd; i++){
        toro_atual = 'toro' + i; //lembrando que toro é a posição, não o BABYLON
        for (poste = 0; poste < 3; poste++){
            for (altura = 0; altura < 7; altura++){
                if (matriz_pos[poste][altura] == i){
                    eval(`${toro_atual}.x = coordenadas_possiveis.x[poste]`);
                    eval(`${toro_atual}.y = coordenadas_possiveis.y[altura]`);
                }}}
    }
}

function logar_matriz_pos(){
    /*Printa no console a variável matriz_pos para fins de debug
    */
    console.log('matriz_pos:')
    for (nivel = 0; nivel < 7; nivel++){
        linha = ''
        for (poste = 0; poste < 3; poste++){
            linha += ' ' + matriz_pos[poste][nivel].toString();
        }
        console.log(linha)
    }
}

function estado_atual(matriz_alvo){
    /*Avalia a situação atual. Recebe a matriz onde será realizada a avaliação,
    que pode ser a matriz_pos mesmo ou ainda uma matriz cópia.
    Retorna:
    1 : Objetivo concluído (vitória)
    0 : Jogo em curso normal
    -1: Jogada inválida realizada
    */
    //Testa -1:
    for (poste = 0; poste < 3; poste++){
        for (nivel = 1; nivel < 7; nivel++){
            if (matriz_alvo[poste][nivel] < matriz_alvo[poste][nivel-1]){
                console.log('Jogada invalida realizada.')
                return -1;
            }}}

    //Testa 1:
    if (matriz_alvo[1][7-qtd] != 0 || matriz_alvo[2][7-qtd] != 0){
        console.log('Fim de jogo!')
        return 1;
    }

    return 0;
}

function createScene(){
    /*Função que constrói a cena
    */
    // criando o objeto-base de cena
    var scene = new BABYLON.Scene(engine);

    // criando a FreeCamera, e setando sua posição para (x:0, y:5, z:-10) é ela que vai dar
    // a perspectiva de onde estaremos olhando os elementos
    var camera = new BABYLON.FreeCamera('camera1', new BABYLON.Vector3(0, 5,-10), scene);

    // direcionando o camera para a origem da cena
    camera.setTarget(BABYLON.Vector3.Zero());

    // criando a iluminação, direcionada para 0,1,0 - que é pra cima
    var light = new BABYLON.HemisphericLight('light1', new BABYLON.Vector3(0,1,-0.5), scene);

    // criando os elementos
    for (i = 1; i <= qtd; i++){
        torus_atual = 'torus' + i;
        tamanho = i / 2;
        eval(`var ${torus_atual} = BABYLON.Mesh.CreateTorus("${torus_atual}", ${tamanho}, 1, 10, scene);`)
    }
    var cylinder = BABYLON.Mesh.CreateCylinder("cylinder", 4, 0.3, 0.3, 6, 1, scene);
    var cylinder2 = BABYLON.Mesh.CreateCylinder("cylinder2", 4, 0.3, 0.3, 6, 1, scene);
    var cylinder3 = BABYLON.Mesh.CreateCylinder("cylinder3", 4, 0.3, 0.3, 6, 1, scene);

    // isso é para mudar a cor, e também podemos usar imagems para ser a textura usando o diffuseTexture
    var materialtorus = new BABYLON.StandardMaterial("texture1", scene);
    for (i = 1; i <= qtd; i++){
        torus_atual = 'torus' + i;
        eval(`${torus_atual}.material = materialtorus;`)
    }
    materialtorus.diffuseColor = new BABYLON.Color3(0.9, 0.29, 0.23);

    //posição dos elementos no eixo X
    for (i = 1; i <= qtd; i++){
        torus_atual = 'torus' + i;
        toro_atual = 'toro' + i;
        eval(`${torus_atual}.position.x = ${toro_atual}.x;`)
    }
    cylinder.position.x = -6;
    cylinder2.position.x = 0;
    cylinder3.position.x = 6;

    // posição dos elementos no eixo Y
    for (i = 1; i <= qtd; i++){
        torus_atual = 'torus' + i;
        toro_atual = 'toro' + i;
        eval(`${torus_atual}.position.y = ${toro_atual}.y;`)
    }
    cylinder.position.y = 1;
    cylinder2.position.y = 1;
    cylinder3.position.y = 1;

    // retorna a cena que criamos
    return scene;
}

/* FIM SEÇÃO */