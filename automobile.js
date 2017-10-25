function Automobile(year, make, model, type) {
    this.year = year; //integer (ex. 2001, 1995)
    this.make = make; //string (ex. Honda, Ford)
    this.model = model; //string (ex. Accord, Focus)
    this.type = type; //string (ex. Pickup, SUV)
    this.logMe = function(boolArg) {
        if (boolArg) { console.log(this.year + ' ' + this.make + ' ' + this.model + ' ' + this.type); }
        else { console.log(this.year + ' ' + this.make + ' ' + this.model); }
    };
}

var automobiles = [
    new Automobile(1995, "Honda", "Accord", "Sedan"),
    new Automobile(1990, "Ford", "F-150", "Pickup"),
    new Automobile(2000, "GMC", "Tahoe", "SUV"),
    new Automobile(2010, "Toyota", "Tacoma", "Pickup"),
    new Automobile(2005, "Lotus", "Elise", "Roadster"),
    new Automobile(2008, "Subaru", "Outback", "Wagon")
];

/*Return sorted object array using arbitrary comparitor*/
function sortArr(comparator, array) {
    var tempArr = array; var base; var temp;
        for (var i = 0; i < tempArr.length - 1; i++) {
            base = i;
            for (var j = i + 1; j < tempArr.length; j++) {
                var comp = comparator(tempArr[j], tempArr[base]);
                if (comp) {base = j;}
        }
        if (base !== i) {
            temp = tempArr[i];
            tempArr[i] = tempArr[base];
            tempArr[base] = temp;
        }
    }
    return tempArr;
}

/*Compare two automobiles numerically by year*/
function yearComparator(auto1, auto2) {
    return auto1.year > auto2.year;
}

/*Compare two automobiles alphabetically by make.*/
function makeComparator(auto1, auto2) {
    var auto1make = auto1.make.charAt(0).toLowerCase();
    var auto2make = auto2.make.charAt(0).toLowerCase();
    return auto1make < auto2make;
}

/*Compare two automobiles by type.*/
function typeComparator(auto1, auto2) {
    var autoType = function(auto) {
        switch (auto.type.toLowerCase()) {
          case "roadster": return 4;
          case "pickup": return 3;
          case "suv": return 2;
          case "wagon": return 1;
          default: return 0;
        }
    }
    /*Compare by year if types match*/
    if (autoType(auto1) == autoType(auto2)) {return yearComparator(auto1, auto2);}
    else return (autoType(auto1) > autoType(auto2));
}

/*Array loop for output*/
function printArr(array, boolType) {
    for (var i = 0; i < array.length; i++) {
    array[i].logMe(boolType);
    }
}

console.log("*****");
console.log("The cars sorted by year are: ");
printArr(sortArr(yearComparator, automobiles), false);
console.log('\n');

console.log("The cars sorted by make are: ");
printArr(sortArr(makeComparator, automobiles), false);
console.log('\n');

console.log("The cars sorted by type are: ");
printArr(sortArr(typeComparator, automobiles), true);
console.log("*****");