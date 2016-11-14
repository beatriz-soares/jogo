 var horizontal= -6;
        var vertical = 0;
        window.addEventListener('DOMContentLoaded', function(){
            // get the canvas DOM element
            var canvas = document.getElementById('renderCanvas');

            // load the 3D engine
            var engine = new BABYLON.Engine(canvas, true);

            // createScene function that creates and return the scene
            var createScene = function(){
                // create a basic BJS Scene object
                var scene = new BABYLON.Scene(engine);

                // create a FreeCamera, and set its position to (x:0, y:5, z:-10)
                var camera = new BABYLON.FreeCamera('camera1', new BABYLON.Vector3(0, 5,-10), scene);

                // target the camera to scene origin
                camera.setTarget(BABYLON.Vector3.Zero());

                // create a basic light, aiming 0,1,0 - meaning, to the sky
                var light = new BABYLON.HemisphericLight('light1', new BABYLON.Vector3(0,1,0), scene);

                // criando os elementos
                var torus = BABYLON.Mesh.CreateTorus("torus", 1, 1, 10, scene);
                var torus2 = BABYLON.Mesh.CreateTorus("torus2", 2, 1, 10, scene);
                var torus3 = BABYLON.Mesh.CreateTorus("torus3", 3, 1, 10, scene);
                var cylinder = BABYLON.Mesh.CreateCylinder("cylinder", 4, 0.3, 0.3, 6, 1, scene);
                var cylinder2 = BABYLON.Mesh.CreateCylinder("cylinder2", 4, 0.3, 0.3, 6, 1, scene);
                var cylinder3 = BABYLON.Mesh.CreateCylinder("cylinder3", 4, 0.3, 0.3, 6, 1, scene);


                var materialtorus = new BABYLON.StandardMaterial("texture1", scene);
                torus2.material = materialtorus;
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

                // return the created scene
                return scene;
            }
            var scene = createScene();
            $("#muda").click(function(){

                if (vertical > -1){
                    horizontal=horizontal+6;
                    vertical=vertical-1;}
                else{
                    horizontal = horizontal -6;
                    vertical = vertical+1;}
                scene = createScene();

               });


            // run the render loop
            engine.runRenderLoop(function(){
                scene.render();
            });

        });

