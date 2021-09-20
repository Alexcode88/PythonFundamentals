

function changeValue( obj ){
    obj.extra = "Extra value"
}

let x = {
    one : 1,
    two : 2
};

changeValue( x )

console.log( x );