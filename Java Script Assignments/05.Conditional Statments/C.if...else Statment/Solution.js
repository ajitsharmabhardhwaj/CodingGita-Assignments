// Question-1
let month = 5
if (month == 12 || month == 1 || month == 2){
    console.log("Winter")
}else if (month == 3 || month == 4 || month == 5){
    console.log("Summer")
}else if (month == 6 || month == 7 || month == 8){
    console.log("Monsoon")
}else{
    console.log("Autumn")
}

// Question-2
let tax = 1200000
if (tax<300000){
    console.log("no tax")
}else if(tax<700000){
    console.log("5% tax")
}else if (tax<1000000){
    console.log("10% tax")
}else{
    console.log("15% tax")
}

// Question-3
let height = 190;
if (height<150){
    console.log("Short")
}else if(height<170){
    console.log("Average")
}else{
    console.log("Tall")
}
 
// Question-4
let num = -25
if (num>0){
    if(num%2==0){
        console.log("Positive Even")
    }else{
        console.log("Positive Odd")
    }
}else if(num==0){
    console.log("Zero")
}else{
    if(num%2==0){
        console.log("Negitive Even")
    }else{
        console.log("Negitive Odd")
    }
}

// Question-5
let units = 100;
if (units<50){
    console.log("₹2 per unit")
}else if(units<150){
    console.log("₹4 per unit")
}else{
    console.log("₹6 per unit")
}
let totalBill = units*4
console.log(totalBill)