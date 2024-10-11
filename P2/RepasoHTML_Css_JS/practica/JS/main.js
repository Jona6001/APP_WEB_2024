// este es un comentario de una linea

/*
Esto es un comentario 
de varias'
lineas
*/

//alerta 
alert("soy una ventana de alerta")

//Variables 
var nombre='Jonathan';
let nombre2='Edmundo';
let edad=20;
let logica=true;
let estatura=1.85;


//Mostrar en pantalla con WRITE
let concatenacion="La persona: " + nombre + "," + " tiene la edad de: " + edad + " years";
// document.write("<h1>"+concatenacion +"</h1>" + "<br>");
// document.write("  La persona: " + nombre + "," + " tiene la edad de: " + edad + " years");  


//Mostrar en pantalla con el document.getelementbyID
let datos=document.getElementById("info");
datos.innerHTML=`
        <br>
        <br>
        <h1> La persona ${nombre2}, tiene una altura de: ${estatura} </h1>
        <hr>
        <br>
`;

let datos2=document.getElementById("info2");
datos2.innerHTML=`
        <h2> Este es otro contenido </h2> 
        <br> <hr>
`;


//condicionales if

if (estatura>=1.90)
    //document.write("Es una persona alta")
    datos.innerHTML+=` <hr>
    <h3> Es una persona alta </h3> 
    
    `
else 
    document.write(" <h3> Es una estatura promedio </h3> ")

//Ciclos

for(let i=1; i<=5; i++)
        {
                datos.innerHTML+=`<hr><h3>For: El número es: ${i} </h3>`
        }

let i=1;        
while (i<=5)
        {
                i++
                datos.innerHTML+=`<hr><h3>While: El número es: ${i} </h3>`
        }


let j=1;
do {
        j++;
        datos.innerHTML+=`<hr><h3>Do While: El número es: ${i} </h3>`
        
} while (j<=5);


//Funciones

//1.- Que no recibe parametros y no recibe valor
function suma()
{
        let n1=2;
        let n2=4;
        suma=n1+n2;
        console.log("La suma es: "+suma);
        datos.innerHTML+=`<hr> <h3> La suma es: ${suma} </h3>`
}

suma();

//2.- Que no recibe parametros y regresa valor
function suma2()
{
        let n1=2;
        let n2=4;
        suma=n1+n2;
        return suma;
}
let sum=suma2()
datos.innerHTML+=`<hr> <h3> La suma2 es: ${sum} </h3>`


//3.- Que recibe parametros y no regresa valor
function suma3(numero1,numero2)
{
        let n1=numero1;
        let n2=numero2;
        suma=n1+n2;
        datos.innerHTML+=`<hr> <h3> La suma3 es: ${suma} </h3>`
}
suma3(3,4);


//4.- Que reciba parametros y regresa valor
function suma4(numero1,numero2)
{
        let n1=numero1;
        let n2=numero2;
        suma=n1+n2;
       return suma;
}
suma=suma4(8,5)
datos.innerHTML+=`<hr> <h3> La suma4 es: ${suma} </h3>`

//Arreglos

let animales={}
animales[0]="Perico";
animales[1]="Perro";
animales[2]="Gato"

datos.innerHTML+=` <hr> <h3> El mejor amigo del hombres es el: ${animales[1]} </h3> `

animales.forEach(element => {
        datos.innerHTML+=`<hr> <h3> El animal es: ${element} </h3>`
});


// Funciones de flecha

//Funcion normal
function sumaR(a,b)
{
        return a+b
}

datos.innerHTML+=`<hr> <h3> La sumaR es: ${sumaR(3,6)} </h3>`;

const sumaFlecha=(a,b)=>a+b;
datos.innerHTML+=`<hr> <h3> La sumaFlecha es: ${sumaFlecha(3,6)} </h3>`;