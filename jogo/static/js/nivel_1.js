 var horizontal= -6;
        var vertical = 0;
        window.addEventListener('DOMContentLoaded', function(){
            // pegando o elemento CANVAS
            var canvas = document.getElementById('renderCanvas');

            // carregando a engine 3D que importamos do BABYLON
            var engine = new BABYLON.Engine(canvas, true);

            // função createScene que constrói a cena
            var createScene = function(){
                // criando o objeto-base de cena
                var scene = new BABYLON.Scene(engine);

                // criando a FreeCamera, e setando sua posição para (x:0, y:5, z:-10) é ela que vai dar
                // a perspectiva de onde estaremos olhando os elementos
                var camera = new BABYLON.FreeCamera('camera1', new BABYLON.Vector3(0, 5,-10), scene);

                // direcionando o camera para a origem da cena
                camera.setTarget(BABYLON.Vector3.Zero());

                // criando a iluminação, direcionada para 0,1,0 - que é pra cima
                var light = new BABYLON.HemisphericLight('light1', new BABYLON.Vector3(0,1,0), scene);

                // criando os elementos
                var torus = BABYLON.Mesh.CreateTorus("torus", 1, 1, 10, scene);
                var torus2 = BABYLON.Mesh.CreateTorus("torus2", 2, 1, 10, scene);
                var torus3 = BABYLON.Mesh.CreateTorus("torus3", 3, 1, 10, scene);
                var cylinder = BABYLON.Mesh.CreateCylinder("cylinder", 4, 0.3, 0.3, 6, 1, scene);
                var cylinder2 = BABYLON.Mesh.CreateCylinder("cylinder2", 4, 0.3, 0.3, 6, 1, scene);
                var cylinder3 = BABYLON.Mesh.CreateCylinder("cylinder3", 4, 0.3, 0.3, 6, 1, scene);

                // isso é para mudar a cor, e também podemos usar imagems para ser a textura usando o diffuseTexture
                var materialtorus = new BABYLON.StandardMaterial("texture1", scene);
                torus.material = materialtorus;
                torus2.material = materialtorus;
                torus3.material = materialtorus;
                materialtorus.diffuseColor = new BABYLON.Color3(1.0, 0.2, 0.7);

                // posição dos elementos no eixo Y
                torus.position.y = vertical;
                torus2.position.y= -0.5;
                torus3.position.y= -1;
                cylinder.position.y = 1;
                cylinder2.position.y = 1;
                cylinder2.position.y = 1;

                //posição dos elementos no eixo X
                torus.position.x = horizontal;
                torus2.position.x= -6;
                torus3.position.x= -6;
                cylinder.position.x = -6;
                cylinder2.position.x = 0;
                cylinder3.position.x = 6;

                // retorna a cena que criamos
                return scene;
            }
            var scene = createScene();

            //criando um evento para mudar a posição do toro quando o botão de id=muda for clicado
            $("#muda").click(function(){

                if (vertical > -1){
                    horizontal=horizontal+6;
                    vertical=vertical-1;}
                else{
                    horizontal = horizontal -6;
                    vertical = vertical+1;}
                scene = createScene();

               });

            // renderiza o loop para a cena aparecer
            engine.runRenderLoop(function(){
                scene.render();
            });

        });

